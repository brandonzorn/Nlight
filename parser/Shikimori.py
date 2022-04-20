from const import SHIKIMORI_HEADERS, URL_SHIKIMORI_API
from items import Manga, Chapter, Image, Genre
from parser.Parser import Parser
from static import get_html


class Shikimori(Parser):
    def __init__(self):
        super().__init__()
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/mangas/{manga.shikimori_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and len(html.json()):
            return Manga(html.json())
        return manga

    def search_manga(self, params: dict) -> [Manga]:
        url = f'{self.url_api}/mangas'
        html = get_html(url, self.headers, params)
        if html and html.status_code == 200 and len(html.json()):
            return [Manga(i) for i in html.json()]
        return []

    def get_chapters(self, manga: Manga) -> [Chapter]:
        pass

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        pass

    def get_image(self, image: Image):
        pass

    def get_preview(self, manga: Manga):
        pass

    def get_genres(self):
        url = f'{self.url_api}/genres'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and len(html.json()):
            return [Genre(i) for i in html.json()]
        return []
