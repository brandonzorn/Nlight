from typing import override

from consts.items import ShikimoriRanobeItems
from models import Manga
from parsers.catalogs_base import AbstractRanobeCatalog

from .shikimori_base import ShikimoriBase


class ShikimoriRanobe(ShikimoriBase, AbstractRanobeCatalog):
    CATALOG_ID = 1002
    CATALOG_NAME = "Shikimori(Ranobe)"
    _CONTENT_NAME = "ranobe"

    _FILTERS = ShikimoriRanobeItems

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        file_name = f"{manga.content_id}.jpg"
        url = f"{self._URL}/system/mangas/original/{file_name}"
        response = self._client.get_bytes(url)
        if not isinstance(response, bytes):
            return None
        return response


__all__ = ["ShikimoriRanobe"]
