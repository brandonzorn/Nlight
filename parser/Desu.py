from const import DESU_HEADERS, URL_DESU_API, manga_desu_genres, manga_desu_kinds, manga_desu_orders
from items import Manga, Chapter, Image, Genre, RequestForm, Kind, Order
from parser.Parser import Parser
from utils import get_html


class Desu(Parser):
    catalog_name = 'Desu'

    def __init__(self):
        self.url_api = URL_DESU_API
        self.headers = DESU_HEADERS
        self.catalog_id = 0

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def search_manga(self, params: RequestForm) -> [Manga]:
        url = f'{self.url_api}'
        params = {'limit': params.limit, 'search': params.search, 'genres': ','.join([i.name for i in params.genres]),
                  'order': params.order, 'kinds': ','.join(params.kinds), 'page': params.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json().get('response'):
                data = i
                data.update({'catalog_id': self.catalog_id})
                manga.append(Manga(data))
        return manga

    def get_chapters(self, manga: Manga) -> [Chapter]:
        url = f'{self.url_api}/{manga.id}'
        html = get_html(url, self.headers)
        chapters = []
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json().get('response').get('chapters').get('list'):
                data = i
                data.update({'language': 'ru'})
                chapters.append(Chapter(data))
        return chapters

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

    def get_genres(self):
        return [Genre({'name': i['en'], 'russian': i['ru']}) for i in manga_desu_genres]

    def get_kinds(self) -> list[Kind]:
        return [Kind({'name': i['en'], 'russian': i['ru']}) for i in manga_desu_kinds]

    def get_orders(self) -> list[Order]:
        return [Order({'name': i['en'], 'russian': i['ru']}) for i in manga_desu_orders]
