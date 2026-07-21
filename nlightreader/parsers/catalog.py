from enum import IntEnum
from typing import ClassVar

from nlightreader.consts.items.parser_items import ParserItems
from nlightreader.consts.urls import DEFAULT_HEADERS
from nlightreader.core.network import OAuthClient
from nlightreader.items import (
    RequestForm,
    User,
    UserRate,
)
from nlightreader.models import (
    Chapter,
    Character,
    Genre,
    Image,
    Kind,
    Manga,
    Order,
)


class CatalogAuthType(IntEnum):
    NO_AUTH = 0
    TOKEN = 1
    CREDENTIALS = 2


class AbstractCatalog:
    AUTH_TYPE: ClassVar[CatalogAuthType] = CatalogAuthType.NO_AUTH
    CATALOG_NAME = "CATALOG"
    CATALOG_ID = -1
    is_primary = False
    _HEADERS: ClassVar = DEFAULT_HEADERS
    _COOKIES: ClassVar = None
    _FILTERS: ClassVar = ParserItems

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def get_character(self, character: Character) -> Character:
        return character

    def search_manga(self, form: RequestForm) -> list[Manga]:
        raise NotImplementedError

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        raise NotImplementedError

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        raise NotImplementedError

    def get_image(self, image: Image) -> bytes | str | None:
        raise NotImplementedError

    def get_preview(self, manga: Manga) -> bytes | None:
        raise NotImplementedError

    def get_character_preview(self, character: Character) -> bytes | None:
        raise NotImplementedError

    def get_genres(self) -> list[Genre]:
        return [
            Genre(
                content_id=i["value"],
                catalog_id=self.CATALOG_ID,
                name=i["name"],
                russian=i["russian"],
            )
            for i in self._FILTERS.GENRES
        ]

    def get_kinds(self) -> list[Kind]:
        return [
            Kind(
                content_id=i["value"],
                catalog_id=self.CATALOG_ID,
                name=i["name"],
                russian=i["russian"],
            )
            for i in self._FILTERS.KINDS
        ]

    def get_orders(self) -> list[Order]:
        return [
            Order(
                content_id=i["value"],
                catalog_id=self.CATALOG_ID,
                name=i["name"],
                russian=i["russian"],
            )
            for i in self._FILTERS.ORDERS
        ]

    def get_relations(self, manga: Manga) -> list[Manga]:
        raise NotImplementedError

    def get_characters(self, manga: Manga) -> list[Character]:
        raise NotImplementedError

    def get_manga_url(self, manga: Manga) -> str:
        raise NotImplementedError


class LibParser:
    AUTH_TYPE: CatalogAuthType = CatalogAuthType.NO_AUTH

    def __init__(self) -> None:
        self._client = None

    @property
    def session(self) -> OAuthClient:
        if self._client is None:
            msg = "session is not implemented"
            raise NotImplementedError(msg)
        return self._client

    def search_manga(self, form: RequestForm) -> list[Manga]:
        raise NotImplementedError

    def get_user(self) -> User:
        raise NotImplementedError

    def create_user_rate(self, manga: Manga) -> None:
        raise NotImplementedError

    def check_user_rate(self, manga: Manga) -> bool:
        raise NotImplementedError

    def delete_user_rate(self, user_rate: UserRate) -> None:
        raise NotImplementedError

    def get_user_rate(self, manga: Manga) -> UserRate | None:
        raise NotImplementedError

    def update_user_rate(self, user_rate: UserRate) -> None:
        raise NotImplementedError


__all__ = [
    "AbstractCatalog",
    "CatalogAuthType",
    "LibParser",
]
