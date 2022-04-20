from const import DEFAULT_HEADERS
from items import Manga, Chapter, Image


class Parser:
    def __init__(self):
        self.url_api = ''
        self.headers = DEFAULT_HEADERS

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
