from nlightreader.items.BaseItem import BaseItem


class Order(BaseItem):
    def __init__(self, item_id, name, russian):
        super().__init__(item_id, name, russian)
