from nlightreader.consts.items import MangaLibItems
from nlightreader.models import Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import get_html


class LibBase(AbstractMangaCatalog):
    _FILTERS = MangaLibItems
    _URL = None

    def get_preview(self, manga: Manga) -> bytes | None:
        headers = self._HEADERS | {"Referer": f"{self._URL}/"}
        return get_html(manga.preview_url, headers=headers, content_type="content")

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/{manga.content_id}"


class SlashLib(LibBase):
    CATALOG_NAME = "SlashLib(Legacy)"
    CATALOG_ID = 9
    _URL = "https://v2.slashlib.me"


__all__ = [
    "LibBase",
    "SlashLib",
]
