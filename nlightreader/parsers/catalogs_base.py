from nlightreader.core.enums import CatalogType
from nlightreader.models import Episode, Manga
from nlightreader.parsers.catalog import AbstractCatalog


class AbstractMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.MANGA


class AbstractHentaiMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.HENTAI_MANGA


class AbstractRanobeCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.RANOBE


class AbstractAnimeCatalog(AbstractCatalog):
    CATALOG_TYPE = CatalogType.ANIME

    def get_episodes(self, anime: Manga) -> list[Episode]:
        raise NotImplementedError


__all__ = [
    "AbstractAnimeCatalog",
    "AbstractHentaiMangaCatalog",
    "AbstractMangaCatalog",
    "AbstractRanobeCatalog",
]
