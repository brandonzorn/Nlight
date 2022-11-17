from nlightreader.items.BaseItem import BaseItem


class Character(BaseItem):
    def __init__(self, item_id, name, russian, description, role):
        super().__init__(item_id, name, russian)
        self.description = description
        self.role = role
