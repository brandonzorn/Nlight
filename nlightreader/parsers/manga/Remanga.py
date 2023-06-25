import json

from bs4 import BeautifulSoup


from nlightreader.consts import URL_REMANGA_API, URL_REMANGA
from nlightreader.items import RequestForm, Manga, Chapter, Image
from nlightreader.parsers.catalogs_base import MangaCatalog
from nlightreader.utils.utils import get_html


class Remanga(MangaCatalog):
    CATALOG_ID = 6
    CATALOG_NAME = "ReManga"

    def __init__(self):
        super().__init__()
        self.url = URL_REMANGA
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
                manga = Manga(manga_id, self.CATALOG_ID, name, russian)
                manga.kind = kind
                manga.score = i.get('avg_rating')
                mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f'{self.url_api}/titles/{manga.content_id}'
        html = get_html(url, self.headers)
        chapters = []
        if html and html.status_code == 200 and html.json():
            data = html.json().get('content')
            branch_id = data.get('branches')[0].get('id')
            page = 1
            while True:
                chapters_data = get_html(f'{self.url_api}/titles/chapters/?branch_id={branch_id}&count=40&page={page}')
                if not (chapters_data and chapters_data.status_code == 200 and chapters_data.json()):
                    break
                data = chapters_data.json().get('content')
                if not data:
                    break
                for ch in data:
                    if ch.get('is_paid'):
                        continue
                    chapter = Chapter(ch.get('id'), self.CATALOG_ID,
                                      str(ch.get('tome')), ch.get('chapter'), ch.get('name'), 'ru')
                    chapters.append(chapter)
                page += 1
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f'{self.url}/manga/{manga.content_id}/{chapter.content_id}'
        html = get_html(url, self.headers)
        images = []
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            script = soup.find("script", {'id': "__NEXT_DATA__", 'type': "application/json"})
            site_json = json.loads(script.text)
            pages_data = site_json['props']['pageProps']['fallbackData']['chapter']['content']["pages"]
            if pages_data:
                for i in pages_data:
                    i = i[0]
                    images.append(Image(i.get("id"), i.get("page"), i.get("link")))
        return images

    def get_image(self, image: Image):
        headers = {'Referer': f'{self.url}/manga/'}
        response = get_html(image.img, headers=headers, content_type='content')
        return response

    def get_preview(self, manga: Manga):
        url = f'{self.url_api}/titles/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            img = html.json().get('content').get('img').get('high')
            response = get_html(f"{self.url}/{img}", content_type='content')
            return response
