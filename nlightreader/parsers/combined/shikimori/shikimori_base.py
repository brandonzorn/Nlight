from nlightreader.consts.items import ShikimoriItems
from nlightreader.consts.urls import (
    SHIKIMORI_HEADERS,
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
)
from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.models import Character, Genre, Manga, Order
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.network import NetworkClient


class ShikimoriBase(AbstractCatalog):
    CATALOG_ID = 1
    CATALOG_NAME = "Shikimori"
    is_primary = True
    _URL = URL_SHIKIMORI
    _URL_API = URL_SHIKIMORI_API
    _HEADERS = SHIKIMORI_HEADERS

    def __init__(self) -> None:
        self._client = NetworkClient(
            catalog_name=self.CATALOG_NAME,
            headers=self._HEADERS,
        )

    def _setup_manga(self, data: dict) -> Manga:
        return Manga(
            content_id=str(data.get("id", "")),
            catalog_id=self.CATALOG_ID,
            name=data.get("name", ""),
            russian=data.get("russian", ""),
        )

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/mangas/{manga.content_id}"
        response = self._client.get_json(url)
        if response:
            data = response
            manga.kind = MangaKind.from_str(data.get("kind"))
            manga.score = float(data.get("score", 0))
            manga.status = MangaStatus.from_str(data.get("status"))
            manga.volumes = int(data.get("volumes", 0))
            manga.chapters = int(data.get("chapters", 0))

            description = data.get("description")
            if isinstance(description, str):
                manga.add_description(
                    Language.UNDEFINED,
                    description,
                )
        return manga

    def get_character(self, character: Character) -> Character:
        url = f"{self._URL_API}/characters/{character.content_id}"
        response = self._client.get_json(url)
        if response and (description := response.get("description")):
            character.description = description
        return character

    def get_preview(self, manga: Manga) -> bytes | None:
        image_response = self._client.get_bytes(
            f"{self._URL}/system/mangas/original/{manga.content_id}.jpg",
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_character_preview(self, character: Character) -> bytes | None:
        image_response = self._client.get_bytes(
            f"{self._URL}/system/characters/"
            f"original/{character.content_id}.jpg",
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_genres(self) -> list[Genre]:
        url = f"{self._URL_API}/genres"
        response = self._client.get_json(url)
        genres: list[Genre] = []
        if not isinstance(response, list):
            return genres
        for data in response:
            if data.get("entry_type") != "Manga":
                continue
            genres.append(
                Genre(
                    content_id=str(data["id"]),
                    catalog_id=self.CATALOG_ID,
                    name=data["name"],
                    russian=data["russian"],
                ),
            )
        return genres

    def get_orders(self) -> list[Order]:
        return [
            Order(
                content_id=i["value"],
                catalog_id=self.CATALOG_ID,
                name=i["name"],
                russian=i["russian"],
            )
            for i in ShikimoriItems.ORDERS
        ]

    def get_relations(self, manga: Manga) -> list[Manga]:
        url = f"{self._URL_API}/mangas/{manga.content_id}/related"
        response = self._client.get_json(url)
        mangas: list[Manga] = []
        if not isinstance(response, list):
            return mangas
        for i in response:
            manga_data = i.get("manga", {})
            if not manga_data:
                continue
            mangas.append(self._setup_manga(manga_data))
        return mangas

    def get_characters(self, manga: Manga) -> list[Character]:
        characters = []
        url = f"{self._URL_API}/mangas/{manga.content_id}/roles"
        response = self._client.get_json(url)
        if not response:
            return characters

        for i in response:
            roles_data = i.get("roles")
            if not roles_data:
                continue
            role = roles_data[0]
            if role not in ("Supporting", "Main"):
                continue
            data = i.get("character")
            if not data:
                continue
            characters.append(
                Character(
                    content_id=str(data.get("id")),
                    catalog_id=self.CATALOG_ID,
                    name=data.get("name"),
                    russian=data.get("russian"),
                    description="",
                    role=role,
                ),
            )
        characters.sort(key=lambda x: x.role)
        return characters

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/mangas/{manga.content_id}"


__all__ = ["ShikimoriBase"]
