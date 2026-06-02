from types import NoneType
from typing import override

from nlightreader.consts.enums import Nl
from nlightreader.models.base_model import BaseModel


class Chapter(BaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        volume_number: str | None,
        chapter_number: str | None,
        title: str,
        language: Nl.Language = Nl.Language.undefined,
        translator: str | None = None,
    ) -> None:
        super().__init__(content_id, catalog_id)
        self.__volume_number = volume_number
        self.__chapter_number = chapter_number
        self.__title = title
        self.__language = language
        self.__translator: str | None = None

    @property
    def volume_number(self) -> str | None:
        return self.__volume_number

    @property
    def chapter_number(self) -> str | None:
        return self.__chapter_number

    @property
    def language(self) -> Nl.Language:
        return self.__language

    @property
    def translator(self) -> str | None:
        return self.__translator

    @translator.setter
    def translator(self, translator: str | None) -> None:
        if not isinstance(translator, (str, NoneType)):
            msg = (
                f"Translator must be a string or None, got {type(translator)}"
            )
            raise TypeError(msg)
        self.__translator = translator

    def get_name(self) -> str:
        if not self.__volume_number and not self.__chapter_number:
            return self.__title

        vol_ch_name = f"{self.__volume_number}-{self.__chapter_number}"
        if self.__title:
            return f"{vol_ch_name} {self.__title}"
        return vol_ch_name

    @override
    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "vol": self.__volume_number,
                "ch": self.__chapter_number,
                "title": self.__title,
                "language": self.__language.name,
            },
        )
        return data


__all__ = ["Chapter"]
