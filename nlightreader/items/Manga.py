from PySide6.QtCore import QLocale

from nlightreader.items import Genre
from nlightreader.items.BaseItem import BaseItem


class Manga(BaseItem):
    def __init__(self, item_id, content_id: str, catalog_id, name, russian):
        super().__init__(item_id, content_id, catalog_id, name, russian)
        self.kind = None
        self.description: str = ""
        self.score = 0
        self.status = None
        self.genres: list[Genre] = []
        self.volumes = 0
        self.chapters = 0

    def get_name(self) -> str:
        if QLocale().language() in (QLocale.Language.Russian, QLocale.Language.Ukrainian):
            if self.russian:
                return self.russian
        return self.name
