from const import DESU_HEADERS, URL_DESU_API
from items import Manga, Chapter, Image
from parser.Parser import Parser
from static import get_html


class Desu(Parser):
    def __init__(self):
        super().__init__()
        self.url_api = URL_DESU_API
        self.headers = DESU_HEADERS

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def search_manga(self, params: dict) -> [Manga]:
        url = f'{self.url_api}'
        html = get_html(url, self.headers, params)
        if html and html.status_code == 200 and len(html.json()):
            return [Manga(i) for i in html.json().get('response')]
        return []

    def get_chapters(self, manga: Manga) -> [Chapter]:
        url = f'{self.url_api}/{manga.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and len(html.json()):
            return [Chapter(i) for i in html.json().get('response').get('chapters').get('list')]
        return []

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        url = f'{URL_DESU_API}/{manga.id}/chapter/{chapter.id}'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and len(html.json()):
            return [Image(i) for i in html.json().get('response').get('pages').get('list')]
        return []

    def get_image(self, image: Image):
        return get_html(image.img)

    def get_preview(self, manga: Manga):
        return get_html(f'https://desu.me/data/manga/covers/preview/{manga.id}.jpg')
