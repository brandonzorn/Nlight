from nlightreader.consts.enums import Nl
from nlightreader.consts.items import ShikimoriAnimeItems
from nlightreader.consts.urls import (
    SHIKIMORI_HEADERS,
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
)
from nlightreader.items import (
    RequestForm,
)
from nlightreader.models import Chapter, Character, Genre, Manga, Order
from nlightreader.parsers.catalogs_base import AbstractAnimeCatalog
from nlightreader.parsers.service.kodik import Kodik
from nlightreader.utils.utils import get_html


class ShikimoriAnime(AbstractAnimeCatalog):
    CATALOG_ID = 11
    CATALOG_NAME = "Shikimori(Anime)"
    _URL = URL_SHIKIMORI
    _URL_API = URL_SHIKIMORI_API
    _HEADERS = SHIKIMORI_HEADERS

    def _setup_manga(self, data: dict) -> Manga:
        return Manga(
            str(data.get("id")),
            self.CATALOG_ID,
            data.get("name"),
            data.get("russian"),
        )

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/animes/{manga.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            data = response
            manga.score = float(data.get("score"))
            manga.status = Nl.MangaStatus.from_str(data.get("status"))

            if description := data.get("description"):
                manga.add_description(
                    Nl.Language.undefined,
                    description,
                )
        return manga

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/animes"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "order": form.get_order_id(),
            "genre": ",".join(form.get_genre_ids()),
            "kind": ",".join(form.get_kind_ids()),
        }
        response = get_html(
            url,
            headers=self._HEADERS,
            params=params,
            content_type="json",
        )

        mangas = []
        if response:
            for i in response:
                mangas.append(self._setup_manga(i))
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        translators = Kodik.search(manga.content_id)
        chapters = []
        for translator in translators:
            for episode_num in range(translator.episodes, 0, -1):
                chapter = Chapter(
                    f"{translator.content_id}{episode_num}",
                    self.CATALOG_ID,
                    None,
                    "",
                    f"Episode {episode_num}",
                    Nl.Language.ru,
                )
                chapter.translator = (
                    f"{translator.translator} ({translator.tr_type})"
                )
                chapter.__setattr__(
                    "url",
                    f"http:{translator.kodik_url}?episode={episode_num}",
                )
                chapters.append(chapter)
        return chapters

    def get_character(self, character: Character) -> Character:
        url = f"{self._URL_API}/characters/{character.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            if description := response.get("description"):
                character.description = description
        return character

    def get_preview(self, manga: Manga):
        return get_html(
            f"{self._URL}/system/animes/original/{manga.content_id}.jpg",
            content_type="content",
        )

    def get_character_preview(self, character: Character):
        return get_html(
            f"{self._URL}/system/characters/"
            f"original/{character.content_id}.jpg",
            content_type="content",
        )

    def get_genres(self) -> list[Genre]:
        url = f"{self._URL_API}/genres"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            return [
                Genre(
                    str(i["id"]),
                    self.CATALOG_ID,
                    i["name"],
                    i["russian"],
                )
                for i in response
                if i["entry_type"] == "Anime"
            ]
        return []

    def get_orders(self) -> list[Order]:
        return [
            Order(
                i["value"],
                self.CATALOG_ID,
                i["name"],
                i["russian"],
            )
            for i in ShikimoriAnimeItems.ORDERS
        ]

    def get_characters(self, manga: Manga) -> list[Character]:
        characters = []
        url = f"{self._URL_API}/animes/{manga.content_id}/roles"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            for i in response:
                if i.get("roles"):
                    role = i.get("roles")[0]
                    if role in ["Supporting", "Main"]:
                        data = i.get("character")
                        if data:
                            characters.append(
                                Character(
                                    str(data.get("id")),
                                    self.CATALOG_ID,
                                    data.get("name"),
                                    data.get("russian"),
                                    "",
                                    role,
                                ),
                            )
            characters.sort(key=lambda x: x.role)
        return characters

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/animes/{manga.content_id}"


__all__ = [
    "ShikimoriAnime",
]
