from enum import Enum, unique

lib_lists_en = ('planned', 'completed', 'watching', 'rewatching', 'on_hold', 'dropped')


@unique
class LibList(Enum):
    planned = 0
    completed = 1
    watching = 2
    rewatching = 3
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
