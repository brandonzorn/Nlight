from nlightreader.items.BaseItem import BaseItem


class Manga(BaseItem):
    def __init__(self, item_id, catalog_id, name, russian):
        super().__init__(item_id, name, russian)
        self.catalog_id = catalog_id
        self.kind = None
        self.description: str = ""
        self.score = 0
        self.status = None
        self.genres: list[Genre] = []
        self.volumes = 0
        self.chapters = 0