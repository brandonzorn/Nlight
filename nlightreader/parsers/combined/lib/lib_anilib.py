from typing import override

from nlightreader.consts.enums import Nl
from nlightreader.consts.items import AniLibItems
from nlightreader.models import Chapter, Manga
from nlightreader.parsers.catalogs_base import AbstractAnimeCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase
from nlightreader.utils.utils import get_html


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
        episodes_response = get_html(
            url,
            headers=self._headers,
            content_type="json",
        )
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
                ep_id,
                self.CATALOG_ID,
                None,
                "",
                f"Episode {ep_number}",
                Nl.Language.ru,
            )
            episodes.append(episode)
        return episodes

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/ru/anime/{manga.content_id}"


__all__ = [
    "LibAnilib",
]
