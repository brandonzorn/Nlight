import base64

from bs4 import BeautifulSoup
import bs4.element

from nlightreader.consts.items import RanobehubItems
from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.utils.utils import get_data, get_html


class Ranobehub(AbstractRanobeCatalog):
    CATALOG_ID = 4
    CATALOG_NAME = "Ranobehub"
    _FILTERS = RanobehubItems
    _URL = "https://ranobehub.org"
    _URL_API = f"{_URL}/api"

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/ranobe/{manga.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if response:
            data = response.get("data")

            manga.score = data.get("rating")
            manga.kind = MangaKind.ranobe

            if status_name := data.get("status").get("title"):
                manga.status = MangaStatus.from_str(status_name)

            manga.add_description(
                Language.undefined,
                data.get("description"),
            )
        return manga

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/search"
        params = {
            "title-contains": form.search,
            "page": form.page,
            "sort": form.get_order_id(),
            "tags:positive[]": [int(i) for i in form.get_genre_ids()],
        }
        response = get_html(
            url,
            headers=self._HEADERS,
            params=params,
            content_type="json",
        )

        mangas: list[Manga] = []
        if not response:
            return mangas

        for i in get_data(response, ["resource"], default_val=[]):
            manga_id = str(i.get("id"))
            name = i.get("names").get("eng")
            russian = i.get("names").get("rus")

            manga = Manga(manga_id, self.CATALOG_ID, name, russian)
            manga.status = MangaStatus.from_str(i.get("status"))
            manga.preview_url = i.get("poster").get("medium")

            mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL_API}/ranobe/{manga.content_id}/contents"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        chapters = []
        if response:
            for i in get_data(response, ["volumes"], default_val=[]):
                volume_num = i.get("num")
                for chapter_data in get_data(i, ["chapters"], []):
                    chapter = Chapter(
                        str(chapter_data.get("id")),
                        self.CATALOG_ID,
                        volume_num,
                        chapter_data.get("num"),
                        chapter_data.get("name"),
                        Language.ru,
                    )
                    chapters.append(chapter)
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL}/ranobe/{manga.content_id}/"
            f"{chapter.volume_number}/{chapter.chapter_number}"
        )
        return [Image("", 1, url)]

    def get_image(self, image: Image) -> str | None:
        def get_chapter_content_image(media_id: str) -> str:
            url = f"{self._URL_API}/media/{media_id}"
            chapter_image = get_html(url, headers=self._HEADERS).content
            str_equivalent_image = base64.b64encode(chapter_image).decode()
            return f"data:image/png;base64,{str_equivalent_image}"

        def find_text_container(
            containers: bs4.element.ResultSet,
        ) -> bs4.element.Tag | None:
            for container in containers:
                if container.has_attr("data-container"):
                    return container
            return None

        response = get_html(image.url, content_type="text")
        if not isinstance(response, str):
            return None
        soup = BeautifulSoup(response, "html.parser")
        text_container = find_text_container(
            soup.findAll("div", {"class": "ui text container"}),
        )
        if not text_container:
            return None

        content = ""

        header = soup.find("div", class_="title-wrapper")
        if header is not None:
            header_text = header.find("h1", class_="ui header")
            if header_text is not None:
                content += f"<h1>{header_text.text}</h1>"

        for p in text_container.findAll("p"):
            if p.find("img"):
                media: str = p.find("img")["data-media-id"]
                content += (
                    f"<p>"
                    f'<img src="{get_chapter_content_image(media)}">'
                    f"</p>"
                )
            else:
                content += str(p)
        return content

    def get_preview(self, manga: Manga) -> bytes | None:
        if not isinstance(manga.preview_url, str):
            return None
        image_response = get_html(
            manga.preview_url,
            headers=self._HEADERS,
            content_type="content",
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/ranobe/{manga.content_id}"


__all__ = [
    "Ranobehub",
]
