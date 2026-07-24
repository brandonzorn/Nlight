from typing import override

from bs4 import BeautifulSoup
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
            headers=self._HEADERS | {"Referer": self._URL},
        )

    @override
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
            name_tag = i.find("div", class_="caption")
            if name_tag is None:
                continue
            name = name_tag.text
            cover_tag = i.find("a", {"class": "cover"})
            if cover_tag is None:
                continue
            manga_href = cover_tag["href"]
            if not isinstance(manga_href, str):
                continue
            manga_id = manga_href.split("/")[-2]

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

    @override
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

    @override
    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = f"{self._URL}/g/{manga.content_id}"
        images: list[Image] = []
        response = self._client.get_text(url)
        if not isinstance(response, str):
            return images
        soup = BeautifulSoup(response, "html.parser")
        html_items = soup.find_all("a", class_="gallerythumb")
        for i in html_items:
            img_tag = i.find("img")
            if img_tag is None:
                continue
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

    @override
    def get_image(self, image: Image) -> bytes | None:
        url = image.url
        if url is None:
            return None
        return self._client.get_bytes(url)

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(url)

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/g/{manga.content_id}"


__all__ = ["NHentai"]
