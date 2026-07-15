from bs4 import BeautifulSoup, element
import validators

from nlightreader.core.exceptions import parser_content_exc
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractHentaiMangaCatalog
from nlightreader.utils.network import NetworkClient


class NHentai(AbstractHentaiMangaCatalog):
    CATALOG_ID = 7
    CATALOG_NAME = "NHentai"
    _URL = "https://nhentai.net"

    def __init__(self) -> None:
        self._client = NetworkClient(
            catalog_name=self.CATALOG_NAME,
            headers=self._HEADERS,
        )

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL}/search"
        if not form.search:
            msg = "Search field is empty"
            raise parser_content_exc.RequestsParamsError(msg)
        params = {
            "page": form.page,
            "q": form.search,
        }
        response = self._client.get_text(url, params=params)

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
                content_id=manga_id,
                catalog_id=self.CATALOG_ID,
                name=name,
                russian="",
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
                content_id=manga.content_id,
                catalog_id=self.CATALOG_ID,
                volume_number="1",
                chapter_number="1",
                title="",
            ),
        ]

    def get_images(self, manga: Manga, _) -> list[Image]:
        url = f"{self._URL}/g/{manga.content_id}"
        images: list[Image] = []
        response = self._client.get_text(url)
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
                    content_id="",
                    page_number=html_items.index(i) + 1,
                    url=img_url,
                ),
            )
        return images

    def get_image(self, image: Image) -> bytes | None:
        get_img_headers = {"Referer": self._URL}
        url = image.url
        if url is None:
            return None
        return self._client.get_bytes(url, extra_headers=get_img_headers)

    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(url)

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/g/{manga.content_id}"


__all__ = [
    "NHentai",
]
