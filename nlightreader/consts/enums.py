import logging
from enum import Enum, unique

LIB_LISTS = ("planned", "completed", "reading", "re-reading", "on hold", "dropped")


class Nl:
    @unique
    class Language(Enum):
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

        def to_full_str(self):
            names = ["Undefined", "English", "Russian", "Ukrainian", "Japanese"]
            return names[self.value]

    @unique
    class CatalogType(Enum):
        manga = 0
        hentai_manga = 1
        ranobe = 2
        anime = 3

    @unique
    class MangaKind(Enum):
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
            if matching_the_pattern(string, ("комикс", "comics")):
                return cls.comics
            logging.warning(f"Unknown manga kind: {string}")
            return cls.undefined

        def to_full_str(self):
            names = ["Undefined", "Manga", "Manhwa", "Manhua", "One shot", "Doujin", "Light Novel", "Comics"]
            return names[self.value]

    @unique
    class LibList(Enum):
        planned = 0
        completed = 1
        reading = 2
        re_reading = 3
        on_hold = 4
        dropped = 5

        @classmethod
        def from_str(cls, string: str | None):
            string = string.lower()
            if string in ("planned",):
                return cls.planned
            if string in ("completed",):
                return cls.completed
            if string in ("reading", "watching",):
                return cls.reading
            if string in ("re-reading", "rewatching"):
                return cls.re_reading
            if string in ("on hold",):
                return cls.on_hold
            if string in ("dropped",):
                return cls.dropped
            raise ValueError(f"Unknown lib_list: {string}")

        def to_str(self):
            return LIB_LISTS[self.value]
