from nlightreader.consts.items import RemangaItems
from nlightreader.core.enums import Language, MangaKind
from nlightreader.core.network import NetworkClient
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import dd_get


class Remanga(AbstractMangaCatalog):
    CATALOG_ID = 6
    CATALOG_NAME = "ReManga"
    _FILTERS = RemangaItems
    _URL = "https://remanga.org"
    _URL_API = f"{_URL}/api"

    def __init__(self) -> None:
        self._client = NetworkClient(
            catalog_name=self.CATALOG_NAME,
            headers=self._HEADERS,
        )

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/titles/{manga.content_id}/"
        response_data = self._client.get_json(url).get("content", {})

        if not response_data:
            return manga

        kind_name = dd_get(response_data, "type.name")
        manga.kind = MangaKind.from_str(kind_name)

        manga.score = float(response_data.get("avg_rating", 0))

        img = dd_get(response_data, "img.high")
        if img and img != "/media/None":
            manga.preview_url = f"{self._URL}{img}"

        manga.add_description(
            Language.UNDEFINED,
            response_data.get("description"),
        )
        return manga

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/search/catalog"
        if form.search:
            url = f"{self._URL_API}/search"
        params = {
            "page": form.page,
            "query": form.search,
            "count": 40,
            "ordering": form.get_order_id(),
            "types": form.get_kind_ids(),
        }
        response = self._client.get_json(
            url,
            params=params,
        )

        mangas: list[Manga] = []
        if not isinstance(response, dict):
            return mangas

        for data in response.get("content", {}):
            manga_id = data.get("dir")
            name = data.get("en_name")
            russian = data.get("rus_name")
            manga = Manga(
                content_id=manga_id,
                catalog_id=self.CATALOG_ID,
                name=name,
                russian=russian,
            )
            manga.kind = MangaKind.from_str(data.get("type"))
            manga.score = float(data.get("avg_rating"))

            if (img := data.get("img", {}).get("high")) and (
                img != "/media/None"
            ):
                manga.preview_url = f"{self._URL}{img}"
            mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL_API}/titles/{manga.content_id}/"
        response = self._client.get_json(url)
        chapters: list[Chapter] = []
        if not isinstance(response, dict):
            return chapters
        data = response.get("content")
        branch_id = data.get("branches")[0].get("id")
        chapters_data = self._client.get_json(
            f"{self._URL_API}/titles/chapters"
            f"?branch_id={branch_id}&user_data=0",
        )
        if not isinstance(chapters_data, dict):
            return chapters
        data = chapters_data.get("content", {})
        for ch in data:
            if ch.get("is_paid"):
                continue
            chapter = Chapter(
                content_id=ch.get("id"),
                catalog_id=self.CATALOG_ID,
                volume_number=str(ch.get("tome")),
                chapter_number=ch.get("chapter"),
                title=ch.get("name"),
                language=Language.RUSSIAN,
            )
            chapters.append(chapter)
        return chapters

    def get_images(self, _: Manga, chapter: Chapter) -> list[Image]:
        url = f"{self._URL_API}/titles/chapters/{chapter.content_id}/"
        response = self._client.get_json(url)
        images: list[Image] = []
        if not isinstance(response, dict):
            return images
        for i, page_data in enumerate(dd_get(response, "content.pages")):
            page_data = page_data[0]
            pg_id = page_data.get("id")
            page = i + 1
            pg_link = page_data.get("link")
            images.append(
                Image(
                    content_id=pg_id,
                    page_number=page,
                    url=pg_link,
                ),
            )
        return images

    def get_image(self, image: Image) -> bytes | None:
        headers = {
            "User-Agent": "Nlight",
            "Referer": f"{self._URL}/",
        }
        image_response = self._client.get_bytes(
            f"{image.url}",
            extra_headers=headers,
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_preview(self, manga: Manga) -> bytes | None:
        image_response = self._client.get_bytes(manga.preview_url)
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/manga/{manga.content_id}"


__all__ = ["Remanga"]
