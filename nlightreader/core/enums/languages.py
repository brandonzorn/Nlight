from enum import IntEnum, unique
import logging

logger = logging.getLogger(__name__)


@unique
class Language(IntEnum):
    UNDEFINED = 0
    ENGLISH = 1
    RUSSIAN = 2
    UKRAINIAN = 3
    JAPANESE = 4

    @classmethod
    def from_str(cls, string: str) -> "Language":
        string = string.lower()
        if string in ("en", "english"):
            return cls.ENGLISH
        if string in ("ru", "russian"):
            return cls.RUSSIAN
        if string in ("uk", "ukrainian"):
            return cls.UKRAINIAN
        if string in ("jp", "japanese"):
            return cls.JAPANESE
        if string in ("undefined",):
            return cls.UNDEFINED
        logger.warning(f"Unknown language {string}")
        return cls.UNDEFINED

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
