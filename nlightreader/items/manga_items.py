from nlightreader.consts.enums import Nl
from nlightreader.items.BaseItem import BaseItem


class Chapter:
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        vol: str,
        ch: str,
        title: str,
        language: Nl.Language = Nl.Language.undefined,
    ):
        self.id = f"|{catalog_id}|_|{content_id}|"
        self.content_id = content_id
        self.catalog_id = catalog_id
        self.vol = vol
        self.ch = ch
        self.title = title
        self.__language = language
        self.translator = None

    def get_name(self) -> str:
        if not self.vol and not self.ch:
            return self.title
        if self.title:
            return f"{self.vol}-{self.ch} {self.title}"
        return f"{self.vol}-{self.ch}"

    @property
    def language(self):
        return self.__language

    def to_dict(self):
        return {
            "id": self.id,
            "content_id": self.content_id,
            "catalog_id": self.catalog_id,
            "vol": self.vol,
            "ch": self.ch,
            "title": self.title,
            "language": self.language.name,
        }


class Image:
    def __init__(self, image_id: str, page: int, img: str):
        self.id = image_id
        self.page = page
        self.img = img

    @staticmethod
    def get_empty_instance():
        item_name = "image"
        return Image(item_name, 1, "")


class Character(BaseItem):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name,
        russian,
        description,
        role,
    ):
        super().__init__(content_id, catalog_id, name, russian)
        self.description = description
        self.role = role
