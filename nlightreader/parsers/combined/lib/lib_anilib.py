from typing import override

from nlightreader.consts.items import AniLibItems
from nlightreader.core.enums import Language
from nlightreader.models import Episode, Manga
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
    def get_episodes(self, anime: Manga) -> list[Episode]:
        url = f"{self._URL_API}/episodes?anime_id={anime.content_id}"
        episodes: list[Episode] = []
        episodes_response = self._client.get_json(url)
        if not isinstance(episodes_response, dict):
            return episodes

        for ep_data in reversed(episodes_response.get("data", [])):
            if not isinstance(ep_data, dict):
                continue

            ep_id = ep_data.get("id")
            ep_number = ep_data.get("number", 0)

            if ep_id is None:
                continue

            name = ep_data.get("name")
            season = str(ep_data.get("season") or "")

            episode = Episode(
                content_id=str(ep_id),
                catalog_id=self.CATALOG_ID,
                season_number=int(season),
                episode_number=int(ep_number),
                title=name,
                url=None,
                language=Language.RUSSIAN,
            )
            episodes.append(episode)
        return episodes


__all__ = ["LibAnilib"]
