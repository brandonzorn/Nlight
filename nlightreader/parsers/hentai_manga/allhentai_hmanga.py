from bs4 import BeautifulSoup

from nlightreader.consts.urls import URL_ALLHENTAI, URL_ALLHENTAI_API
from nlightreader.consts.enums import Nl
from nlightreader.exceptions import parser_content_exc
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractHentaiMangaCatalog
from nlightreader.utils.utils import get_html, make_request


class AllHentai(AbstractHentaiMangaCatalog):
    CATALOG_ID = 8
    CATALOG_NAME = "AllHentai"

    def __init__(self):
        super().__init__()
        self.url = URL_ALLHENTAI
        self.url_api = URL_ALLHENTAI_API

    def search_manga(self, form):
        url = f"{self.url}/search"
        if not form.search:
            raise parser_content_exc.RequestsParamsError(
                "Search field is empty",
            )
        params = {
            "q": form.search,
            "+": "Искать!",
            "fast-filter": "CREATION",
        }
        response = make_request(
            url,
            "POST",
            headers=self.headers,
            data=params,
            content_type="text",
        )
        mangas = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            html_items = soup.findAll("div", class_="tile")
            for i in html_items:
                manga_desc = i.find("div", class_="desc")
                base_info = manga_desc.find("a")
                manga_id = base_info.get("href")
                name = base_info.get("title")
                if manga_id and name:
                    mangas.append(
                        Manga(manga_id, self.CATALOG_ID, name, ""),
                    )
        return mangas

    def get_chapters(self, manga: Manga):
        url = f"{self.url}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="text")

        chapters = []
        if not response:
            return chapters

        soup = BeautifulSoup(response, "html.parser")
        chapters_list_item = soup.find("div", id="chapters-list")
        for chapter_item in chapters_list_item.findAll(
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
                Nl.Language.ru,
            )
            chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        return []

    def get_image(self, image: Image):
        return

    def get_preview(self, manga: Manga):
        url = f"{self.url}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="text")
        if response:
            soup = BeautifulSoup(response, "html.parser")
            html_item = soup.find("img", class_="")
            if html_item:
                img_src = html_item.get("src")
                if img_src:
                    return get_html(
                        img_src,
                        content_type="content",
                        headers=self.headers,
                    )

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/{manga.content_id}"
