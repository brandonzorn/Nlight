from nlightreader.consts.lists import CatalogType
from nlightreader.parsers.Parser import Parser


class MangaCatalog(Parser):
    CATALOG_TYPE = CatalogType.manga

    def __init__(self):
        super().__init__()


class HentaiMangaCatalog(Parser):
    CATALOG_TYPE = CatalogType.hentai_manga

    def __init__(self):
        super().__init__()


class RanobeCatalog(Parser):
    CATALOG_TYPE = CatalogType.ranobe

    def __init__(self):
        super().__init__()
