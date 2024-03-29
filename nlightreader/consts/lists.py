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


@unique
class LibList(Enum):
    planned = 0
    completed = 1
    reading = 2
    re_reading = 3
    on_hold = 4
    dropped = 5


@unique
class MangaKinds(Enum):
    manga = 0
    manhwa = 1
    manhua = 2
    one_shot = 3
    doujin = 4
    ranobe = 5


@unique
class CatalogType(Enum):
    manga = 0
    hentai_manga = 1
    ranobe = 2
    anime = 3
