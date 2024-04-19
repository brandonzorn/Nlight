from PySide6.QtCore import QLocale


class BaseItem:
    def __init__(self, content_id: str, catalog_id: int, name: str, russian: str):
        self.__id = f"|{catalog_id}|_|{content_id}|"
        self.__content_id = content_id
        self.__catalog_id = catalog_id
        self.name = name
        self.russian = russian

    def __eq__(self, other):
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)

    @property
    def id(self):
        return self.__id

    @property
    def content_id(self):
        return self.__content_id

    @property
    def catalog_id(self):
        return self.__catalog_id

    def get_name(self) -> str:
        if QLocale().language() in (
                QLocale.Language.Russian, QLocale.Language.Ukrainian,
        ) and self.russian:
            return self.russian
        return self.name

    @staticmethod
    def get_empty_instance():
        item_name = "base_item"
        return BaseItem(item_name, -1, item_name, item_name)
