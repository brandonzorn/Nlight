from enum import IntEnum, unique

LIB_LISTS: tuple[str, ...] = (
    "planned",
    "completed",
    "reading",
    "re-reading",
    "on hold",
    "dropped",
)


@unique
class LibList(IntEnum):
    PLANNED = 0
    COMPLETED = 1
    READING = 2
    RE_READING = 3
    ON_HOLD = 4
    DROPPED = 5

    @classmethod
    def from_str(cls, string: str) -> "LibList":
        string = string.lower()
        if string == "planned":
            return cls.PLANNED
        if string == "completed":
            return cls.COMPLETED
        if string in ("reading", "watching"):
            return cls.READING
        if string in ("re-reading", "rewatching"):
            return cls.RE_READING
        if string in ("on hold", "on_hold"):
            return cls.ON_HOLD
        if string == "dropped":
            return cls.DROPPED
        msg = f"Unknown lib_list: {string}"
        raise ValueError(msg)

    def to_str(self) -> str:
        return LIB_LISTS[self.value]


__all__ = ["LIB_LISTS", "LibList"]
