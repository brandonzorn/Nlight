from typing import override

from consts.items import ShikimoriAnimeItems
from consts.urls import (
    SHIKIMORI_HEADERS,
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
)
from core.enums import Language
from models import Episode, Manga
from parsers.catalogs_base import AbstractAnimeCatalog
from parsers.service.kodik import Kodik

from .shikimori_base import ShikimoriBase


class ShikimoriAnime(ShikimoriBase, AbstractAnimeCatalog):
    CATALOG_ID = 11
    CATALOG_NAME = "Shikimori(Anime)"

    _HEADERS = SHIKIMORI_HEADERS
    _FILTERS = ShikimoriAnimeItems

    _URL = URL_SHIKIMORI
    _URL_API = URL_SHIKIMORI_API

    _CONTENT_NAME = "animes"
    _PREVIEW_FOLDER = "animes"
    _GENRE_ENTRY_TYPE = "Anime"

    @override
    def _fill_extra_details(self, manga: Manga, response: dict) -> None:
        pass

    @override
    def get_episodes(self, anime: Manga) -> list[Episode]:
        translators = Kodik.search(anime.content_id)
        episodes = []
        for translator in translators:
            for episode_num in range(translator.episodes, 0, -1):
                episode = Episode(
                    content_id=f"{translator.content_id}{episode_num}",
                    catalog_id=self.CATALOG_ID,
                    season_number=0,
                    episode_number=episode_num,
                    title="",
                    url=f"http:{translator.kodik_url}?episode={episode_num}",
                    language=Language.RUSSIAN,
                    translator=translator.translator_text,
                )
                episodes.append(episode)
        return episodes


__all__ = ["ShikimoriAnime"]
