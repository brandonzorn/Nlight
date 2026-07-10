from enum import IntEnum, unique
import logging

logger = logging.getLogger(__name__)


@unique
class MangaKind(IntEnum):
    UNDEFINED = 0
    MANGA = 1
    MANHWA = 2
    MANHUA = 3
    ONE_SHOT = 4
    DOUJIN = 5
    RANOBE = 6
    COMICS = 7

    @staticmethod
    def _matching_the_pattern(text: str, pattern: tuple) -> bool:
        text = text.lower()
        return any([i in text for i in pattern])

    @classmethod
    def from_str(cls, string: str | None) -> "MangaKind":
        if string is None or cls._matching_the_pattern(
            string,
            ("undefined", "Другое"),
        ):
            return cls.UNDEFINED
        if cls._matching_the_pattern(string, ("manga", "манга")):
            return cls.MANGA
        if cls._matching_the_pattern(string, ("manhwa", "манхва")):
            return cls.MANHWA
        if cls._matching_the_pattern(string, ("manhua", "маньхуа")):
            return cls.MANHUA
        if cls._matching_the_pattern(string, ("one_shot",)):
            return cls.ONE_SHOT
        if cls._matching_the_pattern(string, ("doujin",)):
            return cls.DOUJIN
        if cls._matching_the_pattern(string, ("ranobe", "novel")):
            return cls.RANOBE
        if cls._matching_the_pattern(string, ("комикс", "comic")):
            return cls.COMICS
        logger.warning(f"Unknown manga kind: {string}")
        return cls.UNDEFINED

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
    UNDEFINED = 0
    ONGOING = 1
    RELEASED = 2
    FROZEN = 3

    @classmethod
    def from_str(cls, string: str | None) -> "MangaStatus":
        if string is None:
            return cls.UNDEFINED

        string = string.lower()
        if string in ("undefined", "неизвестно"):
            return cls.UNDEFINED
        if string in ("ongoing", "в процессе"):
            return cls.ONGOING
        if string in ("released", "completed", "завершено"):
            return cls.RELEASED
        if string in ("frozen", "заморожено"):
            return cls.FROZEN
        logger.warning(f"Unknown manga status: {string}")
        return cls.UNDEFINED

    def to_str(self) -> str:
        names = [
            "Undefined",
            "Ongoing",
            "Released",
            "Frozen",
        ]
        return names[self.value]


__all__ = ["MangaKind", "MangaStatus"]
