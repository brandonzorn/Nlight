from enum import IntEnum, unique


@unique
class CatalogType(IntEnum):
    UNDEFINED = 0
    MANGA = 1
    HENTAI_MANGA = 2
    RANOBE = 3
    ANIME = 4


__all__ = ["CatalogType"]
