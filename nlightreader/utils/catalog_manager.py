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
    SlashLibLegacy,
)
from nlightreader.parsers.catalog import AbstractCatalog, LibParser

logger = logging.getLogger(__name__)

CATALOG_CLASSES: dict[int, type[AbstractCatalog]] = {
    0: Desu,
    1: ShikimoriBase,
    2: MangaDex,
    3: Rulate,
    4: Ranobehub,
    5: Erolate,
    6: Remanga,
    7: NHentai,
    8: AllHentai,
    9: SlashLibLegacy,
    10: LibMangalib,
    11: ShikimoriAnime,
    # 12:
    13: LibRanobelib,
    14: LibAnilib,
}
USER_CATALOGS: list[type[AbstractCatalog]] = [
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
LIB_CATALOGS: dict[type[AbstractCatalog], type[LibParser]] = {
    ShikimoriBase: ShikimoriLib,
    MangaDex: MangaDexLib,
}


_initialized_catalogs: dict[int, AbstractCatalog] = {}


def get_catalog_by_id(catalog_id: int) -> AbstractCatalog:
    if catalog_id in _initialized_catalogs:
        return _initialized_catalogs[catalog_id]
    if catalog_id in CATALOG_CLASSES:
        instance = CATALOG_CLASSES[catalog_id]()
        _initialized_catalogs[catalog_id] = instance
        return instance
    logger.warning(f"Catalog with id {catalog_id} not found.")
    return AbstractCatalog()


def get_lib_catalog(base_catalog: type[AbstractCatalog]) -> LibParser:
    if base_catalog in LIB_CATALOGS:
        return LIB_CATALOGS[base_catalog]()
    logger.warning(f"Catalog with id {base_catalog.CATALOG_ID} not found.")
    return LibParser()


__all__ = [
    "USER_CATALOGS",
    "get_catalog_by_id",
    "get_lib_catalog",
]
