from types import NoneType

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
    ):
        super().__init__(content_id, catalog_id)
        self.__volume_number = volume_number
        self.__chapter_number = chapter_number
        self.__title = title
        self.__language = language
        self.__translator: str | None = None

    @property
    def volume_number(self):
        return self.__volume_number

    @property
    def chapter_number(self):
        return self.__chapter_number

    @property
    def language(self):
        return self.__language

    @property
    def translator(self):
        return self.__translator

    @translator.setter
    def translator(self, translator: str):
        if not isinstance(translator, (str, NoneType)):
            raise TypeError(
                f"Translator must be a string or None got {type(translator)}",
            )
        self.__translator = translator

    def get_name(self) -> str:
        if not self.__volume_number and not self.__chapter_number:
            return self.__title

        vol_ch_name = f"{self.__volume_number}-{self.__chapter_number}"
        if self.__title:
            return f"{vol_ch_name} {self.__title}"
        return vol_ch_name

    def to_dict(self):
        return {
            "id": self.id,
            "content_id": self.content_id,
            "catalog_id": self.catalog_id,
            "vol": self.__volume_number,
            "ch": self.__chapter_number,
            "title": self.__title,
            "language": self.language.name,
        }
