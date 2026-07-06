from nlightreader.core.enums import CatalogType
from nlightreader.parsers.catalog import AbstractCatalog


class AbstractMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.MANGA


class AbstractHentaiMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.HENTAI_MANGA


class AbstractRanobeCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.RANOBE


class AbstractAnimeCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.ANIME


__all__ = [
    "AbstractMangaCatalog",
    "AbstractAnimeCatalog",
    "AbstractRanobeCatalog",
    "AbstractHentaiMangaCatalog",
]
