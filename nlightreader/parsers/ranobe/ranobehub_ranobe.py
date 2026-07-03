import base64

from bs4 import BeautifulSoup
import bs4.element

from nlightreader.consts.items import RanobehubItems
from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.utils.network import NetworkClient
from nlightreader.utils.utils import dd_get


class Ranobehub(AbstractRanobeCatalog):
    CATALOG_ID = 4
    CATALOG_NAME = "Ranobehub"
    _FILTERS = RanobehubItems
    _URL = "https://ranobehub.org"
    _URL_API = f"{_URL}/api"

    def __init__(self) -> None:
        self._client = NetworkClient(headers=self._HEADERS)

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/ranobe/{manga.content_id}"
        response_data = self._client.get_json(url).get("data", {})
        if not response_data:
            return manga

        manga.score = response_data.get("rating", 0)
        manga.kind = MangaKind.ranobe

        if status_name := dd_get(response_data, "status.title"):
            manga.status = MangaStatus.from_str(status_name)

        manga.add_description(
            Language.undefined,
            response_data.get("description"),
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
        response = self._client.get_json(url, params=params).get(
            "resource",
            [],
        )
        mangas: list[Manga] = []
        if not isinstance(response, list):
            return mangas

        for i in response:
            manga_id = str(i.get("id"))
            name = dd_get(i, "names.eng", "")
            russian = dd_get(i, "names.rus", "")

            manga = Manga(
                content_id=manga_id,
                catalog_id=self.CATALOG_ID,
                name=name,
                russian=russian,
            )
            manga.status = MangaStatus.from_str(i.get("status"))
            manga.preview_url = dd_get(i, "poster.medium", None)

            mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL_API}/ranobe/{manga.content_id}/contents"
        response = self._client.get_json(url)
        chapters: list[Chapter] = []
        if not isinstance(response, dict):
            return chapters
        for i in response.get("volumes", []):
            volume_num = i.get("num")
            for chapter_data in i.get("chapters", []):
                chapter = Chapter(
                    content_id=str(chapter_data.get("id")),
                    catalog_id=self.CATALOG_ID,
                    volume_number=volume_num,
                    chapter_number=chapter_data.get("num"),
                    title=chapter_data.get("name"),
                    language=Language.ru,
                )
                chapters.append(chapter)
        chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL}/ranobe/{manga.content_id}/"
            f"{chapter.volume_number}/{chapter.chapter_number}"
        )
        return [Image(content_id="", page_number=1, url=url)]

    def get_image(self, image: Image) -> str | None:
        def get_chapter_content_image(media_id: str) -> str:
            url = f"{self._URL_API}/media/{media_id}"
            chapter_image = self._client.get_bytes(url)
            if not chapter_image:
                return ""
            str_equivalent_image = base64.b64encode(chapter_image).decode()
            return f"data:image/png;base64,{str_equivalent_image}"

        def find_text_container(
            containers: bs4.element.ResultSet,
        ) -> bs4.element.Tag | None:
            for container in containers:
                if container.has_attr("data-container"):
                    return container
            return None

        response = self._client.get_text(image.url)
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
                    f'<p><img src="{get_chapter_content_image(media)}"></p>'
                )
            else:
                content += str(p)
        return content

    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(url)

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/ranobe/{manga.content_id}"


__all__ = ["Ranobehub"]
