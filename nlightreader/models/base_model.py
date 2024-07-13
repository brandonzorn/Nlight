class BaseModel:
    def __init__(self, content_id: str, catalog_id: int):
        self.__id = f"|{catalog_id}|_|{content_id}|"
        self.__content_id = content_id
        self.__catalog_id = catalog_id

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

    def to_dict(self) -> dict:
        raise NotImplementedError
