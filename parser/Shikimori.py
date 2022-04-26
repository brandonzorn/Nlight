from const import SHIKIMORI_HEADERS, URL_SHIKIMORI_API
from items import Manga, Chapter, Image, Genre, RequestForm
from static import get_html


class Shikimori:
    def __init__(self):
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS
        self.catalog_id = 1

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/mangas/{manga.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and len(html.json()):
            m = Manga(html.json())
            m.catalog_id = self.catalog_id
            return m
        return manga

    def search_manga(self, params: RequestForm) -> [Manga]:
        url = f'{self.url_api}/mangas'
        params = {'limit': params.limit, 'search': params.search, 'genre': ','.join([i.id for i in params.genres]),
                  'order': 'popularity', 'kind': ','.join(params.kinds), 'page': params.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json():
                data = i
                data.update({'catalog_id': self.catalog_id})
                manga.append(Manga(data))
        return manga

    def get_chapters(self, manga: Manga) -> [Chapter]:
        return []

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        return []

    def get_image(self, image: Image):
        pass

    def get_preview(self, manga: Manga):
        return get_html(f'https://shikimori.one/system/mangas/preview/{manga.id}.jpg')

    def get_genres(self):
        url = f'{self.url_api}/genres'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and len(html.json()):
            return [Genre(i) for i in html.json()]
        return []
