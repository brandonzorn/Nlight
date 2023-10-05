from nlightreader.consts import URL_REMANGA_API, URL_REMANGA
from nlightreader.consts.items import RemangaItems
from nlightreader.items import RequestForm, Manga, Chapter, Image
from nlightreader.parsers.catalogs_base import MangaCatalog
from nlightreader.utils.utils import get_html, get_data


class Remanga(MangaCatalog):
    CATALOG_ID = 6
    CATALOG_NAME = 'ReManga'

    def __init__(self):
        super().__init__()
        self.url = URL_REMANGA
        self.url_api = URL_REMANGA_API
        self.items = RemangaItems

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/titles/{manga.content_id}/'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = html.json().get('content')
            manga.description.update({'all': data.get('description')})
        return manga

    def search_manga(self, form: RequestForm):
        url = f'{self.url_api}/search/catalog'
        if form.search:
            url = f'{self.url_api}/search'
        params = {
            'page': form.page,
            'query': form.search,
            'count': 40,
            'ordering': form.order.content_id,
        }
        params = list(params.items())
        [params.append(('types', kind_id)) for kind_id in form.get_kind_id()]
        html = get_html(url, self.headers, params)
        mangas = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('content'):
                manga_id = i.get('dir')
                name = i.get('en_name')
                russian = i.get('rus_name')
                kind = i.get('type')
                manga = Manga(manga_id, self.CATALOG_ID, name, russian)
                manga.kind = kind
                manga.score = i.get('avg_rating')
                mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f'{self.url_api}/titles/{manga.content_id}/'
        html = get_html(url, self.headers)
        chapters = []
        if html and html.status_code == 200 and html.json():
            data = html.json().get('content')
            branch_id = data.get('branches')[0].get('id')
            chapters_data = get_html(
                f'{self.url_api}/titles/chapters?branch_id={branch_id}&user_data=0',
                headers=self.headers,
            )
            if (
                chapters_data
                and chapters_data.status_code == 200
                and chapters_data.json()
            ):
                data = chapters_data.json().get('content')
                if data:
                    for ch in data:
                        if ch.get('is_paid'):
                            continue
                        chapter = Chapter(
                            ch.get('id'),
                            self.CATALOG_ID,
                            str(ch.get('tome')),
                            ch.get('chapter'),
                            ch.get('name'),
                            'ru',
                        )
                        chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f'{self.url_api}/titles/chapters/{chapter.content_id}/'
        response = get_html(url, self.headers, content_type='json')
        images = []
        if response:
            for page_data in get_data(response, ['content', 'pages'], {}):
                page_data = page_data[0]
                pg_id = page_data.get('id')
                page = page_data.get('page')
                pg_link = page_data.get('link')
                images.append(Image(pg_id, page, pg_link))
        return images

    def get_image(self, image: Image):
        headers = {'User-Agent': 'Nlight', 'Referer': 'https://remanga.org/'}
        response = get_html(
            f'{image.img}', headers=headers, content_type='content'
        )
        return response

    def get_preview(self, manga: Manga):
        url = f'{self.url_api}/titles/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            img = html.json().get('content').get('img').get('high')
            response = get_html(
                f'{self.url}{img}',
                headers=self.headers,
                content_type='content',
            )
            return response

    def get_manga_url(self, manga: Manga) -> str:
        return f'{self.url}/manga/{manga.content_id}'
