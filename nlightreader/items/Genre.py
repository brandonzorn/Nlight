from nlightreader.items.BaseItem import BaseItem


class Genre(BaseItem):
    def __init__(self, item_id, name, russian, kind):
        super().__init__(item_id, name, russian)
        self.kind = kind
