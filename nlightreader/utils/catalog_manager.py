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

CATALOGS = {
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


def get_catalog_by_id(catalog_id):
    if catalog_id not in CATALOGS:
        logging.warning(f"Catalog with id {catalog_id} not found.")
        return AbstractCatalog()
    return CATALOGS[catalog_id]()


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)()
