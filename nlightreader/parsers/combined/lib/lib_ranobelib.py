import base64
import re
from typing import override

from nlightreader.consts.enums import Nl
from nlightreader.consts.items import RanobeLibItems
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase
from nlightreader.utils.utils import get_html


class LibRanobelib(LibBase, AbstractRanobeCatalog):
    CATALOG_NAME = "RanobeLib"
    CATALOG_ID = 13
    _FILTERS = RanobeLibItems
    _URL = "https://ranobelib.me"

    _CONTENT_NAME = "manga"
    _SITE_ID = 3

    @override
    def get_manga(self, manga: Manga) -> Manga:
        manga.kind = Nl.MangaKind.ranobe
        return super().get_manga(manga)

    @override
    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}/chapter"
            f"?number={chapter.chapter_number}"
            f"&volume={chapter.volume_number}"
        )
        return [Image("", 1, url)]

    @override
    def get_image(self, image: Image) -> str | None:
        def get_chapter_content_image(media_id: str) -> str:
            url = (
                media_id
                if media_id.startswith(
                    "http",
                )
                else f"{self._URL}{media_id}"
            )
            chapter_image = get_html(
                url,
                headers=self._HEADERS,
            ).content
            str_equivalent_image = base64.b64encode(chapter_image).decode()
            return f"data:image/png;base64,{str_equivalent_image}"

        def replace_images(text: str) -> str:
            pattern = r'src=["\']([^"\']+)["\']'
            return re.sub(
                pattern,
                lambda x: f'src="{get_chapter_content_image(x.group(1))}"',
                text,
            )

        response = get_html(image.url, content_type="json")
        if not isinstance(response, dict):
            return None
        content_data = response.get("data", {}).get("content")

        if not isinstance(content_data, str):
            return None
        content_data = content_data.replace("\n", " ").replace("\r", " ")
        return replace_images(content_data)

    @override
    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/ru/book/{manga.content_id}"


__all__ = [
    "LibRanobelib",
]
