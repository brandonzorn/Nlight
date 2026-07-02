from typing import override

from nlightreader.consts.items import MangaLibItems
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase


class LibMangalib(LibBase, AbstractMangaCatalog):
    CATALOG_NAME = "MangaLib"
    CATALOG_ID = 10
    _FILTERS = MangaLibItems
    _URL = "https://mangalib.me"
    _DEFAULT_IMG_HOST = "https://img2.imglib.info"

    _CONTENT_NAME = "manga"
    _SITE_ID = 1

    @override
    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}/chapter"
        )
        params = {
            "number": chapter.chapter_number,
            "volume": chapter.volume_number,
        }

        response = self._client.get_json(url, params=params)
        images: list[Image] = []

        if not isinstance(response, dict):
            return images

        data = response.get("data", {})
        for i, page_data in enumerate(data.get("pages", [])):
            if not isinstance(page_data, dict):
                continue
            page_url = page_data.get("url")
            if not page_url:
                continue

            full_url = f"{self._DEFAULT_IMG_HOST}{page_url}"
            images.append(
                Image(
                    content_id=page_data["id"],
                    page_number=i + 1,
                    url=full_url,
                ),
            )
        return images

    @override
    def get_image(self, image: Image) -> bytes | None:
        image_response = self._client.get_bytes(image.url)
        if not isinstance(image_response, bytes):
            return None
        return image_response

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/ru/manga/{manga.content_id}"


__all__ = ["LibMangalib"]
