from bs4 import BeautifulSoup

from nlightreader.core.enums import Language
from nlightreader.exceptions import parser_content_exc
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractHentaiMangaCatalog
from nlightreader.utils.utils import get_html, make_request


class AllHentai(AbstractHentaiMangaCatalog):
    CATALOG_ID = 8
    CATALOG_NAME = "AllHentai"
    _URL = "https://20.allhen.online"

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
            base_info = manga_desc.find("a")
            manga_id = base_info.get("href")
            name = base_info.get("title")
            if not isinstance(manga_id, str) or not isinstance(name, str):
                continue
            mangas.append(
                Manga(
                    manga_id,
                    self.CATALOG_ID,
                    name,
                    "",
                ),
            )
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL}/{manga.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="text")

        chapters: list[Chapter] = []
        if not isinstance(response, str):
            return chapters

        soup = BeautifulSoup(response, "html.parser")
        chapters_list_item = soup.find("div", id="chapters-list")
        for chapter_item in chapters_list_item.find_all(
            "tr",
            class_="item-row",
        ):
            volume: str = chapter_item.get("data-vol")
            chapter_num: str = chapter_item.get("data-num")
            if chapter_num.isdigit():
                chapter_as_num = int(chapter_num) / 10
                if chapter_as_num.is_integer():
                    chapter_as_num = int(chapter_as_num)
                chapter_num = str(chapter_as_num)

            chapter = Chapter(
                manga.content_id,
                self.CATALOG_ID,
                volume,
                chapter_num,
                "",
                Language.ru,
            )
            chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        return super().get_images(manga, chapter)

    def get_image(self, image: Image) -> bytes | None:
        return super().get_image(image)

    def get_preview(self, manga: Manga) -> bytes | None:
        url = f"{self._URL}/{manga.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="text")
        if not isinstance(response, str):
            return None
        soup = BeautifulSoup(response, "html.parser")
        html_item = soup.find("img", class_="")
        img_src = html_item.get("src")
        if not isinstance(img_src, str):
            return None
        image_response = get_html(
            img_src,
            content_type="content",
            headers=self._HEADERS,
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/{manga.content_id}"


__all__ = [
    "AllHentai",
]
