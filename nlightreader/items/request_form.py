from nlightreader.consts.enums import Nl
from nlightreader.models.sort_models import Genre, Kind, Order


class RequestForm:
    def __init__(self) -> None:
        self.limit = 50
        self.search = ""
        self.page = 1
        self.__genres: list[Genre] = []
        self.__order: Order | None = None
        self.__kinds: list[Kind] = []
        self.lib_list = Nl.LibList.planned

    @property
    def offset(self) -> int:
        return (self.page - 1) * 50

    def set_order(self, order: Order) -> None:
        self.__order = order

    def set_kinds(self, kinds: list[Kind]) -> None:
        self.__kinds = kinds

    def set_genres(self, genres: list[Genre]) -> None:
        self.__genres = genres

    def get_order_id(self) -> str:
        return self.__order.content_id

    def get_kind_ids(self) -> list[str]:
        return [kind.content_id for kind in self.__kinds]

    def get_genre_ids(self) -> list[str]:
        return [genre.content_id for genre in self.__genres]

    def clear(self) -> None:
        self.limit = 50
        self.search = ""
        self.page = 1
        self.__genres = []
        self.__order = None
        self.__kinds = []
        self.lib_list = Nl.LibList.planned


__all__ = [
    "RequestForm",
]
