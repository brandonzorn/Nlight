from PySide6.QtCore import QLocale


class BaseItem:
    def __init__(self, item_id: str, content_id: str, catalog_id: int, name: str, russian: str):
        self.id = item_id
        self.content_id = content_id
        self.catalog_id = catalog_id
        self.name = name
        self.russian = russian

    def get_name(self) -> str:
        if QLocale().language() in (QLocale.Language.Russian, QLocale.Language.Ukrainian):
            if self.russian:
                return self.russian
        return self.name.capitalize()

    @staticmethod
    def get_empty_instance():
        item_name = 'base_item'
        return BaseItem(item_name, item_name, -1, item_name, item_name)
