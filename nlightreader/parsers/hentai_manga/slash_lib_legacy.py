from typing import override

from nlightreader.consts.items import MangaLibItems
from nlightreader.core.network import NetworkClient
from nlightreader.models import Manga
from nlightreader.parsers.catalogs_base import (
    AbstractHentaiMangaCatalog,
)


class SlashLibLegacy(AbstractHentaiMangaCatalog):
    _URL = "https://v2.slashlib.me"
    _FILTERS = MangaLibItems
    CATALOG_NAME = "SlashLib(Legacy)"
    CATALOG_ID = 9

    def __init__(self) -> None:
        self._client = NetworkClient(
            catalog_name=self.CATALOG_NAME,
            headers=self._HEADERS,
        )

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(
            url,
            extra_headers={"Referer": f"{self._URL}/"},
        )

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/{manga.content_id}"


__all__ = ["SlashLibLegacy"]
