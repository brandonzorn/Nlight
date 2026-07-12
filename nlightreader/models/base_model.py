from PySide6.QtCore import QLocale

from nlightreader.utils.config import cfg


class BaseModel:
    def __init__(self, content_id: str, catalog_id: int) -> None:
        self._id = f"|{catalog_id}|_|{content_id}|"
        self._content_id = content_id
        self._catalog_id = catalog_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseModel):
            return NotImplemented
        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)

    @property
    def id(self) -> str:
        return self._id

    @property
    def content_id(self) -> str:
        return self._content_id

    @property
    def catalog_id(self) -> int:
        return self._catalog_id

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "content_id": self._content_id,
            "catalog_id": self._catalog_id,
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
        self._name = name
        self._russian = russian

    @property
    def name(self) -> str:
        return self._name

    @property
    def russian(self) -> str:
        return self._russian

    def get_name(self) -> str:
        locale = cfg.get(cfg.language).value.language()
        if (
            locale
            in (
                QLocale.Language.Russian,
                QLocale.Language.Ukrainian,
            )
            and self._russian
        ):
            return self._russian
        return self._name

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "name": self._name,
                "russian": self._russian,
            },
        )
        return data


__all__ = [
    "BaseModel",
    "NamedBaseModel",
]
