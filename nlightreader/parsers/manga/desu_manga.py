from typing import ClassVar, override

from nlightreader.consts.items import DesuItems
from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.network import NetworkClient
from nlightreader.utils.utils import dd_get


class Desu(AbstractMangaCatalog):
    CATALOG_ID = 0
    CATALOG_NAME = "Desu"
    _FILTERS = DesuItems
    _URL = "https://desu.uno"
    _URL_API = f"{_URL}/manga/api"
    _HEADERS: ClassVar = {"User-Agent": "Nlight", "Referer": f"{_URL}/"}

    def __init__(self) -> None:
        self._client = NetworkClient(headers=self._HEADERS)

    @override
    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/{manga.content_id}"
        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return manga

        manga_data = response.get("response", {})
        if not isinstance(manga_data, dict):
            return manga

        manga.score = manga_data.get("score", 0)
        manga.kind = MangaKind.from_str(manga_data.get("kind"))
        manga.status = MangaStatus.from_str(manga_data.get("status"))

        chapters_data = manga_data.get("chapters", {})

        manga.volumes = int(chapters_data.get("last", {}).get("vol", 0))
        manga.chapters = int(chapters_data.get("count", 0))

        manga.add_description(
            Language.UNDEFINED,
            manga_data.get("description", ""),
        )
        return manga

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "genres": ",".join(form.get_genre_ids()),
            "order": form.get_order_id(),
            "kinds": ",".join(form.get_kind_ids()),
        }
        mangas: list[Manga] = []
        response = self._client.get_json(
            self._URL_API,
            params=params,
        )
        if not isinstance(response, dict):
            return mangas

        manga_response = response.get("response")
        if not isinstance(manga_response, list):
            return mangas

        for manga_data in manga_response:
            manga_id = manga_data.get("id")
            if manga_id is None:
                continue
            mangas.append(
                Manga(
                    content_id=str(manga_id),
                    catalog_id=self.CATALOG_ID,
                    name=manga_data.get("name"),
                    russian=manga_data.get("russian"),
                ),
            )
        return mangas

    @override
    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL_API}/{manga.content_id}"
        chapters: list[Chapter] = []

        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return chapters

        chapters_data = dd_get(response, "response.chapters.list", [])
        if not isinstance(chapters_data, list):
            return chapters

        for chapter_data in chapters_data:
            if not isinstance(chapter_data, dict):
                continue
            content_id = chapter_data.get("id")
            if not content_id:
                continue
            chapter = Chapter(
                content_id=str(content_id),
                catalog_id=self.CATALOG_ID,
                volume_number=str(chapter_data.get("vol") or ""),
                chapter_number=str(chapter_data.get("ch") or ""),
                title=str(chapter_data.get("title") or ""),
                language=Language.RUSSIAN,
            )
            chapters.append(chapter)
        return chapters

    @override
    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL_API}/{manga.content_id}/chapter/{chapter.content_id}"
        )
        images: list[Image] = []

        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return images

        images_data = dd_get(response, "response.pages.list", [])
        if not isinstance(images_data, list):
            return images

        for img_data in images_data:
            if not isinstance(img_data, dict):
                continue
            page = img_data.get("page")
            if not isinstance(page, int):
                continue
            img_url = str(img_data.get("img") or "")
            if "?" in img_url:
                img_url = img_url.split("?", maxsplit=1)[0]
            images.append(
                Image(
                    content_id=str(hash(img_url)),
                    page_number=page,
                    url=img_url,
                ),
            )
        return images

    @override
    def get_image(self, image: Image) -> bytes | None:
        url = image.url
        if url is None:
            return None
        return self._client.get_bytes(url)

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        return self._client.get_bytes(
            f"{self._URL}/data/manga/covers/preview/{manga.content_id}.jpg",
        )

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/manga/{manga.content_id}"


__all__ = ["Desu"]
