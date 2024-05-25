from nlightreader.consts.items import MangaLibItems
from nlightreader.consts.urls import URL_MANGALIB
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase


class LibMangalib(LibBase, AbstractMangaCatalog):
    CATALOG_NAME = "MangaLib"
    CATALOG_ID = 14

    def __init__(self):
        super().__init__()
        self.url = URL_MANGALIB
        self.items = MangaLibItems

        self.content_name = "manga"
        self.site_id = 1
