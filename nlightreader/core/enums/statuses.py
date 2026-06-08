from enum import IntEnum, unique
import logging
from typing import Self

logger = logging.getLogger(__name__)


@unique
class MangaKind(IntEnum):
    undefined = 0
    manga = 1
    manhwa = 2
    manhua = 3
    one_shot = 4
    doujin = 5
    ranobe = 6
    comics = 7

    @classmethod
    def from_str(cls, string: str | None) -> Self:
        def matching_the_pattern(text: str, pattern: tuple) -> bool:
            text = text.lower()
            return any([i in text for i in pattern])

        if string is None or string in ("undefined", "Другое"):
            return cls.undefined
        if matching_the_pattern(string, ("manga", "манга")):
            return cls.manga
        if matching_the_pattern(string, ("manhwa", "манхва")):
            return cls.manhwa
        if matching_the_pattern(string, ("manhua", "маньхуа")):
            return cls.manhua
        if matching_the_pattern(string, ("one_shot",)):
            return cls.one_shot
        if matching_the_pattern(string, ("doujin",)):
            return cls.doujin
        if matching_the_pattern(string, ("ranobe", "novel")):
            return cls.ranobe
        if matching_the_pattern(string, ("комикс", "comic")):
            return cls.comics
        logging.warning(f"Unknown manga kind: {string}")
        return cls.undefined

    def to_str(self) -> str:
        names = [
            "Undefined",
            "Manga",
            "Manhwa",
            "Manhua",
            "Oneshot",
            "Doujin",
            "Ranobe",
            "Comics",
        ]
        return names[self.value]


@unique
class MangaStatus(IntEnum):
    undefined = 0
    ongoing = 1
    released = 2
    frozen = 3

    @classmethod
    def from_str(cls, string: str | None) -> Self:
        if string is None or string.lower() in ("undefined", "неизвестно"):
            return cls.undefined

        string = string.lower()
        if string in ("ongoing", "в процессе"):
            return cls.ongoing
        if string in ("released", "completed", "завершено"):
            return cls.released
        if string in ("frozen", "заморожено"):
            return cls.frozen
        logger.warning(f"Unknown manga status: {string}")
        return cls.undefined

    def to_str(self) -> str:
        names = [
            "Undefined",
            "Ongoing",
            "Released",
            "Frozen",
        ]
        return names[self.value]


__all__ = ["MangaKind", "MangaStatus"]
