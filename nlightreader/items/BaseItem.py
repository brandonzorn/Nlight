class BaseItem:
    def __init__(self, item_id: str, name: str, russian: str):
        self.id = item_id
        self.name = name
        self.russian = russian

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name
