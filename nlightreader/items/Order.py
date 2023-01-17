from nlightreader.items.BaseItem import BaseItem


class Order(BaseItem):
    def __init__(self, item_id, content_id: str, catalog_id: int, name, russian):
        super().__init__(item_id, content_id, catalog_id, name, russian)
