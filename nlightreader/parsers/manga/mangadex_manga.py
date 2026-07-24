import logging
from typing import Any, ClassVar, override

import requests

from nlightreader.consts.items import MangaDexItems
from nlightreader.core.enums import Language, LibList, MangaKind, MangaStatus
from nlightreader.core.utils.decorators import singleton
from nlightreader.items import RequestForm, User
from nlightreader.models import Chapter, Genre, Image, Kind, Manga
from nlightreader.parsers.catalog import CatalogAuthType, LibParser
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.network import NetworkClient
from nlightreader.utils.token import TokenManager
from nlightreader.utils.utils import dd_get, make_request

logger = logging.getLogger(__name__)

try:
    from keys import MANGADEX_CLIENT_ID, MANGADEX_CLIENT_SECRET
except (ModuleNotFoundError, ImportError):
    logger.warning("MangaDex API keys not found")


class MangaDex(AbstractMangaCatalog):
    AUTH_TYPE = CatalogAuthType.CREDENTIALS
    CATALOG_ID = 2
    CATALOG_NAME = "MangaDex"
    _FILTERS = MangaDexItems
    _URL = "https://mangadex.org"
    _URL_API = "https://api.mangadex.org"
    _HEADERS: ClassVar = {"User-Agent": "Nlight"}

    def __init__(self) -> None:
        self._client = NetworkClient(headers=self._HEADERS)

    @override
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

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/manga"
        params = {
            "limit": 50,
            f"order[{form.get_order_id()}]": "desc",
            "title": form.search,
            "offset": form.offset,
            "includedTags[]": form.get_genre_ids() | form.get_kind_ids(),
            "contentRating[]": [
                "safe",
                "suggestive",
                "erotica",
                "pornographic",
            ],
        }
        mangas: list[Manga] = []

        response = self._client.get_json(url, params=params)
        if not isinstance(response, dict):
            return mangas

        manga_data = response.get("data")
        if not isinstance(manga_data, list):
            return mangas

        mangas.extend(self._parse_manga_data(data) for data in manga_data)
        return mangas

    @override
    def get_chapters(self, manga: Manga) -> list[Chapter]:
        items_per_page = 100
        url = f"{self._URL_API}/chapter"
        params = {
            "manga": manga.content_id,
            "limit": items_per_page,
            "translatedLanguage[]": ["ru", "en", "uk"],
            "order[chapter]": "desc",
            "contentRating[]": [
                "safe",
                "suggestive",
                "erotica",
                "pornographic",
            ],
        }
        chapters: list[Chapter] = []

        response = self._client.get_json(url, params=params)
        if not isinstance(response, dict):
            return chapters
        chunk_data = response.get("data", {})
        chapters.extend(self._parse_chapters_data(chunk_data))

        total = dd_get(response, "total")
        if not isinstance(total, int):
            return chapters

        params.update({"limit": items_per_page})
        for page in range(1, total // items_per_page + 1):
            params.update({"offset": page * items_per_page})
            chunk_response = self._client.get_json(url, params=params)
            if not isinstance(chunk_response, dict):
                continue

            chunk_data = chunk_response.get("data", {})
            chapters.extend(self._parse_chapters_data(chunk_data))
        return chapters

    @override
    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = f"{self._URL_API}/at-home/server/{chapter.content_id}"
        response = self._client.get_json(url)
        images: list[Image] = []
        if not isinstance(response, dict):
            return images
        img_host = response.get("baseUrl")
        if not isinstance(img_host, str):
            return images
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

    @override
    def get_image(self, image: Image) -> bytes | None:
        url = image.url
        if url is None:
            return None
        return self._client.get_bytes(url)

    @override
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

    @override
    def get_genres(self) -> list[Genre]:
        return [
            Genre(**tag_data)
            for tag_data in self._get_tags_by_group("genre", "theme")
        ]

    @override
    def get_kinds(self) -> list[Kind]:
        return [
            Kind(**tag_data) for tag_data in self._get_tags_by_group("format")
        ]

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/title/{manga.content_id}"

    def _get_tags_by_group(self, *args: str) -> list[dict]:
        url = f"{self._URL_API}/manga/tag"
        response = self._client.get_json(url)
        tags: list[dict] = []
        if not isinstance(response, dict):
            return tags
        tags_data = response.get("data", {})
        for tag_data in tags_data:
            group_name = dd_get(tag_data, "attributes.group")
            if group_name not in args:
                continue
            content_id = dd_get(tag_data, "id")
            name = dd_get(tag_data, "attributes.name.en")
            if not isinstance(name, str):
                continue
            tags.append(
                {
                    "content_id": content_id,
                    "catalog_id": self.CATALOG_ID,
                    "name": name,
                    "russian": "",
                },
            )
        return tags

    def _parse_manga_data(self, data: dict) -> Manga:
        manga_id = dd_get(data, "id", "")
        name = dd_get(data, "attributes.title.en")
        russian = ""
        alt_titles = dd_get(data, "attributes.altTitles")
        if not isinstance(alt_titles, list):
            alt_titles = []
        for j in alt_titles:
            if not isinstance(j, dict):
                continue
            if "ru" in j:
                russian = str(j.get("ru") or "")
            if not name and "en" in j:
                name = j.get("en")
        if not isinstance(name, str):
            name = ""
        return Manga(
            content_id=manga_id,
            catalog_id=self.CATALOG_ID,
            name=name,
            russian=russian,
        )

    def _parse_chapters_data(self, data: list[dict]) -> list[Chapter]:
        chapters = []
        for chapter_data in reversed(data):
            attrs = chapter_data.get("attributes")
            if not isinstance(attrs, dict):
                continue
            if "id" not in chapter_data:
                continue
            chapters.append(
                Chapter(
                    content_id=chapter_data["id"],
                    catalog_id=self.CATALOG_ID,
                    volume_number=attrs.get("volume"),
                    chapter_number=attrs.get("chapter"),
                    title=attrs.get("title", ""),
                    language=Language.from_str(
                        attrs.get("translatedLanguage"),
                    ),
                ),
            )
        chapters.reverse()
        return chapters


class MangaDexLib(MangaDex, LibParser):
    def __init__(self) -> None:
        super().__init__()
        self.fields = 2
        self._session = Auth()

    def search_manga(self, form: RequestForm) -> list[Manga]:
        mangas = []
        lib_list = form.lib_list.name
        if form.lib_list == LibList.planned:
            lib_list = "plan_to_read"
        response_statuses = self._session.get(
            f"{self._URL_API}/manga/status",
            params={"status": lib_list},
        )
        params = {"limit": form.limit, "offset": form.offset}
        response = self._session.get(
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
        response = self._session.get(f"{self._URL_API}/user/me")
        if response and (resp_json := response.json()):
            data = resp_json.get("data")
            return User(
                data.get("id"),
                data.get("attributes").get("username"),
                "",
            )
        return User(None, None, None)


@singleton
class Auth:
    _URL_TOKEN = (
        "https://auth.mangadex.org/"
        "realms/mangadex/protocol/openid-connect/token"
    )

    def __init__(self) -> None:
        self.tokens = TokenManager.load_token(MangaDex.CATALOG_NAME)

        self.client_headers = {
            "client_id": MANGADEX_CLIENT_ID,
            "client_secret": MANGADEX_CLIENT_SECRET,
        }

        self.is_authorized = False

        if self.check_token():
            self.refresh_token()

    def check_token(self) -> bool:
        if not self.tokens:
            return False
        if "access_token" in self.tokens and "refresh_token" in self.tokens:
            return True
        return False

    def update_token(self, token: dict) -> None:
        if token and "access_token" in token and "refresh_token" in token:
            token = {
                "access_token": token["access_token"],
                "refresh_token": token["refresh_token"],
            }
            TokenManager.save_token(token, catalog_name=MangaDex.CATALOG_NAME)
            self.tokens = token

    def refresh_token(self) -> None:
        request_data = self._refresh_headers
        response = make_request(
            self._URL_TOKEN,
            "POST",
            data=request_data,
            content_type="json",
        )
        if response:
            self.update_token(response)
            self.is_authorized = True
        else:
            self.is_authorized = False

    def auth_login(self, params: dict[str, Any] | None) -> None:
        request_data = self._auth_headers | params
        response = make_request(
            self._URL_TOKEN,
            "POST",
            data=request_data,
            content_type="json",
        )
        if response:
            self.update_token(response)
            self.is_authorized = True
        else:
            self.refresh_token()

    def get(
        self,
        url: str,
        params: dict[str, Any] | None = None,
    ) -> None | bytes | str | dict | requests.Response:
        if not self.is_authorized:
            return None
        return make_request(url, "GET", params=params, headers=self.headers)

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.tokens.get('access_token')}"}

    @property
    def _refresh_headers(self) -> dict[str, str]:
        return {
            "grant_type": "refresh_token",
            "refresh_token": self.tokens["refresh_token"],
        } | self.client_headers

    @property
    def _auth_headers(self) -> dict[str, str]:
        return {"grant_type": "password"} | self.client_headers


__all__ = [
    "MangaDex",
    "MangaDexLib",
]
