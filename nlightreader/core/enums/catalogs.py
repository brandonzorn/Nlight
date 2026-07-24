from enum import IntEnum, unique


@unique
class CatalogType(IntEnum):
    MANGA = 0
    HENTAI_MANGA = 1
    RANOBE = 2
    ANIME = 3


__all__ = ["CatalogType"]
