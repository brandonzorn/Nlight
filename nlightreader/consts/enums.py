import logging
from enum import IntEnum, unique

LIB_LISTS = (
    "planned",
    "completed",
    "reading",
    "re-reading",
    "on hold",
    "dropped",
)


class Nl:
    @unique
    class Language(IntEnum):
        undefined = 0
        en = 1
        ru = 2
        uk = 3
        jp = 4

        @classmethod
        def from_str(cls, string: str):
            if string in ("en", "eng"):
                return cls.en
            if string in ("ru", "rus"):
                return cls.ru
            if string in ("uk", "ukr"):
                return cls.uk
            if string in ("jp", "jap"):
                return cls.jp
            if string in ("undefined",):
                return cls.undefined
            logging.warning(f"Unknown language {string}")
            return cls.undefined

        def to_str(self) -> str:
            names = [
                "Undefined",
                "English",
                "Russian",
                "Ukrainian",
                "Japanese",
            ]
            return names[self.value]

    @unique
    class CatalogType(IntEnum):
        manga = 0
        hentai_manga = 1
        ranobe = 2
        anime = 3

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
        def from_str(cls, string: str | None):
            def matching_the_pattern(text, pattern):
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
    class LibList(IntEnum):
        planned = 0
        completed = 1
        reading = 2
        re_reading = 3
        on_hold = 4
        dropped = 5

        @classmethod
        def from_str(cls, string: str):
            string = string.lower()
            if string in ("planned",):
                return cls.planned
            if string in ("completed",):
                return cls.completed
            if string in ("reading", "watching"):
                return cls.reading
            if string in ("re-reading", "rewatching"):
                return cls.re_reading
            if string in ("on hold", "on_hold"):
                return cls.on_hold
            if string in ("dropped",):
                return cls.dropped
            raise ValueError(f"Unknown lib_list: {string}")

        def to_str(self) -> str:
            return LIB_LISTS[self.value]

    @unique
    class MangaStatus(IntEnum):
        undefined = 0
        ongoing = 1
        released = 2
        frozen = 3

        @classmethod
        def from_str(cls, string: str | None):
            if string is None or string.lower() in ("undefined", "неизвестно"):
                return cls.undefined

            string = string.lower()
            if string in ("ongoing", "в процессе"):
                return cls.ongoing
            if string in ("released", "completed", "завершено"):
                return cls.released
            if string in ("frozen", "заморожено"):
                return cls.frozen
            logging.warning(f"Unknown manga status: {string}")
            return cls.undefined

        def to_str(self) -> str:
            names = [
                "Undefined",
                "Ongoing",
                "Released",
                "Frozen",
            ]
            return names[self.value]


__all__ = [
    "LIB_LISTS",
    "Nl",
]
