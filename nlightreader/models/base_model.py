from types import NoneType
from typing import Any, override

from PySide6.QtCore import QLocale

from core.enums import Language
from utils.config import cfg


def is_cyrillic_locale() -> bool:
    locale = cfg.get(cfg.language).value.language()
    return locale in (
        QLocale.Language.Belarusian,
        QLocale.Language.Russian,
        QLocale.Language.Ukrainian,
    )


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
        return hash((type(self), self._id))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self._id!r})"

    @property
    def id(self) -> str:
        return self._id

    @property
    def content_id(self) -> str:
        return self._content_id

    @property
    def catalog_id(self) -> int:
        return self._catalog_id

    def to_dict(self) -> dict[str, Any]:
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
        if self._russian and is_cyrillic_locale():
            return self._russian
        return self._name

    @override
    def to_dict(self) -> dict[str, Any]:
        data = super().to_dict()
        data.update(
            {
                "name": self._name,
                "russian": self._russian,
            },
        )
        return data


class TranslatedContentModel(BaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        title: str | None,
        language: Language = Language.UNDEFINED,
        translator: str | None = None,
    ) -> None:
        super().__init__(content_id, catalog_id)
        self._title = title
        self._language = language
        self._translator: str | None = None
        self.translator = translator

    @property
    def title(self) -> str:
        return self._title or ""

    @property
    def language(self) -> Language:
        return self._language

    @property
    def translator(self) -> str | None:
        return self._translator

    @translator.setter
    def translator(self, translator: str | None) -> None:
        if not isinstance(translator, (str, NoneType)):
            msg = (
                f"Translator must be a string or None, got {type(translator)}"
            )
            raise TypeError(msg)
        self._translator = translator

    @override
    def to_dict(self) -> dict[str, Any]:
        data = super().to_dict()
        data.update(
            {
                "title": self._title,
                "language": self._language.name,
                "translator": self._translator,
            },
        )
        return data


__all__ = [
    "BaseModel",
    "NamedBaseModel",
    "TranslatedContentModel",
]
