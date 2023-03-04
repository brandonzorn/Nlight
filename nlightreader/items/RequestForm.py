from nlightreader.consts import LibList
from nlightreader.items.sort_items import Order, Genre, Kind


class RequestForm:
    def __init__(self):
        self.limit = 50
        self.search = ''
        self.page = 1
        self.genres: list[Genre] = []
        self.order: Order = Order.get_empty_instance()
        self.kinds: list[Kind] = []
        self.lib_list = LibList.planned

    @property
    def offset(self):
        return (self.page - 1) * 50

    def get_kind_id(self) -> list[str]:
        return [kind.content_id for kind in self.kinds]

    def get_genre_id(self) -> list[str]:
        return [genre.content_id for genre in self.genres]

    def clear(self):
        self.limit = 50
        self.search = ''
        self.page = 1
        self.genres = []
        self.order = Order.get_empty_instance()
        self.kinds = []
        self.lib_list = LibList.planned
