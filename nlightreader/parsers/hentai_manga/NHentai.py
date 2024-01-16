from bs4 import BeautifulSoup

from nlightreader.consts import URL_NHENTAI, URL_NHENTAI_API
from nlightreader.items import Manga, Chapter, Image
from nlightreader.parsers.catalogs_base import HentaiMangaCatalog
from nlightreader.utils.utils import get_html


class NHentai(HentaiMangaCatalog):
    CATALOG_ID = 7
    CATALOG_NAME = "NHentai"

    def __init__(self):
        super().__init__()
        self.url = URL_NHENTAI
        self.url_api = URL_NHENTAI_API

    def search_manga(self, form):
        url = f"{self.url}/search"
        params = {"page": form.page, "q": form.search}
        response = get_html(url, headers=self.headers, params=params, content_type="text")
        mangas = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            html_items = soup.findAll("div", class_="gallery")
            for i in html_items:
                caption_tag = i.find("div", class_="caption")
                if caption_tag is not None:
                    name = i.find("div", class_="caption").text
                    cover_tag = i.find("a", {"class": "cover"})
                    if cover_tag is not None:
                        manga_id = cover_tag["href"].split("/")[-2]
                        if not manga_id:
                            continue
                        mangas.append(Manga(manga_id, self.CATALOG_ID, name, ""))
        return mangas

    def get_chapters(self, manga: Manga):
        return [Chapter(manga.content_id, self.CATALOG_ID, "1", "1", "")]

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url}/g/{manga.content_id}"
        images = []
        response = get_html(url, headers=self.headers, content_type="text")
        if response:
            soup = BeautifulSoup(response, "html.parser")
            html_items = soup.findAll("a", class_="gallerythumb")
            for i in html_items:
                img_tag = i.find("img", class_="")
                img_url: str = img_tag["src"]
                for img_format in ["png", "jpg", "gif"]:
                    if img_url.endswith(f"t.{img_format}"):
                        img_url = img_url.replace(f"t.{img_format}", f".{img_format}", 1)
                        break
                images.append(Image("", html_items.index(i) + 1, img_url))
        return images

    def get_image(self, image: Image):
        img_request_headers = self.headers | {"Referer": URL_NHENTAI}
        return get_html(image.img, headers=img_request_headers, content_type="content")

    def get_preview(self, manga: Manga):
        url = f"{self.url}/g/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="text")
        if response:
            soup = BeautifulSoup(response, "html.parser")
            html_item = soup.find("div", id="cover")
            if html_item:
                img_tag = html_item.find("img")
                if img_tag:
                    img_request_headers = self.headers | {"Referer": URL_NHENTAI}
                    return get_html(img_tag["src"], content_type="content", headers=img_request_headers)

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/g/{manga.content_id}"
