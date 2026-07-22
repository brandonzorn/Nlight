import base64
from typing import override

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

    @override
    def get_manga(self, manga: Manga) -> Manga:
        manga.kind = MangaKind.RANOBE
        url = f"{self._URL_API}/ranobe/{manga.content_id}"
        response = self._client.get_json(url)
        if not isinstance(response, dict):
            return manga
        response_data = response.get("data", {})

        manga.score = response_data.get("rating", 0)

        status_name = dd_get(response_data, "status.title")
        if isinstance(status_name, str):
            manga.status = MangaStatus.from_str(status_name)

        manga.add_description(
            Language.UNDEFINED,
            response_data.get("description"),
        )
        return manga

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/search"
        params = {
            "title-contains": form.search,
            "page": form.page,
            "sort": form.get_order_id(),
            "tags:positive[]": [int(i) for i in form.get_genre_ids()],
        }
        response = self._client.get_json(url, params=params)
        mangas: list[Manga] = []
        if not isinstance(response, dict):
            return mangas

        response_data = response.get("resource", [])
        for i in response_data:
            manga_id = str(i.get("id"))
            name = dd_get(i, "names.eng")
            if not isinstance(name, str):
                continue
            russian = dd_get(i, "names.rus")
            if not isinstance(russian, str):
                russian = ""

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

    @override
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
                    language=Language.RUSSIAN,
                )
                chapters.append(chapter)
        chapters.reverse()
        return chapters

    @override
    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL}/ranobe/{manga.content_id}/"
            f"{chapter.volume_number}/{chapter.chapter_number}"
        )
        return [Image(content_id="", page_number=1, url=url)]

    @override
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

        url = image.url
        if url is None:
            return None
        response = self._client.get_text(url)
        if not isinstance(response, str):
            return None
        soup = BeautifulSoup(response, "html.parser")
        text_container = find_text_container(
            soup.find_all("div", {"class": "ui text container"}),
        )
        if not text_container:
            return None

        content = ""

        header = soup.find("div", class_="title-wrapper")
        if header is not None:
            header_text = header.find("h1", class_="ui header")
            if header_text is not None:
                content += f"<h1>{header_text.text}</h1>"

        for p in text_container.find_all("p"):
            img_tag = p.find("img")
            if img_tag:
                img_url = img_tag["data-media-id"]
                if not isinstance(img_url, str):
                    continue
                content += (
                    f'<p><img src="{get_chapter_content_image(img_url)}"></p>'
                )
            else:
                content += str(p)
        return content

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(url)

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/ranobe/{manga.content_id}"


__all__ = ["Ranobehub"]
