from const import MANGA_DEX_HEADERS, URL_MANGA_DEX_API, DEFAULT_HEADERS
from items import Manga, Chapter, Image, Genre, RequestForm
from parser.Parser import Parser
from static import get_html


class MangaDex(Parser):
    catalog_name = 'MangaDex'

    def __init__(self):
        self.url_api = URL_MANGA_DEX_API
        self.headers = DEFAULT_HEADERS
        self.catalog_id = 2

    def get_manga(self, manga: Manga) -> Manga:
        pass

    def search_manga(self, params: RequestForm) -> [Manga]:
        url = f'{self.url_api}/manga'
        params = {'limit': 50, 'title': params.search, 'offset': params.offset(),
                  'includedTags[]': [i.id for i in params.genres]}
        manga = []
        html = get_html(url, self.headers, params)
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json().get('data'):
                id = i.get('id')
                kind = i.get('type')
                name = i.get('attributes').get('title').get('en')
                russian = None
                if i.get('attributes').get('altTitles'):
                    for j in i.get('attributes').get('altTitles'):
                        if 'ru' in j.keys():
                            russian = j.get('ru')
                        if not name and 'en' in j.keys():
                            name = j.get('en')
                description = i.get('attributes').get('description')
                if description:
                    if description.get('ru'):
                        description = description.get('ru')
                    else:
                        description = description.get('en')
                else:
                    description = None
                data = {'id': id, 'kind': kind, 'name': name, 'russian': russian, 'description': description}
                data.update({'catalog_id': self.catalog_id})
                manga.append(Manga(data))
        return manga

    def get_chapters(self, manga: Manga) -> [Chapter]:
        url = f'{self.url_api}/chapter'
        params = {'manga': manga.id, 'limit': 1, 'translatedLanguage[]': ['ru']}
        html = get_html(url, self.headers, params)
        chapters = []
        if html and html.status_code == 200 and len(html.json()):
            params.update({'limit': 100})
            for j in range(html.json().get('total') // 100 + 1):
                params.update({'offset': j * 100})
                html = get_html(url, self.headers, params)
                for i in html.json().get('data'):
                    attr = i.get('attributes')
                    data = {'id': i.get('id'), 'vol': attr.get('volume'), 'ch': attr.get('chapter'),
                            'title': attr.get('title')}
                    chapters.append(Chapter(data))
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        url = f'{self.url_api}/at-home/server/{chapter.id}'
        html = get_html(url, self.headers)
        images = []
        if html and html.status_code == 200 and len(html.json()):
            hash = html.json().get('chapter').get('hash')
            for i in html.json().get('chapter').get('data'):
                i = str(i)
                data = {'hash': hash, 'page': html.json().get('chapter').get('data').index(i) + 1, 'img': i}
                images.append(Image(data))
        return images

    def get_image(self, image: Image):
        return get_html(f'https://uploads.mangadex.org/data/{image.hash}/{image.img}')

    def get_preview(self, manga: Manga):
        url = f'{self.url_api}/cover'
        params = {'manga[]': manga.id}
        html = get_html(url, self.headers, params)
        filename = ''
        if html and html.status_code == 200 and len(html.json()):
            filename = html.json().get('data')[0].get('attributes').get('fileName')
        return get_html(f'https://uploads.mangadex.org/covers/{manga.id}/{filename}.256.jpg')

    def get_genres(self):
        url = f'{self.url_api}/manga/tag'
        html = get_html(url, headers=self.headers)
        genres = []
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json().get('data'):
                if i.get('attributes').get('group') not in ['genre', 'theme']:
                    continue
                data = {'id': i.get('id'), 'name': i.get('attributes').get('name').get('en'), }
                genres.append(Genre(data))
        return genres
