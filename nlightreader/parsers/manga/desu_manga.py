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
    _HEADERS = {"User-Agent": "Nlight", "Referer": f"{_URL}/"}

    def __init__(self) -> None:
        self._client = NetworkClient(headers=self._HEADERS)

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/{manga.content_id}"
        manga_data = self._client.get_json(url).get("response", {})

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

    def search_manga(self, form: RequestForm) -> list[Manga]:
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "genres": ",".join(form.get_genre_ids()),
            "order": form.get_order_id(),
            "kinds": ",".join(form.get_kind_ids()),
        }
        manga_response = self._client.get_json(
            self._URL_API,
            params=params,
        ).get("response", [])

        mangas: list[Manga] = []
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

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL_API}/{manga.content_id}"
        data = self._client.get_json(url)
        chapters: list[Chapter] = []

        for chapter_data in dd_get(data, "response.chapters.list"):
            chapter = Chapter(
                content_id=str(chapter_data.get("id")),
                catalog_id=self.CATALOG_ID,
                volume_number=str(chapter_data.get("vol", "")),
                chapter_number=str(chapter_data.get("ch", "")),
                title=chapter_data.get("title"),
                language=Language.RUSSIAN,
            )
            chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL_API}/{manga.content_id}/chapter/{chapter.content_id}"
        )
        response = self._client.get_json(url)
        images: list[Image] = []
        if not isinstance(response, dict):
            return images
        for img_data in dd_get(response, "response.pages.list"):
            page = img_data.get("page")
            img_url: str = img_data.get("img", "")
            if "?" in img_url:
                img_url = img_url.split("?")[0]
            images.append(
                Image(
                    content_id=str(hash(img_url)),
                    page_number=page,
                    url=img_url,
                ),
            )
        return images

    def get_image(self, image: Image) -> bytes | None:
        if image.url is None:
            return None
        return self._client.get_bytes(image.url)

    def get_preview(self, manga: Manga) -> bytes | None:
        return self._client.get_bytes(
            f"{self._URL}/data/manga/covers/preview/{manga.content_id}.jpg",
        )

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/manga/{manga.content_id}"


__all__ = ["Desu"]
