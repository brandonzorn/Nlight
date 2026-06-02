import logging

from nlightreader.parsers import (
    AllHentai,
    Desu,
    Erolate,
    LibAnilib,
    LibMangalib,
    LibRanobelib,
    MangaDex,
    MangaDexLib,
    NHentai,
    Ranobehub,
    Remanga,
    Rulate,
    ShikimoriAnime,
    ShikimoriBase,
    ShikimoriLib,
    ShikimoriManga,
    ShikimoriRanobe,
    SlashLib,
)
from nlightreader.parsers.catalog import AbstractCatalog

CATALOG_CLASSES = {
    0: Desu,
    1: ShikimoriBase,
    2: MangaDex,
    3: Rulate,
    4: Ranobehub,
    5: Erolate,
    6: Remanga,
    7: NHentai,
    8: AllHentai,
    9: SlashLib,
    10: LibMangalib,
    11: ShikimoriAnime,
    # 12:
    13: LibRanobelib,
    14: LibAnilib,
}
USER_CATALOGS = [
    Desu,
    MangaDex,
    Remanga,
    ShikimoriManga,
    ShikimoriRanobe,
    ShikimoriAnime,
    LibMangalib,
    LibRanobelib,
    LibAnilib,
    Rulate,
    Erolate,
    Ranobehub,
    NHentai,
    AllHentai,
]
LIB_CATALOGS = {ShikimoriBase: ShikimoriLib, MangaDex: MangaDexLib}


_initialized_catalogs = {}


def get_catalog_by_id(catalog_id: int):
    if catalog_id in _initialized_catalogs:
        return _initialized_catalogs[catalog_id]
    if catalog_id in CATALOG_CLASSES:
        instance = CATALOG_CLASSES[catalog_id]()
        _initialized_catalogs[catalog_id] = instance
        return instance
    logging.warning(f"Catalog with id {catalog_id} not found.")
    return AbstractCatalog()


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)()


__all__ = [
    "get_catalog_by_id",
    "get_lib_catalog",
    "USER_CATALOGS",
]
