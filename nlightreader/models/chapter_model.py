from types import NoneType
from typing import override

from nlightreader.core.enums import Language
from nlightreader.models.base_model import BaseModel


class Chapter(BaseModel):
    def __init__(
        self,
        *,
        content_id: str,
        catalog_id: int,
        volume_number: str | None,
        chapter_number: str | None,
        title: str,
        language: Language = Language.UNDEFINED,
        translator: str | None = None,
    ) -> None:
        super().__init__(content_id, catalog_id)
        self._volume_number = volume_number
        self._chapter_number = chapter_number
        self._title = title
        self._language = language
        self._translator = translator

    @property
    def volume_number(self) -> str | None:
        return self._volume_number

    @property
    def chapter_number(self) -> str | None:
        return self._chapter_number

    @property
    def title(self) -> str:
        return self._title

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

    def get_name(self) -> str:
        if not self._volume_number and not self._chapter_number:
            return self._title

        vol_ch_name = f"{self._volume_number}-{self._chapter_number}"
        if self._title:
            return f"{vol_ch_name} {self._title}"
        return vol_ch_name

    @override
    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "vol": self._volume_number,
                "ch": self._chapter_number,
                "title": self._title,
                "language": self._language.name,
                "translator": self._translator,
            },
        )
        return data


__all__ = ["Chapter"]
