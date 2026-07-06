from typing import override

from nlightreader.consts.items import AniLibItems
from nlightreader.core.enums import Language
from nlightreader.models import Chapter, Manga
from nlightreader.parsers.catalogs_base import AbstractAnimeCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase


class LibAnilib(LibBase, AbstractAnimeCatalog):
    CATALOG_NAME = "AniLib"
    CATALOG_ID = 14
    _FILTERS = AniLibItems
    _URL = "https://v5.animelib.org"
    _URL_API = "https://hapi.hentaicdn.org/api"

    _CONTENT_NAME = "anime"
    _SITE_ID = 5

    @override
    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL_API}/episodes?anime_id={manga.content_id}"
        episodes: list[Chapter] = []
        episodes_response = self._client.get_json(url)
        if not isinstance(episodes_response, dict):
            return episodes

        for ep_data in reversed(episodes_response.get("data", [])):
            if not isinstance(ep_data, dict):
                continue

            ep_id = ep_data.get("id")
            ep_number = ep_data.get("number", 0)

            if not isinstance(ep_id, str):
                continue

            episode = Chapter(
                content_id=ep_id,
                catalog_id=self.CATALOG_ID,
                volume_number=None,
                chapter_number="",
                title=f"Episode {ep_number}",
                language=Language.RUSSIAN,
            )
            episodes.append(episode)
        return episodes

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/ru/anime/{manga.content_id}"


__all__ = [
    "LibAnilib",
]
