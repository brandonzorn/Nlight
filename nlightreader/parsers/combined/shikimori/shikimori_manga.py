from typing import override

from models import Manga
from parsers.catalogs_base import AbstractMangaCatalog

from .shikimori_base import ShikimoriBase


class ShikimoriManga(ShikimoriBase, AbstractMangaCatalog):
    CATALOG_ID = 1001
    CATALOG_NAME = "Shikimori(Manga)"
    is_primary = True
    _CONTENT_NAME = "mangas"

    @override
    def get_relations(self, manga: Manga) -> list[Manga]:
        url = (
            f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}/related"
        )
        response = self._client.get_json(url)
        mangas: list[Manga] = []
        if not isinstance(response, list):
            return mangas
        for i in response:
            manga_data = i.get("manga", {})
            if not manga_data:
                continue
            mangas.append(self._setup_manga(manga_data))
        return mangas


__all__ = ["ShikimoriManga"]
