from nlightreader.consts.enums import Nl
from nlightreader.parsers.catalog import AbstractCatalog


class AbstractMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = Nl.CatalogType.manga

    def __init__(self):
        super().__init__()


class AbstractHentaiMangaCatalog(AbstractCatalog):
    CATALOG_TYPE = Nl.CatalogType.hentai_manga

    def __init__(self):
        super().__init__()


class AbstractRanobeCatalog(AbstractCatalog):
    CATALOG_TYPE = Nl.CatalogType.ranobe

    def __init__(self):
        super().__init__()
