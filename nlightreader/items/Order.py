from nlightreader.items.BaseItem import BaseItem


class Order(BaseItem):
    def __init__(self, content_id: str, catalog_id: int, name, russian):
        super().__init__(content_id, catalog_id, name, russian)
