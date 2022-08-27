from enum import Enum, unique

lib_lists_en = ('planned', 'completed', 'watching', 'rewatching', 'on_hold', 'dropped')
lib_lists_ru = ('запланированно', 'прочитано', 'читаю', 'перечитываю', 'отложено', 'брошено')


@unique
class LibList(Enum):
    planned = 0
    completed = 1
    watching = 2
    rewatching = 3
    on_hold = 4
    dropped = 5
