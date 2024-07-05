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


def get_catalog(catalog_id=0):
    return CATALOGS.get(catalog_id)


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)
