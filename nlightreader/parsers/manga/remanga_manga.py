from nlightreader.consts.items import RemangaItems
from nlightreader.core.enums import Language, MangaKind
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import get_html


class Remanga(AbstractMangaCatalog):
    CATALOG_ID = 6
    CATALOG_NAME = "ReManga"
    _FILTERS = RemangaItems
    _URL = "https://remanga.org"
    _URL_API = f"{_URL}/api"

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/titles/{manga.content_id}/"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            data = response.get("content")

            if kind_name := data.get("type").get("name"):
                manga.kind = MangaKind.from_str(kind_name)

            manga.score = float(data.get("avg_rating"))
            if (img := data.get("img").get("high")) and (img != "/media/None"):
                manga.preview_url = f"{self._URL}{img}"

            manga.add_description(
                Language.undefined,
                data.get("description"),
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
        response = get_html(
            url,
            headers=self._HEADERS,
            params=params,
            content_type="json",
        )

        mangas: list[Manga] = []
        if not isinstance(response, dict):
            return mangas

        for data in response.get("content", {}):
            manga_id = data.get("dir")
            name = data.get("en_name")
            russian = data.get("rus_name")
            manga = Manga(manga_id, self.CATALOG_ID, name, russian)
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
        response = get_html(url, headers=self._HEADERS, content_type="json")
        chapters: list[Chapter] = []
        if not isinstance(response, dict):
            return chapters
        data = response.get("content")
        branch_id = data.get("branches")[0].get("id")
        chapters_data = get_html(
            f"{self._URL_API}/titles/chapters"
            f"?branch_id={branch_id}&user_data=0",
            headers=self._HEADERS,
            content_type="json",
        )
        if not isinstance(chapters_data, dict):
            return chapters
        data = chapters_data.get("content", {})
        for ch in data:
            if ch.get("is_paid"):
                continue
            chapter = Chapter(
                ch.get("id"),
                self.CATALOG_ID,
                str(ch.get("tome")),
                ch.get("chapter"),
                ch.get("name"),
                Language.ru,
            )
            chapters.append(chapter)
        return chapters

    def get_images(self, _: Manga, chapter: Chapter) -> list[Image]:
        url = f"{self._URL_API}/titles/chapters/{chapter.content_id}/"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        images: list[Image] = []
        if not isinstance(response, dict):
            return images
        for i, page_data in enumerate(
            response.get("content", {}).get("pages", []),
        ):
            page_data = page_data[0]
            pg_id = page_data.get("id")
            page = i + 1
            pg_link = page_data.get("link")
            images.append(Image(pg_id, page, pg_link))
        return images

    def get_image(self, image: Image) -> bytes | None:
        headers = {
            "User-Agent": "Nlight",
            "Referer": f"{self._URL}/",
        }
        image_response = get_html(
            f"{image.url}",
            headers=headers,
            content_type="content",
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_preview(self, manga: Manga) -> bytes | None:
        image_response = get_html(
            manga.preview_url,
            headers=self._HEADERS,
            content_type="content",
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/manga/{manga.content_id}"


__all__ = ["Remanga"]
