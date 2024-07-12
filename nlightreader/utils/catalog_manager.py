import logging

from nlightreader.parsers import Desu, ShikimoriBase, MangaDex, Rulate, Ranobehub, MangaDexLib, ShikimoriRanobe, \
    ShikimoriManga, ShikimoriLib, Erolate, Remanga, NHentai, AllHentai, SlashLib, MangaLib, ShikimoriAnime
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
    10: MangaLib,
    11: ShikimoriAnime,
}
USER_CATALOGS = [
    Desu,
    ShikimoriManga,
    ShikimoriRanobe,
    ShikimoriAnime,
    MangaDex,
    MangaLib,
    Remanga,
    Rulate,
    Erolate,
    Ranobehub,
    SlashLib,
    NHentai,
    AllHentai,
]
LIB_CATALOGS = {ShikimoriBase: ShikimoriLib, MangaDex: MangaDexLib}


def get_catalog(catalog_id):
    if catalog_id not in CATALOGS:
        logging.warning(f"Catalog with id {catalog_id} not found.")
        return AbstractCatalog
    return CATALOGS.get(catalog_id)


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)
