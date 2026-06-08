from enum import IntEnum, unique
from typing import Self

LIB_LISTS = (
    "planned",
    "completed",
    "reading",
    "re-reading",
    "on hold",
    "dropped",
)


@unique
class LibList(IntEnum):
    planned = 0
    completed = 1
    reading = 2
    re_reading = 3
    on_hold = 4
    dropped = 5

    @classmethod
    def from_str(cls, string: str) -> Self:
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
        msg = f"Unknown lib_list: {string}"
        raise ValueError(msg)

    def to_str(self) -> str:
        return LIB_LISTS[self.value]


__all__ = ["LIB_LISTS", "LibList"]
