from nlightreader.consts.enums import Nl
from nlightreader.parsers.catalog import AbstractCatalog


class AbstractMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = Nl.CatalogType.manga


class AbstractHentaiMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = Nl.CatalogType.hentai_manga


class AbstractRanobeCatalog(AbstractCatalog):
    CATALOG_TYPE = Nl.CatalogType.ranobe


class AbstractAnimeCatalog(AbstractCatalog):
    CATALOG_TYPE = Nl.CatalogType.anime


__all__ = [
    "AbstractMangaCatalog",
    "AbstractAnimeCatalog",
    "AbstractRanobeCatalog",
    "AbstractHentaiMangaCatalog",
]
