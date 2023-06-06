from PySide6.QtCore import QLocale


class BaseItem:
    def __init__(self, content_id: str, catalog_id: int, name: str, russian: str):
        self.id = f'|{catalog_id}|_|{content_id}|'
        self.content_id = content_id
        self.catalog_id = catalog_id
        self.name = name
        self.russian = russian

    def __eq__(self, other):
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)

    def get_name(self) -> str:
        if QLocale().language() in (QLocale.Language.Russian, QLocale.Language.Ukrainian):
            if self.russian:
                return self.russian
        return self.name.capitalize()

    @staticmethod
    def get_empty_instance():
        item_name = 'base_item'
        return BaseItem(item_name, -1, item_name, item_name)
