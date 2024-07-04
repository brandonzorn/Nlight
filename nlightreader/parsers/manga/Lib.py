
from nlightreader.consts.items import MangaLibItems
from nlightreader.consts.urls import URL_SLASHLIB
from nlightreader.items import Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import get_html


class LibBase(AbstractMangaCatalog):
    def __init__(self):
        super().__init__()
        self.url = None
        self.items = MangaLibItems

    def get_preview(self, manga: Manga):
        headers = self.headers | {"Referer": f"{self.url}/"}
        return get_html(
            manga.preview_url,
            headers=headers,
            content_type="content",
        )

    def get_manga_url(self, manga: Manga):
        return f"{self.url}/{manga.content_id}"


class SlashLib(LibBase):
    CATALOG_NAME = "SlashLib(Legacy)"
    CATALOG_ID = 9

    def __init__(self):
        super().__init__()
        self.url = URL_SLASHLIB
