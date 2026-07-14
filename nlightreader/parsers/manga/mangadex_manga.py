import logging
import os
from typing import Any

from authlib.integrations.requests_client import OAuth2Session
from authlib.oauth2.rfc6749 import OAuth2Token
import requests

from nlightreader.consts.items import MangaDexItems
from nlightreader.consts.urls import URL_MANGADEX_TOKEN
from nlightreader.core.enums import Language, LibList, MangaKind, MangaStatus
from nlightreader.core.utils.decorators import singleton
from nlightreader.items import RequestForm, User
from nlightreader.models import Chapter, Genre, Image, Kind, Manga
from nlightreader.parsers.catalog import CatalogAuthType, LibParser
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.network import NetworkClient
from nlightreader.utils.token import TokenManager
from nlightreader.utils.utils import dd_get

logger = logging.getLogger(__name__)

IS_TEST_ENV = os.getenv("TEST") == "1"

try:
    from keys import MANGADEX_CLIENT_ID, MANGADEX_CLIENT_SECRET
except (ModuleNotFoundError, ImportError):
    logger.warning("MangaDex API keys not found")
    MANGADEX_CLIENT_ID, MANGADEX_CLIENT_SECRET = "", ""


class MangaDex(AbstractMangaCatalog):
    AUTH_TYPE = CatalogAuthType.CREDENTIALS
    CATALOG_ID = 2
    CATALOG_NAME = "MangaDex"
    _FILTERS = MangaDexItems
    _URL = "https://mangadex.org"
    _URL_API = "https://api.mangadex.org"
    _HEADERS = {"User-Agent": "Nlight"}

    def __init__(self) -> None:
        self._client = NetworkClient(headers=self._HEADERS)

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/manga/{manga.content_id}"
        response = self._client.get_json(url)
        if not isinstance(response, dict) or not response:
            return manga
        data = response.get("data", {})
        manga.kind = MangaKind.from_str(data.get("type"))
        descriptions = dd_get(data, "attributes.description")
        if isinstance(descriptions, dict):
            en_d = descriptions.get("en")
            ru_d = descriptions.get("ru")
            if isinstance(en_d, str):
                manga.add_description(Language.ENGLISH, en_d)
            if isinstance(ru_d, str):
                manga.add_description(Language.RUSSIAN, ru_d)
        volumes = dd_get(data, "attributes.lastVolume")
        if volumes and isinstance(volumes, (int, str)):
            manga.volumes = int(volumes)
        chapters = dd_get(data, "attributes.lastChapter")
        if chapters and isinstance(chapters, (int, str)):
            manga.chapters = int(chapters)
        status = dd_get(data, "attributes.status")
        if isinstance(status, str):
            manga.status = MangaStatus.from_str(status)
        return manga

    def setup_manga(self, data: dict) -> Manga:
        manga_id = dd_get(data, "id", "")
        name = dd_get(data, "attributes.title.en", "")
        russian = ""
        alt_titles: list[dict[str, str]] = dd_get(
            data,
            "attributes.altTitles",
            [],
        )
        for j in alt_titles:
            if "ru" in j:
                russian = j.get("ru", "")
            if not name and "en" in j:
                name = j.get("en", "")
        return Manga(
            content_id=manga_id,
            catalog_id=self.CATALOG_ID,
            name=name,
            russian=russian,
        )

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/manga"
        params = {
            "limit": 50,
            f"order[{form.get_order_id()}]": "desc",
            "title": form.search,
            "offset": form.offset,
            "includedTags[]": form.get_genre_ids() + form.get_kind_ids(),
            "contentRating[]": [
                "safe",
                "suggestive",
                "erotica",
                "pornographic",
            ],
        }
        response = self._client.get_json(
            url,
            params=params,
        )

        mangas: list[Manga] = []
        if not isinstance(response, dict):
            return mangas
        mangas.extend(
            self.setup_manga(data) for data in response.get("data", {})
        )
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        items_per_page = 100
        url = f"{self._URL_API}/chapter"
        params = {
            "manga": manga.content_id,
            "limit": 1,
            "translatedLanguage[]": ["ru", "en", "uk"],
            "order[chapter]": "asc",
            "contentRating[]": [
                "safe",
                "suggestive",
                "erotica",
                "pornographic",
            ],
        }
        response = self._client.get_json(url, params=params)
        chapters: list[Chapter] = []
        if not isinstance(response, dict):
            return chapters
        total = dd_get(response, "total", -1)

        params.update({"limit": items_per_page})
        for j in range(total // items_per_page + 1):
            params.update({"offset": j * items_per_page})
            chunk_response = self._client.get_json(
                url,
                params=params,
            )
            if not isinstance(chunk_response, dict):
                continue
            for data in reversed(chunk_response.get("data", {})):
                attr = data.get("attributes")
                chapter = Chapter(
                    content_id=data.get("id"),
                    catalog_id=self.CATALOG_ID,
                    volume_number=attr.get("volume"),
                    chapter_number=attr.get("chapter"),
                    title=attr.get("title"),
                    language=Language.from_str(
                        attr.get("translatedLanguage"),
                    ),
                )
                chapters.append(chapter)
        return chapters

    def get_images(self, _: Manga, chapter: Chapter) -> list[Image]:
        url = f"{self._URL_API}/at-home/server/{chapter.content_id}"
        response = self._client.get_json(url)
        images: list[Image] = []
        if not isinstance(response, dict):
            return images
        img_host = response["baseUrl"]
        img_hash = dd_get(response, "chapter.hash")
        img_data = dd_get(response, "chapter.data")
        if not img_hash or not isinstance(img_data, list):
            return images
        for i, image in enumerate(img_data):
            images.append(
                Image(
                    content_id="",
                    page_number=i + 1,
                    url=f"{img_host}/data/{img_hash}/{image}",
                ),
            )
        return images

    def get_image(self, image: Image) -> bytes | None:
        url = image.url
        if url is None:
            return None
        return self._client.get_bytes(url)

    def get_preview(self, manga: Manga) -> bytes | None:
        url = f"{self._URL_API}/cover"
        params = {"manga[]": manga.content_id}
        covers_list_response = self._client.get_json(
            url,
            params=params,
        )
        if not isinstance(covers_list_response, dict):
            return None
        filename = covers_list_response["data"][0]["attributes"]["fileName"]
        return self._client.get_bytes(
            f"https://uploads.mangadex.org/"
            f"covers/{manga.content_id}/{filename}.256.jpg",
        )

    def _get_tags_data_by_group(self, groups: list[str]) -> list[dict]:
        url = f"{self._URL_API}/manga/tag"
        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return []
        data = response.get("data", {})
        return list(
            filter(
                lambda x: dd_get(x, "attributes.group") in groups,
                data,
            ),
        )

    def get_genres(self) -> list[Genre]:
        return [
            Genre(
                content_id=dd_get(tag_data, "id", ""),
                catalog_id=self.CATALOG_ID,
                name=dd_get(tag_data, "attributes.name.en"),
                russian="",
            )
            for tag_data in self._get_tags_data_by_group(["genre", "theme"])
        ]

    def get_kinds(self) -> list[Kind]:
        return [
            Kind(
                content_id=dd_get(tag_data, "id", ""),
                catalog_id=self.CATALOG_ID,
                name=dd_get(tag_data, "attributes.name.en"),
                russian="",
            )
            for tag_data in self._get_tags_data_by_group(["format"])
        ]

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/title/{manga.content_id}"


class MangaDexLib(MangaDex, LibParser):
    AUTH_TYPE = CatalogAuthType.CREDENTIALS

    def __init__(self) -> None:
        super().__init__()
        self._client = MangaDexClient(self.CATALOG_NAME, self._HEADERS)

    def search_manga(self, form: RequestForm) -> list[Manga]:
        mangas = []
        lib_list = form.lib_list.name
        if form.lib_list == LibList.planned:
            lib_list = "plan_to_read"
        response_statuses = self._client.request(
            "GET",
            f"{self._URL_API}/manga/status",
            params={"status": lib_list},
        )
        params = {"limit": form.limit, "offset": form.offset}
        response = self._client.request(
            "GET",
            f"{self._URL_API}/user/follows/manga",
            params=params,
        )
        if response and (resp_json := response.json()):
            for i in resp_json.get("data"):
                manga = self.setup_manga(i)
                if manga.content_id in response_statuses.json().get(
                    "statuses",
                ):
                    mangas.append(manga)
        return mangas

    def get_user(self) -> User:
        response = self._client.request("GET", f"{self._URL_API}/user/me")
        if response and (resp_json := response.json()):
            data = resp_json.get("data")
            return User(
                data.get("id"),
                data.get("attributes").get("username"),
                "",
            )
        return User(None, None, None)


@singleton
class MangaDexClient:
    def __init__(self, catalog_name: str, headers: dict[str, str]) -> None:
        self._is_authorized = False
        initial_token = OAuth2Token.from_dict(
            TokenManager.load_token(catalog_name),
        )

        self._session = OAuth2Session(
            client_id=MANGADEX_CLIENT_ID,
            client_secret=MANGADEX_CLIENT_SECRET,
            token=initial_token,
            token_endpoint=URL_MANGADEX_TOKEN,
            token_endpoint_auth_method="client_secret_post",
            update_token=self._token_saver,
        )
        self._session.session.headers.clear()
        self._session.session.headers.update(headers)
        if initial_token:
            self._update_actual_auth_status()

    @staticmethod
    def _token_saver(token: OAuth2Token, **_) -> None:
        if not token or "access_token" not in token:
            return
        TokenManager.save_token(
            token,
            catalog_name=MangaDexLib.CATALOG_NAME,
        )
        logger.info("OAuth token saved.")

    @property
    def authorized(self) -> bool:
        return self._is_authorized

    @property
    def token(self) -> OAuth2Token | None:
        return self._session.token

    @staticmethod
    def get_authorization_url() -> str:
        return ""

    def authorize(self, params: dict[str, str]) -> None:
        login, password = params.get("login"), params.get("password")
        if not login or not password:
            return
        token = self._session.fetch_token(
            username=login,
            password=password,
            grant_type="password",
        )
        self._token_saver(token)
        self._update_actual_auth_status()

    def _update_actual_auth_status(self) -> None:
        self._is_authorized = False
        url = f"{MangaDexLib._URL_API}/user/me"
        response = self.request("GET", url, ignore_authorize=True)
        if response is None:
            return
        data = response.json()
        self._is_authorized = bool(data)

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        ignore_authorize: bool = False,
    ) -> requests.Response | None:
        if (not ignore_authorize and not self._is_authorized) or IS_TEST_ENV:
            logger.warning(f"Request to {url} blocked: Unauthorized state.")
            return None
        try:
            response = self._session.request(
                method,
                url,
                params=params,
                json=json,
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(
                f"\n\tError fetching URL: {url}\n"
                f"\t\tReason: {e}\n"
                f"\t\tHeaders: {self._session.session.headers}\n"
                f"\t\tParams: {params}\n"
                f"\t\tCookies: {self._session.session.cookies}\n"
                f"\t\tJson: {json}\n",
            )
            if e.response is not None and e.response.status_code == 401:
                self._is_authorized = False


__all__ = [
    "MangaDex",
    "MangaDexLib",
]
