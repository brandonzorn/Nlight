from const import DESU_HEADERS, URL_DESU_API, manga_desu_genres
from items import Manga, Chapter, Image, Genre
from static import get_html


class Desu:
    def __init__(self):
        self.url_api = URL_DESU_API
        self.headers = DESU_HEADERS
        self.catalog_id = 0

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def search_manga(self, params: dict) -> [Manga]:
        url = f'{self.url_api}'
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

    def get_genres(self):
        return [Genre({'name': i['en'], 'russian': i['ru']}) for i in manga_desu_genres]
