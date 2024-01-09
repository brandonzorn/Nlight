from nlightreader.consts import Nl
from nlightreader.parsers.Parser import Parser


class MangaCatalog(Parser):
    CATALOG_TYPE = Nl.CatalogType.manga

    def __init__(self):
        super().__init__()


class HentaiMangaCatalog(Parser):
    CATALOG_TYPE = Nl.CatalogType.hentai_manga

    def __init__(self):
        super().__init__()


class RanobeCatalog(Parser):
    CATALOG_TYPE = Nl.CatalogType.ranobe

    def __init__(self):
        super().__init__()
