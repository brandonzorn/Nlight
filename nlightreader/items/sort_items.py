from nlightreader.items.BaseItem import BaseItem


class Kind(BaseItem):
    def __init__(self, content_id: str, catalog_id: int, name, russian):
        super().__init__(content_id, catalog_id, name, russian)


class Order(BaseItem):
    def __init__(self, content_id: str, catalog_id: int, name, russian):
        super().__init__(content_id, catalog_id, name, russian)


class Genre(BaseItem):
    def __init__(self, content_id: str, catalog_id: int, name, russian):
        super().__init__(content_id, catalog_id, name, russian)


class Status(BaseItem):
    def __init__(self, content_id: str, catalog_id: int, name, russian):
        super().__init__(content_id, catalog_id, name, russian)
