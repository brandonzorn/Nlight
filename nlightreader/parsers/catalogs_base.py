from nlightreader.core.enums import CatalogType
from nlightreader.parsers.catalog import AbstractCatalog


class AbstractMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.manga


class AbstractHentaiMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.hentai_manga


class AbstractRanobeCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.ranobe


class AbstractAnimeCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.anime


__all__ = [
    "AbstractMangaCatalog",
    "AbstractAnimeCatalog",
    "AbstractRanobeCatalog",
    "AbstractHentaiMangaCatalog",
]
