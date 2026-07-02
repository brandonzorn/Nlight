from nlightreader.consts.items import MangaLibItems
from nlightreader.models import Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.network import NetworkClient


class LibBase(AbstractMangaCatalog):
    _FILTERS = MangaLibItems
    _URL = None

    def __init__(self) -> None:
        self._client = NetworkClient(headers=self._HEADERS)

    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(
            url,
            extra_headers={"Referer": f"{self._URL}/"},
        )

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
