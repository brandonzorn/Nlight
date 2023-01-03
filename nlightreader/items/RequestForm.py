from nlightreader.consts import LibList
from nlightreader.items import Genre, Kind
from nlightreader.items.Order import Order


class RequestForm:
    def __init__(self):
        self.limit = 50
        self.search = ''
        self.page = 1
        self.genres: list[Genre] = []
        self.order: Order = Order('', '', '')
        self.kinds: list[Kind] = []
        self.lib_list = LibList.planned

    @property
    def offset(self):
        return (self.page - 1) * 50

    def clear(self):
        self.limit = 50
        self.search = ''
        self.page = 1
        self.genres = []
        self.order = Order('', '', '')
        self.kinds = []
        self.lib_list = LibList.planned
