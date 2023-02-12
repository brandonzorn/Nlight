from PySide6.QtCore import QLocale

from nlightreader.items.BaseItem import BaseItem
from nlightreader.items.sort_items import Genre


class Manga(BaseItem):
    def __init__(self, content_id: str, catalog_id, name, russian):
        super().__init__(content_id, catalog_id, name, russian)
        self.kind = None
        self.description = ""
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


class Chapter:
    def __init__(self, content_id: str, catalog_id: int, vol: str, ch: str, title: str, language: str):
        self.id = f'|{catalog_id}|_|{content_id}|'
        self.content_id = content_id
        self.catalog_id = catalog_id
        self.vol = vol
        self.ch = ch
        self.title = title
        self.language = language

    def get_name(self) -> str:
        if not self.vol and not self.ch:
            return self.title
        if self.title:
            return f'{self.vol}-{self.ch} {self.title}'
        return f'{self.vol}-{self.ch}'


class Image:
    def __init__(self, image_id: str, page: int, img: str):
        self.id = image_id
        self.page = page
        self.img = img

    @staticmethod
    def get_empty_instance():
        item_name = 'image'
        return Image(item_name, 1, '')


class Character(BaseItem):
    def __init__(self, content_id: str, catalog_id: int, name, russian, description, role):
        super().__init__(content_id, catalog_id, name, russian)
        self.description = description
        self.role = role
