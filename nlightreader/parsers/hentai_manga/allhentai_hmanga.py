from typing import override

from bs4 import BeautifulSoup

from nlightreader.consts import URL_ALLHENTAI, URL_ALLHENTAI_API, Nl
from nlightreader.items import Manga, Chapter, Image
from nlightreader.parsers.catalogs_base import AbstractHentaiMangaCatalog
from nlightreader.utils.utils import get_html, make_request


class AllHentai(AbstractHentaiMangaCatalog):
    CATALOG_ID = 8
    CATALOG_NAME = "AllHentai"

    def __init__(self):
        super().__init__()
        self.url = URL_ALLHENTAI
        self.url_api = URL_ALLHENTAI_API
        self.cookies = {
            "remember_me":
                "JTJCWlRqaDdOS3ElMkZKQzJXbFZxN3JrRzF5N2pXVDNEdnVhM1J6a25SUGhHZjglM0Q6VVN1S0dCRVV"
                "ET0F2OE5xY2xpbU9vaW9mQmJaZTExdUxKVHJKMFFMYng2SSUzRA",
        }

    @override
    def search_manga(self, form):
        url = f"{self.url}/search"
        params = {"q": form.search, "+": "Искать!", "fast-filter": "CREATION"}
        response = make_request(url, "POST", headers=self.headers, data=params, content_type="text")
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
                    mangas.append(Manga(manga_id, self.CATALOG_ID, name, ""))
        return mangas

    @override
    def get_chapters(self, manga: Manga):
        url = f"{self.url}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="text")
        chapters = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            chapters_list_item = soup.find("div", id="chapters-list")
            for chapter_item in chapters_list_item.findAll("tr", class_="item-row"):
                volume: str = chapter_item.get("data-vol")
                chapter_num: str = chapter_item.get("data-num")
                if chapter_num.isdigit():
                    chapter_as_num = int(chapter_num) / 10
                    if chapter_as_num.is_integer():
                        chapter_as_num = int(chapter_as_num)
                    chapter_num = str(chapter_as_num)

                chapter = Chapter(manga.content_id, self.CATALOG_ID, volume, chapter_num, "")
                chapter.language = Nl.Language.ru
                chapters.append(chapter)
        return chapters

    @override
    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url}/{manga.content_id}/vol{chapter.vol}/{chapter.ch}"
        response = get_html(url, headers=self.headers, cookies=self.cookies, content_type="text")
        images = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            pages_count = soup.find("span", class_="pages-count").text
            pages = int(pages_count) if pages_count.isdigit() else 499
            for i in range(1, pages+1):
                image = Image(str(i), i, f"{url}#page={i}")
                images.append(image)
        return images

    @override
    def get_image(self, image: Image):
        response = get_html(image.img, headers=self.headers, cookies=self.cookies, content_type="text")
        if response:
            soup = BeautifulSoup(response, "html.parser")
            image_elem = soup.find("img", id="mangaPicture")
            image_url = f"https:{image_elem.get('src')}"
            return get_html(image_url, headers=self.headers, cookies=self.cookies, content_type="content")

    @override
    def get_preview(self, manga: Manga):
        url = f"{self.url}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="text")
        if response:
            soup = BeautifulSoup(response, "html.parser")
            html_item = soup.find("img", class_="")
            if html_item:
                img_src = html_item.get("src")
                if img_src:
                    return get_html(img_src, content_type="content", headers=self.headers)

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/{manga.content_id}"
