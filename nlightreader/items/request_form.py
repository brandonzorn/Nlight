from nlightreader.core.enums import LibList
from nlightreader.models.sort_models import Genre, Kind, Order


class RequestForm:
    def __init__(self) -> None:
        self.limit = 50
        self.search = ""
        self.page = 1
        self._genres: list[Genre] = []
        self._order: Order | None = None
        self._kinds: list[Kind] = []
        self.lib_list = LibList.planned

    @property
    def offset(self) -> int:
        return (self.page - 1) * 50

    def set_order(self, order: Order) -> None:
        self._order = order

    def set_kinds(self, kinds: list[Kind]) -> None:
        self._kinds = kinds

    def set_genres(self, genres: list[Genre]) -> None:
        self._genres = genres

    def get_order_id(self) -> str:
        return self._order.content_id

    def get_kind_ids(self) -> list[str]:
        return [kind.content_id for kind in self._kinds]

    def get_genre_ids(self) -> list[str]:
        return [genre.content_id for genre in self._genres]

    def clear(self) -> None:
        self.limit = 50
        self.search = ""
        self.page = 1
        self._genres = []
        self._order = None
        self._kinds = []
        self.lib_list = LibList.planned


__all__ = ["RequestForm"]
