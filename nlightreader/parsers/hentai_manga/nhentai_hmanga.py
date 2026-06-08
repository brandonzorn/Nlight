from bs4 import BeautifulSoup, element
import validators

from nlightreader.exceptions import parser_content_exc
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractHentaiMangaCatalog
from nlightreader.utils.utils import get_html


class NHentai(AbstractHentaiMangaCatalog):
    CATALOG_ID = 7
    CATALOG_NAME = "NHentai"
    _URL = "https://nhentai.net"

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL}/search"
        if not form.search:
            msg = "Search field is empty"
            raise parser_content_exc.RequestsParamsError(
                msg,
            )
        params = {
            "page": form.page,
            "q": form.search,
        }
        response = get_html(
            url,
            headers=self._HEADERS,
            params=params,
            content_type="text",
        )

        mangas: list[Manga] = []
        if not isinstance(response, str):
            return mangas

        soup = BeautifulSoup(response, "html.parser")
        html_items = soup.find_all("div", class_="gallery")
        for i in html_items:
            caption_tag = i.find("div", class_="caption")
            if caption_tag is None:
                continue
            name = i.find("div", class_="caption").text
            cover_tag: element.Tag = i.find("a", {"class": "cover"})
            if cover_tag is None:
                continue
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
                if isinstance(src, str) and validators.url(src):
                    manga.preview_url = src
            mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        return [
            Chapter(
                manga.content_id,
                self.CATALOG_ID,
                "1",
                "1",
                "",
            ),
        ]

    def get_images(self, manga: Manga, _) -> list[Image]:
        url = f"{self._URL}/g/{manga.content_id}"
        images: list[Image] = []
        response = get_html(url, headers=self._HEADERS, content_type="text")
        if not isinstance(response, str):
            return images
        soup = BeautifulSoup(response, "html.parser")
        html_items = soup.find_all("a", class_="gallerythumb")
        for i in html_items:
            img_tag = i.find("img")
            img_url = img_tag.get("data-src")
            if not isinstance(img_url, str) or not validators.url(img_url):
                continue
            images.append(
                Image(
                    "",
                    html_items.index(i) + 1,
                    img_url,
                ),
            )
        return images

    def get_image(self, image: Image) -> bytes | None:
        img_request_headers = self._HEADERS | {
            "Referer": self._URL,
        }
        image_response = get_html(
            image.url,
            headers=img_request_headers,
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
        return f"{self._URL}/g/{manga.content_id}"


__all__ = [
    "NHentai",
]
