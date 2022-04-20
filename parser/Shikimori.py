from const import SHIKIMORI_HEADERS, URL_SHIKIMORI_API
from items import Manga, Chapter, Image
from parser.Parser import Parser


class Shikimori(Parser):
    def __init__(self):
        super().__init__()
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS

    def get_manga(self, manga) -> Manga:
        pass

    def search_manga(self, params: dict) -> [Manga]:
        pass

    def get_chapters(self, manga: Manga) -> [Chapter]:
        pass

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        pass

    def get_image(self, image: Image):
        pass

    def get_preview(self, manga: Manga):
        pass
