from enum import IntEnum, unique
import logging
from typing import Self

logger = logging.getLogger(__name__)


@unique
class Language(IntEnum):
    undefined = 0
    en = 1
    ru = 2
    uk = 3
    jp = 4

    @classmethod
    def from_str(cls, string: str) -> Self:
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
        logger.warning(f"Unknown language {string}")
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


__all__ = ["Language"]
