from nlightreader.parsers import Desu, ShikimoriBase, MangaDex, Rulate, Ranobehub, MangaDexLib, ShikimoriRanobe, \
    ShikimoriManga, ShikimoriLib, Erolate, Remanga, NHentai, AllHentai, SlashLib, MangaLib

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
}
USER_CATALOGS = [
    Desu,
    ShikimoriManga,
    ShikimoriRanobe,
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


def get_catalog(catalog_id=0):
    return CATALOGS.get(catalog_id)


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)
