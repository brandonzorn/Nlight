import validators
from bs4 import BeautifulSoup, element

from nlightreader.consts.urls import URL_NHENTAI
from nlightreader.exceptions import parser_content_exc
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractHentaiMangaCatalog
from nlightreader.utils.utils import get_html


class NHentai(AbstractHentaiMangaCatalog):
    CATALOG_ID = 7
    CATALOG_NAME = "NHentai"

    def __init__(self):
        super().__init__()
        self.url = URL_NHENTAI

    def search_manga(self, form):
        url = f"{self.url}/search"
        if not form.search:
            raise parser_content_exc.RequestsParamsError(
                "Search field is empty",
            )
        params = {
            "page": form.page,
            "q": form.search,
        }
        response = get_html(
            url,
            headers=self.headers,
            params=params,
            content_type="text",
        )

        mangas = []
        if not response:
            return mangas

        soup = BeautifulSoup(response, "html.parser")
        html_items = soup.findAll("div", class_="gallery")
        for i in html_items:
            caption_tag = i.find("div", class_="caption")
            if caption_tag is not None:
                name = i.find("div", class_="caption").text
                cover_tag: element.Tag = i.find("a", {"class": "cover"})
                if cover_tag is not None:
                    manga_id = cover_tag["href"].split("/")[-2]
                    if not manga_id:
                        continue

                    manga = Manga(
                        manga_id,
                        self.CATALOG_ID,
                        name,
                        "",
                    )

                    if (noscript_img_tag := cover_tag.find("noscript")) and (
                        img_tag := noscript_img_tag.find("img")
                    ):
                        src = img_tag.get("src")
                        if validators.url(src):
                            manga.preview_url = src
                    mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga):
        return [
            Chapter(
                manga.content_id,
                self.CATALOG_ID,
                "1",
                "1",
                "",
            ),
        ]

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url}/g/{manga.content_id}"
        images = []
        response = get_html(url, headers=self.headers, content_type="text")
        if response:
            soup = BeautifulSoup(response, "html.parser")
            html_items = soup.findAll("a", class_="gallerythumb")
            for i in html_items:
                img_tag = i.find("img")
                img_url: str = img_tag.get("data-src")
                if not validators.url(img_url):
                    continue
                images.append(Image("", html_items.index(i) + 1, img_url))
        return images

    def get_image(self, image: Image):
        img_request_headers = self.headers | {
            "Referer": URL_NHENTAI,
        }
        return get_html(
            image.url,
            headers=img_request_headers,
            content_type="content",
        )

    def get_preview(self, manga: Manga):
        return get_html(
            manga.preview_url,
            headers=self.headers,
            content_type="content",
        )

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/g/{manga.content_id}"


__all__ = [
    "NHentai",
]
