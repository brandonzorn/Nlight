from PySide6.QtCore import QLocale


class BaseItem:
    def __init__(self, item_id: str, name: str, russian: str):
        self.id = item_id
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
        return BaseItem(item_name, item_name, item_name)
