import json

from nlightreader.items import Order, Kind, Genre


class ParserItems:
    ORDERS: list[Order] = []
    KINDS: list[Kind] = []
    GENRES: list[Genre] = []


class ParserData:
    def __init__(self, parser_name):
        self.__parser_name = parser_name
        self.urls = {}
        self.filters = ParserItems()
        self.load_from_json()

    def load_from_json(self):
        with open(f"data/catalogs/{self.__parser_name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.urls = data["urls"]
            filters = data["filters"]
            self.filters.ORDERS = filters.get("orders", [])
            self.filters.KINDS = filters.get("kinds", [])
            self.filters.GENRES = filters.get("genres", [])

    def get_url(self, url_name):
        return self.urls[url_name]
