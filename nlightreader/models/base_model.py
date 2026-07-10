from typing import override

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)
from PySide6.QtCore import QLocale

from nlightreader.utils.config import cfg


class ContentModel(BaseModel):
    model_config = ConfigDict(
        coerce_numbers_to_str=True,
        validate_assignment=True,
    )

    id: str = Field(default="", init=False)
    content_id: str = Field(frozen=True, min_length=1)
    catalog_id: int = Field(frozen=True, ge=0)

    @model_validator(mode="after")
    def generate_id(self) -> "ContentModel":
        if not self.id:
            self.id = f"|{self.catalog_id}|_|{self.content_id}|"
        return self

    def __eq__(self, other: "ContentModel") -> bool:
        if not isinstance(other, ContentModel):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def to_dict(self) -> dict:
        return self.model_dump()


class NamedContentModel(ContentModel):
    name: str
    russian: str | None

    @field_validator("russian", mode="before")
    @classmethod
    def blank_to_none(cls, value: str | None) -> str | None:
        if isinstance(value, str) and not value.strip():
            return None
        return value

    def get_name(self) -> str:
        locale = cfg.get(cfg.language).value.language()
        if (
            locale
            in (
                QLocale.Language.Russian,
                QLocale.Language.Ukrainian,
            )
            and self.russian
        ):
            return self.russian
        return self.name

    @override
    def to_dict(self) -> dict:
        return self.model_dump()


__all__ = [
    "ContentModel",
    "NamedContentModel",
]
