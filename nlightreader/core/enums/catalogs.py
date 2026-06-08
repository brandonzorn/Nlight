from enum import IntEnum, unique


@unique
class CatalogType(IntEnum):
    manga = 0
    hentai_manga = 1
    ranobe = 2
    anime = 3


__all__ = ["CatalogType"]
