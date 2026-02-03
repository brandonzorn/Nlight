import re
from types import NoneType
from typing import override

from PySide6.QtCore import QLocale
import validators

from nlightreader.consts.enums import Nl
from nlightreader.models.base_model import NamedBaseModel
from nlightreader.utils.config import cfg


class Manga(NamedBaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ) -> None:
        super().__init__(content_id, catalog_id, name, russian)

        self.__kind: Nl.MangaKind = Nl.MangaKind.undefined
        self.__status: Nl.MangaStatus = Nl.MangaStatus.undefined
        self.__score: int | float = 0
        self.__preview_url: str | None = None

        self.__volumes = 0
        self.__chapters = 0

        self.__descriptions: dict[Nl.Language, str] = {}

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind) -> None:
        if not isinstance(kind, Nl.MangaKind):
            msg = f"Kind must be Nl.MangaKind got {type(kind)}"
            raise TypeError(msg)
        self.__kind = kind

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: Nl.MangaStatus) -> None:
        if not isinstance(status, Nl.MangaStatus):
            msg = f"Status must be Nl.MangaStatus got {type(status)}"
            raise TypeError(msg)
        self.__status = status

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score: int | float) -> None:
        if not isinstance(score, (int, float)):
            msg = f"Score must be int or float got {type(score)}"
            raise TypeError(msg)

        if isinstance(score, float) and score.is_integer():
            score = int(score)
        self.__score = score

    @property
    def preview_url(self):
        return self.__preview_url

    @preview_url.setter
    def preview_url(self, url: str | None) -> None:
        if not isinstance(url, (str, NoneType)):
            msg = f"Preview url must be str or None got {type(url)}"
            raise TypeError(msg)
        if url is not None and not validators.url(url):
            msg = f"Url {url} is not valid"
            raise ValueError(msg)
        self.__preview_url = url

    @property
    def volumes(self):
        return self.__volumes

    @volumes.setter
    def volumes(self, volumes: int) -> None:
        if not isinstance(volumes, int):
            msg = f"Volumes must be int got {type(volumes)}"
            raise TypeError(msg)
        self.__volumes = volumes

    @property
    def chapters(self):
        return self.__chapters

    @chapters.setter
    def chapters(self, chapters: int) -> None:
        if not isinstance(chapters, int):
            msg = f"Chapters must be int got {type(chapters)}"
            raise TypeError(msg)
        self.__chapters = chapters

    def add_description(self, language: Nl.Language, description: str) -> None:
        if not isinstance(language, Nl.Language):
            msg = f"Language must be Nl.Language got {type(language)}"
            raise TypeError(msg)
        if not isinstance(description, str):
            msg = f"Description must be str got {type(description)}"
            raise TypeError(msg)
        self.__descriptions.update({language: description})

    def get_description(self) -> str:
        if self.__descriptions.get(Nl.Language.undefined):
            return self.__descriptions.get(Nl.Language.undefined)

        locale = cfg.get(cfg.language).value.language()
        if locale in (
            QLocale.Language.Russian,
            QLocale.Language.Ukrainian,
        ) and self.__descriptions.get(Nl.Language.ru):
            return self.__descriptions.get(Nl.Language.ru)
        return self.__descriptions.get(Nl.Language.en)

    def descriptions_to_str(self) -> str:
        desc_str = ""
        for key in self.__descriptions:
            if self.__descriptions.get(key):
                desc_str += (
                    f"<lang={key.name}>{self.__descriptions.get(key)}<end>"
                )
        return desc_str

    def set_description_from_str(self, desc: str) -> None:
        for lang, text in re.findall(
            r"<lang=(\w+)>(.+?)<end>",
            desc,
            re.DOTALL,
        ):
            self.add_description(
                Nl.Language.from_str(lang),
                text,
            )

    @override
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "content_id": self.content_id,
            "catalog_id": self.catalog_id,
            "name": self.name,
            "russian": self.russian,
            "kind": self.kind.name,
            "description": self.descriptions_to_str(),
            "score": self.score,
            "status": self.__status.name,
            "volumes": self.__volumes,
            "chapters": self.__chapters,
            "preview_url": self.__preview_url,
        }


__all__ = [
    "Manga",
]
