from PySide6.QtCore import QLocale

from nlightreader.utils.config import cfg


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


class NamedBaseModel(BaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ):
        super().__init__(content_id, catalog_id)
        self.__name = name
        self.__russian = russian

    @property
    def name(self):
        return self.__name

    @property
    def russian(self):
        return self.__russian

    def get_name(self) -> str:
        locale = cfg.get(cfg.language).value.language()
        if (
            locale
            in (
                QLocale.Language.Russian,
                QLocale.Language.Ukrainian,
            )
            and self.__russian
        ):
            return self.__russian
        return self.__name
