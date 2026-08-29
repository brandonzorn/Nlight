from types import NoneType
from typing import override

from nlightreader.core.enums import Language
from nlightreader.models.base_model import BaseModel


class Episode(BaseModel):
    def __init__(
        self,
        *,
        content_id: str,
        catalog_id: int,
        season_number: int,
        episode_number: int,
        title: str,
        url: str | None,
        language: Language = Language.UNDEFINED,
        translator: str | None = None,
    ) -> None:
        super().__init__(content_id, catalog_id)
        self._season_number = season_number
        self._episode_number = episode_number
        self._title = title
        self._language = language
        self._translator = translator

        self._url = url

    @property
    def url(self) -> str | None:
        return self._url

    @property
    def season_number(self) -> int:
        return self._season_number

    @property
    def episode_number(self) -> int:
        return self._episode_number

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
        if not self._season_number and not self._episode_number:
            return self._title

        num_name = f"{self._season_number}-{self._episode_number}"
        if self._title:
            return f"{num_name} {self._title}"
        return num_name

    @override
    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "season_number": self._season_number,
                "episode_number": self._episode_number,
                "title": self._title,
                "language": self._language.name,
                "translator": self._translator,
            },
        )
        return data


__all__ = ["Episode"]
