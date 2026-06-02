from PySide6.QtCore import QLocale

from nlightreader.utils.config import cfg


class BaseModel:
    def __init__(self, content_id: str, catalog_id: int) -> None:
        self.__id = f"|{catalog_id}|_|{content_id}|"
        self.__content_id = content_id
        self.__catalog_id = catalog_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseModel):
            return False
        return self.__id == other.id

    def __hash__(self) -> int:
        return hash(self.__id)

    @property
    def id(self) -> str:
        return self.__id

    @property
    def content_id(self) -> str:
        return self.__content_id

    @property
    def catalog_id(self) -> int:
        return self.__catalog_id

    def to_dict(self) -> dict:
        return {
            "content_id": self.__content_id,
            "catalog_id": self.__catalog_id,
            "id": self.__id,
        }


class NamedBaseModel(BaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ) -> None:
        super().__init__(content_id, catalog_id)
        self.__name = name
        self.__russian = russian

    @property
    def name(self) -> str:
        return self.__name

    @property
    def russian(self) -> str:
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

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "name": self.__name,
                "russian": self.__russian,
            },
        )
        return data


__all__ = [
    "BaseModel",
    "NamedBaseModel",
]
