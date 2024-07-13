from nlightreader.consts.items import MangaLibItems
from nlightreader.consts.urls import URL_MANGALIB
from nlightreader.items import Chapter, Image
from nlightreader.models import Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase
from nlightreader.utils.utils import get_html


class LibMangalib(LibBase, AbstractMangaCatalog):
    CATALOG_NAME = "MangaLib"
    CATALOG_ID = 10

    def __init__(self):
        super().__init__()
        self.url = URL_MANGALIB
        self.items = MangaLibItems

        self.content_name = "manga"
        self.site_id = 1

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = f"{self.url_api}/{self.content_name}/{manga.content_id}/chapter"
        params = {
            "number": chapter.ch,
            "volume": chapter.vol,
        }
        response = get_html(url, params=params, content_type="json")
        images = []
        if response:
            data = response["data"]
            for i, page_data in enumerate(data.get("pages", [])):
                images.append(
                    Image(
                        page_data["id"],
                        i + 1,
                        f"https://img33.imgslib.link{page_data['url']}",
                    ),
                )
        return images

    def get_image(self, image: Image):
        return get_html(image.img, content_type="content")

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/ru/manga/{manga.content_id}"
