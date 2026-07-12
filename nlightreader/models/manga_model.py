import re
from types import NoneType
from typing import override

from PySide6.QtCore import QLocale
import validators

from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.models.base_model import NamedBaseModel
from nlightreader.utils.config import cfg


class Manga(NamedBaseModel):
    def __init__(
        self,
        *,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ) -> None:
        super().__init__(content_id, catalog_id, name, russian)

        self._kind: MangaKind = MangaKind.UNDEFINED
        self._status: MangaStatus = MangaStatus.UNDEFINED
        self._score: int | float = 0
        self._preview_url: str | None = None
        self._volumes_number: int = 0
        self._chapters_number: int = 0
        self._descriptions: dict[Language, str] = {}

    @property
    def kind(self) -> MangaKind:
        return self._kind

    @kind.setter
    def kind(self, kind: MangaKind) -> None:
        if not isinstance(kind, MangaKind):
            msg = f"Kind must be MangaKind got {type(kind)}"
            raise TypeError(msg)
        self._kind = kind

    @property
    def status(self) -> MangaStatus:
        return self._status

    @status.setter
    def status(self, status: MangaStatus) -> None:
        if not isinstance(status, MangaStatus):
            msg = f"Status must be MangaStatus got {type(status)}"
            raise TypeError(msg)
        self._status = status

    @property
    def score(self) -> int | float:
        return self._score

    @score.setter
    def score(self, score: int | float) -> None:
        if not isinstance(score, (int, float)):
            msg = f"Score must be int or float got {type(score)}"
            raise TypeError(msg)

        if isinstance(score, float) and score.is_integer():
            score = int(score)
        self._score = score

    @property
    def preview_url(self) -> str | None:
        return self._preview_url

    @preview_url.setter
    def preview_url(self, url: str | None) -> None:
        if not isinstance(url, (str, NoneType)):
            msg = f"Preview url must be str or None, got{type(url)}"
            raise TypeError(msg)
        if url and not validators.url(url):
            msg = f"Url {url} is not valid"
            raise ValueError(msg)
        if isinstance(url, str) and not url:
            url = None
        self._preview_url = url

    @property
    def volumes_number(self) -> int:
        return self._volumes_number

    @volumes_number.setter
    def volumes_number(self, volumes: int) -> None:
        if not isinstance(volumes, int):
            msg = f"Volumes must be int got {type(volumes)}"
            raise TypeError(msg)
        self._volumes_number = volumes

    @property
    def chapters_number(self) -> int:
        return self._chapters_number

    @chapters_number.setter
    def chapters_number(self, chapters_number: int) -> None:
        if not isinstance(chapters_number, int):
            msg = f"Chapters must be int got {type(chapters_number)}"
            raise TypeError(msg)
        self._chapters_number = chapters_number

    def add_description(self, language: Language, description: str) -> None:
        if not isinstance(language, Language):
            msg = f"Language must be Language got {type(language)}"
            raise TypeError(msg)
        if not isinstance(description, str):
            msg = f"Description must be str got {type(description)}"
            raise TypeError(msg)
        self._descriptions.update({language: description})

    def get_description(self) -> str | None:
        if self._descriptions.get(Language.UNDEFINED):
            return self._descriptions.get(Language.UNDEFINED)

        locale = cfg.get(cfg.language).value.language()
        if locale in (
            QLocale.Language.Russian,
            QLocale.Language.Ukrainian,
        ) and self._descriptions.get(Language.RUSSIAN):
            return self._descriptions.get(Language.RUSSIAN)
        return self._descriptions.get(Language.ENGLISH)

    def descriptions_to_str(self) -> str:
        desc_str = ""
        for key in self._descriptions:
            if self._descriptions.get(key):
                desc_str += (
                    f"<lang={key.name}>{self._descriptions.get(key)}<end>"
                )
        return desc_str

    def set_description_from_str(self, desc: str) -> None:
        for lang_str, text in re.findall(
            r"<lang=(\w+)>(.+?)<end>",
            desc,
            re.DOTALL,
        ):
            lang_enum = Language.from_str(lang_str)
            self.add_description(lang_enum, text)

    @override
    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "kind": self._kind.name,
                "description": self.descriptions_to_str(),
                "score": self._score,
                "status": self._status.name,
                "volumes": self._volumes_number,
                "chapters": self._chapters_number,
                "preview_url": self._preview_url,
            },
        )
        return data


__all__ = ["Manga"]
