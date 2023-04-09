from nlightreader.consts import URL_REMANGA_API, URL_REMANGA
from nlightreader.items import RequestForm, Manga, Chapter
from nlightreader.parsers.Parser import Parser
from nlightreader.utils.utils import get_html


class Remanga(Parser):
    catalog_name = "ReManga"

    def __init__(self):
        super().__init__()
        self.catalog_id = 6
        self.url_api = URL_REMANGA_API

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/titles/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = html.json().get('content')
            manga.description.update({'all': data.get('description')})
        return manga

    def search_manga(self, form: RequestForm):
        url = f'{self.url_api}/search'
        if not form.search:
            url = f'{self.url_api}/titles'
        params = {'page': form.page, 'query': form.search, 'count': 40}
        html = get_html(url, self.headers, params)
        mangas = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('content'):
                manga_id = i.get('dir')
                name = i.get('en_name')
                russian = i.get('rus_name')
                kind = i.get('type')
                manga = Manga(manga_id, self.catalog_id, name, russian)
                manga.kind = kind
                manga.score = i.get('avg_rating')
                mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        return []

    def get_preview(self, manga: Manga):
        url = f'{self.url_api}/titles/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            img = html.json().get('content').get('img').get('high')
            return get_html(f"{URL_REMANGA}/{img}").content
