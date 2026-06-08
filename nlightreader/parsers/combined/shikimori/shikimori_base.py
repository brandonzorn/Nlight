from nlightreader.consts.items import ShikimoriItems
from nlightreader.consts.urls import (
    SHIKIMORI_HEADERS,
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
)
from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.models import Character, Genre, Manga, Order
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.utils import get_html


class ShikimoriBase(AbstractCatalog):
    CATALOG_ID = 1
    CATALOG_NAME = "Shikimori"
    is_primary = True
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
        url = f"{self._URL_API}/mangas/{manga.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            data = response
            manga.kind = MangaKind.from_str(data.get("kind"))
            manga.score = float(data.get("score"))
            manga.status = MangaStatus.from_str(data.get("status"))
            if data.get("volumes"):
                manga.volumes = int(data.get("volumes"))
            if data.get("chapters"):
                manga.chapters = int(data.get("chapters"))

            if description := data.get("description"):
                manga.add_description(
                    Language.undefined,
                    description,
                )
        return manga

    def get_character(self, character: Character) -> Character:
        url = f"{self._URL_API}/characters/{character.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response and (description := response.get("description")):
            character.description = description
        return character

    def get_preview(self, manga: Manga):
        return get_html(
            f"{self._URL}/system/mangas/original/{manga.content_id}.jpg",
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
        if not response:
            return []

        return [
            Genre(
                str(i["id"]),
                self.CATALOG_ID,
                i["name"],
                i["russian"],
            )
            for i in response
            if i["entry_type"] == "Manga"
        ]

    def get_orders(self) -> list[Order]:
        return [
            Order(
                i["value"],
                self.CATALOG_ID,
                i["name"],
                i["russian"],
            )
            for i in ShikimoriItems.ORDERS
        ]

    def get_relations(self, manga: Manga) -> list[Manga]:
        mangas = []
        url = f"{self._URL_API}/mangas/{manga.content_id}/related"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            for i in response:
                if manga_data := i.get("manga"):
                    mangas.append(
                        self._setup_manga(manga_data),
                    )
        return mangas

    def get_characters(self, manga: Manga) -> list[Character]:
        characters = []
        url = f"{self._URL_API}/mangas/{manga.content_id}/roles"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if not response:
            return characters

        for i in response:
            if roles_data := i.get("roles"):
                role = roles_data[0]
                if role in ["Supporting", "Main"]:
                    if data := i.get("character"):
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
        return f"{self._URL}/mangas/{manga.content_id}"


__all__ = [
    "ShikimoriBase",
]
