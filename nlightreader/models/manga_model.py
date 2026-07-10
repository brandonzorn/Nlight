import re
from typing import override

from pydantic import Field, field_serializer, field_validator
from PySide6.QtCore import QLocale
import validators

from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.models.base_model import NamedContentModel
from nlightreader.utils.config import cfg


class Manga(NamedContentModel):
    kind: MangaKind = MangaKind.UNDEFINED
    status: MangaStatus = MangaStatus.UNDEFINED
    score: int | float = 0
    volumes_number: int = 0
    chapters_number: int = 0

    descriptions: dict[Language, str] = Field(default_factory=dict)
    preview_url: str | None = None

    @field_validator("preview_url", mode="before")
    @classmethod
    def validate_preview_url(cls, value: str | None) -> str | None:
        if isinstance(value, str) and not value.strip():
            return None

        if value is not None:
            if not isinstance(value, str):
                msg = f"Preview url must be str or None, got {type(value).__name__}"
                raise TypeError(msg)
            if not validators.url(value):
                msg = f"Url {value} is not valid"
                raise ValueError(msg)

        return value

    def add_description(self, language: Language, description: str) -> None:
        if not isinstance(description, str):
            msg = f"Description must be str got {type(description).__name__}"
            raise TypeError(msg)
        self.descriptions[language] = description

    def get_description(self) -> str | None:
        if self.descriptions.get(Language.UNDEFINED):
            return self.descriptions.get(Language.UNDEFINED)

        locale = cfg.get(cfg.language).value.language()
        if locale in (
            QLocale.Language.Russian,
            QLocale.Language.Ukrainian,
        ) and self.descriptions.get(Language.RUSSIAN):
            return self.descriptions.get(Language.RUSSIAN)
        return self.descriptions.get(Language.ENGLISH)

    @field_serializer("descriptions")
    def serialize_descriptions(self, descriptions: dict[Language, str]) -> str:
        desc_str = ""
        for key, value in descriptions.items():
            if not value:
                continue
            desc_str += f"<lang={key.name}>{value}<end>"
        return desc_str

    def set_description_from_str(self, descriptions: str) -> None:
        lang_regex = r"<lang=(\w+)>(.+?)<end>"
        for lang_str, text in re.findall(
            lang_regex,
            descriptions,
            re.DOTALL,
        ):
            lang_enum = Language.from_str(lang_str)
            self.add_description(lang_enum, text)

    @override
    def to_dict(self) -> dict:
        return self.model_dump()


__all__ = ["Manga"]
