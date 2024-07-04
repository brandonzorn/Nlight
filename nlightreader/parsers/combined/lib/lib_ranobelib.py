import base64
import re

from nlightreader.consts.enums import Nl
from nlightreader.consts.items import RanobeLibItems
from nlightreader.consts.urls import URL_RANOBELIB
from nlightreader.items import Manga, Chapter, Image
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase
from nlightreader.utils.utils import get_html


class LibRanobelib(LibBase, AbstractRanobeCatalog):
    CATALOG_NAME = "RanobeLib"
    CATALOG_ID = 13

    def __init__(self):
        super().__init__()
        self.url = URL_RANOBELIB
        self.items = RanobeLibItems

        self.content_name = "manga"
        self.site_id = 3

    def get_manga(self, manga: Manga) -> Manga:
        manga.kind = Nl.MangaKind.ranobe
        return super().get_manga(manga)

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self.url_api}/{self.content_name}/{manga.content_id}/"
            f"chapter?number={chapter.ch}&volume={chapter.vol}"
        )
        return [Image("", 1, url)]

    def get_image(self, image: Image):
        # Function to get content images from chapter
        def get_chapter_content_image(media_id: str):
            url = media_id if media_id.startswith(
                "http",
            ) else f"{self.url}{media_id}"
            chapter_image = get_html(
                url, headers=self.headers,
            ).content
            str_equivalent_image = base64.b64encode(chapter_image).decode()
            return f"data:image/png;base64,{str_equivalent_image}"

        def replace_images(text: str):
            pattern = r'src="([^"]+)"'
            return re.sub(
                pattern,
                lambda x: f'src="{get_chapter_content_image(x.group(1))}"',
                text,
            )

        response = get_html(image.img, content_type="json")
        if response:
            data = response["data"]
            content = data["content"]
            if isinstance(content, str):
                content = content.replace("\n", "")
                content = content.replace("\r", "")
            return replace_images(content)

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/ru/book/{manga.content_id}"
