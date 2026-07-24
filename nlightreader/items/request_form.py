from collections.abc import Collection

from nlightreader.core.enums import LibList
from nlightreader.models.sort_models import Genre, Kind, Order


class RequestForm:
    def __init__(self) -> None:
        self.limit: int = 50
        self.search = ""
        self.page: int = 1
        self._genres: Collection[Genre] = []
        self._kinds: Collection[Kind] = []
        self._order: Order | None = None
        self.lib_list = LibList.planned

    @property
    def offset(self) -> int:
        return (self.page - 1) * 50

    def set_order(self, order: Order | None) -> None:
        self._order = order

    def set_kinds(self, kinds: Collection[Kind]) -> None:
        self._kinds = kinds

    def set_genres(self, genres: Collection[Genre]) -> None:
        self._genres = genres

    def get_order_id(self) -> str | None:
        if self._order is None:
            return None
        return self._order.content_id

    def get_kind_ids(self) -> set[str]:
        return {kind.content_id for kind in self._kinds}

    def get_genre_ids(self) -> set[str]:
        return {genre.content_id for genre in self._genres}

    def clear(self) -> None:
        self.limit = 50
        self.search = ""
        self.page = 1
        self._genres = []
        self._kinds = []
        self._order = None
        self.lib_list = LibList.planned


__all__ = ["RequestForm"]
