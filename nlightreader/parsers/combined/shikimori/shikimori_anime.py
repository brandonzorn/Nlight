from nlightreader.consts.items import ShikimoriAnimeItems
from nlightreader.consts.urls import (
    SHIKIMORI_HEADERS,
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
)
from nlightreader.core.enums import Language, MangaStatus
from nlightreader.items import (
    RequestForm,
)
from nlightreader.models import Chapter, Character, Genre, Manga, Order
from nlightreader.parsers.catalogs_base import AbstractAnimeCatalog
from nlightreader.parsers.service.kodik import Kodik
from nlightreader.utils.network import NetworkClient


class ShikimoriAnime(AbstractAnimeCatalog):
    CATALOG_ID = 11
    CATALOG_NAME = "Shikimori(Anime)"
    _URL = URL_SHIKIMORI
    _URL_API = URL_SHIKIMORI_API
    _HEADERS = SHIKIMORI_HEADERS

    def __init__(self) -> None:
        self._client = NetworkClient(headers=self._HEADERS)

    def _setup_manga(self, data: dict) -> Manga:
        return Manga(
            content_id=str(data.get("id", "")),
            catalog_id=self.CATALOG_ID,
            name=data.get("name", ""),
            russian=data.get("russian", ""),
        )

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/animes/{manga.content_id}"
        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return manga
        manga.score = float(response.get("score", 0))
        manga.status = MangaStatus.from_str(response.get("status"))

        description = response.get("description")
        if isinstance(description, str):
            manga.add_description(
                Language.undefined,
                description,
            )
        return manga

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
        if response is None:
            return mangas
        for data in response:
            if not isinstance(data, dict):
                continue
            mangas.append(self._setup_manga(data))
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        translators = Kodik.search(manga.content_id)
        chapters = []
        for translator in translators:
            for episode_num in range(translator.episodes, 0, -1):
                chapter = Chapter(
                    content_id=f"{translator.content_id}{episode_num}",
                    catalog_id=self.CATALOG_ID,
                    volume_number=None,
                    chapter_number="",
                    title=f"Episode {episode_num}",
                    language=Language.ru,
                )
                chapter.translator = (
                    f"{translator.translator} ({translator.tr_type})"
                )
                chapter.__setattr__(
                    "url",
                    f"http:{translator.kodik_url}?episode={episode_num}",
                )
                chapters.append(chapter)
        return chapters

    def get_character(self, character: Character) -> Character:
        url = f"{self._URL_API}/characters/{character.content_id}"
        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return character
        description = response.get("description")
        if isinstance(description, str):
            character.description = description
        return character

    def get_preview(self, manga: Manga) -> bytes | None:
        url = f"{self._URL}/system/animes/original/{manga.content_id}.jpg"
        response = self._client.get_bytes(url)
        if not isinstance(response, bytes):
            return None
        return response

    def get_character_preview(self, character: Character) -> bytes | None:
        url = (
            f"{self._URL}/system/characters/"
            f"original/{character.content_id}.jpg"
        )
        image_response = self._client.get_bytes(url)
        if not isinstance(image_response, bytes):
            return None
        return image_response

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

    def get_orders(self) -> list[Order]:
        return [
            Order(
                content_id=i["value"],
                catalog_id=self.CATALOG_ID,
                name=i["name"],
                russian=i["russian"],
            )
            for i in ShikimoriAnimeItems.ORDERS
        ]

    def get_characters(self, manga: Manga) -> list[Character]:
        url = f"{self._URL_API}/animes/{manga.content_id}/roles"
        response = self._client.get_json(url)
        characters: list[Character] = []
        if not isinstance(response, dict):
            return characters
        for data in response:
            roles = data.get("roles")
            if not isinstance(roles, list) or len(roles) == 0:
                continue
            role = data.get("roles")[0]
            if role not in ["Supporting", "Main"]:
                continue
            character_data = data.get("character")
            if not isinstance(character_data, dict):
                continue
            characters.append(
                Character(
                    content_id=str(character_data.get("id")),
                    catalog_id=self.CATALOG_ID,
                    name=character_data.get("name", ""),
                    russian=character_data.get("russian", ""),
                    description="",
                    role=role,
                ),
            )
        characters.sort(key=lambda x: x.role)
        return characters

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/animes/{manga.content_id}"


__all__ = ["ShikimoriAnime"]
