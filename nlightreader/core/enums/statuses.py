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

    @classmethod
    def from_str(cls, string: str | None) -> IntEnum:
        def matching_the_pattern(text: str, pattern: tuple) -> bool:
            text = text.lower()
            return any([i in text for i in pattern])

        if string is None or string in ("undefined", "Другое"):
            return cls.UNDEFINED
        if matching_the_pattern(string, ("manga", "манга")):
            return cls.MANGA
        if matching_the_pattern(string, ("manhwa", "манхва")):
            return cls.MANHWA
        if matching_the_pattern(string, ("manhua", "маньхуа")):
            return cls.MANHUA
        if matching_the_pattern(string, ("one_shot",)):
            return cls.ONE_SHOT
        if matching_the_pattern(string, ("doujin",)):
            return cls.DOUJIN
        if matching_the_pattern(string, ("ranobe", "novel")):
            return cls.RANOBE
        if matching_the_pattern(string, ("комикс", "comic")):
            return cls.COMICS
        logging.warning(f"Unknown manga kind: {string}")
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
    def from_str(cls, string: str | None) -> IntEnum:
        if string is None or string.lower() in ("undefined", "неизвестно"):
            return cls.UNDEFINED

        string = string.lower()
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
