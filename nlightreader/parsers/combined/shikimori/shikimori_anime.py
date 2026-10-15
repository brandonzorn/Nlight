from typing import override

from consts.items import ShikimoriAnimeItems
from consts.urls import (
    SHIKIMORI_HEADERS,
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
)
from core.enums import Language, MangaStatus
from items import (
    RequestForm,
)
from models import (
    Episode,
    Genre,
    Manga,
)
from parsers.catalogs_base import AbstractAnimeCatalog
from parsers.service.kodik import Kodik

from .shikimori_base import ShikimoriBase


class ShikimoriAnime(ShikimoriBase, AbstractAnimeCatalog):
    CATALOG_ID = 11
    CATALOG_NAME = "Shikimori(Anime)"
    _URL = URL_SHIKIMORI
    _URL_API = URL_SHIKIMORI_API
    _HEADERS = SHIKIMORI_HEADERS
    _CONTENT_NAME = "animes"

    _FILTERS = ShikimoriAnimeItems

    @override
    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}"
        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return manga
        manga.score = float(response.get("score", 0))
        manga.status = MangaStatus.from_str(response.get("status"))

        description = response.get("description")
        if isinstance(description, str):
            manga.add_description(
                Language.UNDEFINED,
                description,
            )
        return manga

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/animes"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "order": form.get_order_id(),
            "genre": ",".join(form.get_genre_ids()),
            "kind": ",".join(form.get_kind_ids()),
        }
        response = self._client.get_json(
            url,
            params=params,
        )

        mangas: list[Manga] = []
        for data in response:
            if not isinstance(data, dict):
                continue
            mangas.append(self._setup_manga(data))
        return mangas

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

    @override
    def get_genres(self) -> list[Genre]:
        url = f"{self._URL_API}/genres"
        response = self._client.get_json(url)
        genres: list[Genre] = []
        if not isinstance(response, list):
            return genres
        for data in response:
            if data.get("entry_type") != "Anime":
                continue
            genres.append(
                Genre(
                    content_id=str(data.get("id", "")),
                    catalog_id=self.CATALOG_ID,
                    name=data.get("name", ""),
                    russian=data.get("russian", ""),
                ),
            )
        return genres


__all__ = ["ShikimoriAnime"]
