from typing import override

from bs4 import BeautifulSoup, Tag

from nlightreader.core.enums import Language
from nlightreader.core.exceptions import parser_content_exc
from nlightreader.core.network import NetworkClient
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Manga
from nlightreader.parsers.catalogs_base import AbstractHentaiMangaCatalog
from nlightreader.utils.utils import make_request


class AllHentai(AbstractHentaiMangaCatalog):
    CATALOG_ID = 8
    CATALOG_NAME = "AllHentai"
    _URL = "https://20.allhen.online"

    def __init__(self) -> None:
        self._client = NetworkClient(
            catalog_name=self.CATALOG_NAME,
            headers=self._HEADERS,
        )

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL}/search"
        if not form.search:
            msg = "Search field is empty"
            raise parser_content_exc.RequestsParamsError(
                msg,
            )
        params = {
            "q": form.search,
            "+": "Искать!",
            "fast-filter": "CREATION",
        }
        response = make_request(
            url,
            "POST",
            headers=self._HEADERS,
            data=params,
            content_type="text",
        )
        mangas: list[Manga] = []
        if not isinstance(response, str):
            return mangas
        soup = BeautifulSoup(response, "html.parser")
        html_items = soup.find_all("div", class_="tile")
        for i in html_items:
            manga_desc = i.find("div", class_="desc")
            if not isinstance(manga_desc, Tag):
                continue
            base_info = manga_desc.find("a")
            if not isinstance(base_info, Tag):
                continue
            manga_id = base_info.get("href")
            name = base_info.get("title")
            if not isinstance(manga_id, str) or not isinstance(name, str):
                continue
            mangas.append(
                Manga(
                    content_id=manga_id,
                    catalog_id=self.CATALOG_ID,
                    name=name,
                    russian="",
                ),
            )
        return mangas

    @override
    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL}/{manga.content_id}"
        response = self._client.get_text(url)

        chapters: list[Chapter] = []
        if not isinstance(response, str):
            return chapters

        soup = BeautifulSoup(response, "html.parser")
        chapters_list_item = soup.find("div", id="chapters-list")
        if not isinstance(chapters_list_item, Tag):
            return chapters
        for chapter_item in chapters_list_item.find_all(
            "tr",
            class_="item-row",
        ):
            volume = str(chapter_item.get("data-vol") or "")
            chapter_num = str(chapter_item.get("data-num") or "")
            if chapter_num.isdigit():
                chapter_as_num = int(chapter_num) / 10
                if chapter_as_num.is_integer():
                    chapter_as_num = int(chapter_as_num)
                chapter_num = str(chapter_as_num)

            chapter = Chapter(
                content_id=manga.content_id,
                catalog_id=self.CATALOG_ID,
                volume_number=volume,
                chapter_number=chapter_num,
                title="",
                language=Language.RUSSIAN,
            )
            chapters.append(chapter)
        return chapters

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        url = f"{self._URL}/{manga.content_id}"
        response = self._client.get_text(url)
        if not isinstance(response, str):
            return None
        soup = BeautifulSoup(response, "html.parser")
        img_tag = soup.find("img", class_="")
        if not isinstance(img_tag, Tag):
            return None
        img_src = img_tag.get("src")
        if not isinstance(img_src, str):
            return None
        image_response = self._client.get_bytes(img_src)
        if not isinstance(image_response, bytes):
            return None
        return image_response

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/{manga.content_id}"


__all__ = [
    "AllHentai",
]
