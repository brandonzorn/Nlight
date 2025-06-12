import logging

from nlightreader.consts.enums import Nl
from nlightreader.consts.items import MangaDexItems
from nlightreader.consts.urls import (
    MANGA_DEX_HEADERS,
    URL_MANGA_DEX,
    URL_MANGA_DEX_API,
    URL_MANGA_DEX_TOKEN,
)
from nlightreader.items import (
    RequestForm,
    User,
)
from nlightreader.models import Chapter, Genre, Image, Kind, Manga
from nlightreader.parsers.catalog import LibParser
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.decorators import singleton
from nlightreader.utils.token import TokenManager
from nlightreader.utils.utils import get_data, get_html, make_request

try:
    from keys import MANGADEX_CLIENT_ID, MANGADEX_CLIENT_SECRET
except (ModuleNotFoundError, ImportError):
    logging.info("MangaDex API keys not found")
    MANGADEX_CLIENT_ID, MANGADEX_CLIENT_SECRET = "", ""


class MangaDex(AbstractMangaCatalog):
    CATALOG_ID = 2
    CATALOG_NAME = "MangaDex"

    def __init__(self):
        super().__init__()
        self.url = URL_MANGA_DEX
        self.url_api = URL_MANGA_DEX_API
        self.headers = MANGA_DEX_HEADERS
        self.items = MangaDexItems

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self.url_api}/manga/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            data = get_data(response, ["data"])
            manga.kind = Nl.MangaKind.from_str(data.get("type"))
            if description := get_data(data, ["attributes", "description"]):
                if description.get("en"):
                    manga.add_description(
                        Nl.Language.en,
                        description.get("en"),
                    )
                if description.get("ru"):
                    manga.add_description(
                        Nl.Language.ru,
                        description.get("ru"),
                    )
            if volumes := get_data(data, ["attributes", "lastVolume"]):
                manga.volumes = int(volumes)
            if chapters := get_data(data, ["attributes", "lastChapter"]):
                manga.chapters = int(chapters)
            manga.status = Nl.MangaStatus.from_str(
                get_data(data, ["attributes", "status"]),
            )
        return manga

    def setup_manga(self, data: dict):
        manga_id = str(data.get("id"))
        name = get_data(data, ["attributes", "title", "en"])
        russian = None
        alt_titles = get_data(data, ["attributes", "altTitles"])
        for j in alt_titles:
            if "ru" in j.keys():
                russian = j.get("ru")
            if not name and "en" in j.keys():
                name = j.get("en")
        return Manga(manga_id, self.CATALOG_ID, name, russian)

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}/manga"
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
        response = get_html(
            url,
            headers=self.headers,
            params=params,
            content_type="json",
        )

        mangas = []
        if not response:
            return mangas

        for i in get_data(response, ["data"]):
            mangas.append(self.setup_manga(i))
        return mangas

    def get_chapters(self, manga: Manga):
        url = f"{self.url_api}/chapter"
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
        response = get_html(
            url,
            headers=self.headers,
            params=params,
            content_type="json",
        )
        chapters = []
        if response:
            params.update({"limit": 100})
            for j in range(response.get("total") // 100 + 1):
                params.update({"offset": j * 100})
                html = get_html(url, headers=self.headers, params=params)
                for i in get_data(html.json(), ["data"]):
                    attr = i.get("attributes")
                    chapter = Chapter(
                        i.get("id"),
                        self.CATALOG_ID,
                        attr.get("volume"),
                        attr.get("chapter"),
                        attr.get("title"),
                        Nl.Language.from_str(
                            attr.get("translatedLanguage"),
                        ),
                    )
                    chapters.append(chapter)
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/at-home/server/{chapter.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        images = []
        if response:
            img_host = response["baseUrl"]
            img_hash = response["chapter"]["hash"]
            images_data = get_data(response, ["chapter", "data"])
            for img_index, img_data in enumerate(images_data):
                img_url = f"{img_host}/data/{img_hash}/{img_data}"
                page = img_index + 1
                images.append(Image("", page, img_url))
        return images

    def get_image(self, image: Image):
        return get_html(
            image.url,
            headers=self.headers,
            content_type="content",
        )

    def get_preview(self, manga: Manga):
        url = f"{self.url_api}/cover"
        params = {"manga[]": manga.content_id}
        covers_list_response = get_html(
            url,
            params=params,
            headers=self.headers,
            content_type="json",
        )
        filename = ""
        if covers_list_response:
            filename = covers_list_response["data"][0]["attributes"][
                "fileName"
            ]
        return get_html(
            f"https://uploads.mangadex.org/"
            f"covers/{manga.content_id}/{filename}.256.jpg",
            content_type="content",
        )

    def get_genres(self):
        url = f"{self.url_api}/manga/tag"
        response = get_html(
            url,
            headers=self.headers,
            content_type="json",
        )
        genres = []
        if response:
            for i in response.get("data"):
                if i.get("attributes").get("group") not in ["genre", "theme"]:
                    continue
                genres.append(
                    Genre(
                        i.get("id"),
                        self.CATALOG_ID,
                        get_data(i, ["attributes", "name", "en"]),
                        "",
                    ),
                )
        return genres

    def get_kinds(self):
        url = f"{self.url_api}/manga/tag"
        response = get_html(url, headers=self.headers, content_type="json")
        kinds = []
        if response:
            for i in list(
                filter(
                    lambda x: x["attributes"]["group"] in ["format"],
                    response["data"],
                ),
            ):
                kinds.append(
                    Kind(
                        i.get("id"),
                        self.CATALOG_ID,
                        i.get("attributes").get("name").get("en"),
                        "",
                    ),
                )
        return kinds

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/title/{manga.content_id}"


class MangaDexLib(MangaDex, LibParser):
    def __init__(self):
        super().__init__()
        self.fields = 2
        self.session = Auth()

    def search_manga(self, form: RequestForm):
        mangas = []
        lib_list = form.lib_list.name
        if form.lib_list == Nl.LibList.planned:
            lib_list = "plan_to_read"
        response_statuses = self.session.get(
            f"{self.url_api}/manga/status",
            params={"status": lib_list},
        )
        params = {"limit": form.limit, "offset": form.offset}
        response = self.session.get(
            f"{self.url_api}/user/follows/manga",
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

    def get_user(self):
        response = self.session.get(f"{self.url_api}/user/me")
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
    def __init__(self):
        self.url_api = URL_MANGA_DEX_API
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

    def update_token(self, token: dict):
        if token and "access_token" in token and "refresh_token" in token:
            token = {
                "access_token": token["access_token"],
                "refresh_token": token["refresh_token"],
            }
            TokenManager.save_token(token, catalog_name=MangaDex.CATALOG_NAME)
            self.tokens = token

    def refresh_token(self):
        request_data = self._refresh_headers
        response = make_request(
            URL_MANGA_DEX_TOKEN,
            "POST",
            data=request_data,
            content_type="json",
        )
        if response:
            self.update_token(response)
            self.is_authorized = True
        else:
            self.is_authorized = False

    def auth_login(self, params):
        request_data = self._auth_headers | params
        response = make_request(
            URL_MANGA_DEX_TOKEN,
            "POST",
            data=request_data,
            content_type="json",
        )
        if response:
            self.update_token(response)
            self.is_authorized = True
        else:
            self.refresh_token()

    def get(self, url, params=None):
        if not self.is_authorized:
            return None
        return get_html(url, params=params, headers=self.headers)

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.tokens.get('access_token')}"}

    @property
    def _refresh_headers(self):
        return {
            "grant_type": "refresh_token",
            "refresh_token": self.tokens["refresh_token"],
        } | self.client_headers

    @property
    def _auth_headers(self):
        return {"grant_type": "password"} | self.client_headers


__all__ = [
    "MangaDex",
    "MangaDexLib",
]
