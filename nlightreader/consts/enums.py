import logging
from enum import Enum, unique

lib_lists_en = (
    "planned",
    "completed",
    "reading",
    "re-reading",
    "on hold",
    "dropped",
)


def parse_lib_list(lib_list: str):
    if lib_list == "watching":
        return "reading"
    if lib_list == "rewatching":
        return "re-reading"
    return lib_list


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
            if string in ("manga", "Манга"):
                return cls.manga
            if string in ("manhwa", "Манхва"):
                return cls.manhwa
            if string in ("manhua", "Маньхуа"):
                return cls.manhua
            if string in ("one_shot",):
                return cls.one_shot
            if string in ("doujin",):
                return cls.doujin
            if string in ("ranobe", "light_novel"):
                return cls.ranobe
            if string in ("comics", "Рукомикс", "Западный комикс", "Индонезийский комикс"):
                return cls.comics
            if string is None or string in ("undefined", "Другое"):
                return cls.undefined
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
