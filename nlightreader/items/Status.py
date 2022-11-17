class Status:
    def __init__(self, name, russian):
        self.name = name
        self.russian = russian

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name
