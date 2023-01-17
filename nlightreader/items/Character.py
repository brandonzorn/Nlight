from nlightreader.items.BaseItem import BaseItem


class Character(BaseItem):
    def __init__(self, item_id, content_id: str, catalog_id: int, name, russian, description, role):
        super().__init__(item_id, content_id, catalog_id, name, russian)
        self.description = description
        self.role = role
