import requests

from nlightreader.consts import URL_MANGA_DEX_API, URL_MANGA_DEX, LibList
from nlightreader.items import Manga, Chapter, Image, Genre, RequestForm, User, Kind
from nlightreader.parsers.Parser import Parser, LibParser
from nlightreader.utils.decorators import singleton
from nlightreader.utils.token import TokenManager
from nlightreader.utils.utils import get_data, get_html


class MangaDex(Parser):
    catalog_name = 'MangaDex'

    def __init__(self):
        super().__init__()
        self.url = URL_MANGA_DEX
        self.url_api = URL_MANGA_DEX_API
        self.catalog_id = 2

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/manga/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = get_data(html.json(), ['data'])
            manga.kind = data.get('type')
            description = get_data(data, ['attributes', 'description'])
            if description:
                manga.description.update({'en': description.get('en')})
                if description.get('ru'):
                    manga.description.update({'ru': description.get('ru')})
            volumes = get_data(data, ['attributes', 'lastVolume'])
            chapters = get_data(data, ['attributes', 'lastChapter'])
            if volumes:
                manga.volumes = volumes
            if chapters:
                manga.chapters = chapters
            manga.status = get_data(data, ['attributes', 'status'])
        return manga

    def setup_manga(self, data: dict):
        manga_id = str(data.get('id'))
        name = get_data(data, ['attributes', 'title', 'en'])
        russian = None
        alt_titles = get_data(data, ['attributes', 'altTitles'])
        for j in alt_titles:
            if 'ru' in j.keys():
                russian = j.get('ru')
            if not name and 'en' in j.keys():
                name = j.get('en')
        return Manga(manga_id, self.catalog_id, name, russian)

    def search_manga(self, form: RequestForm):
        url = f'{self.url_api}/manga'
        params = {'limit': 50, 'title': form.search, 'offset': form.offset,
                  'includedTags[]': form.get_genre_id() + form.get_kind_id()}
        mangas = []
        html = get_html(url, self.headers, params)
        if html and html.status_code == 200 and html.json():
            for i in get_data(html.json(), ['data']):
                mangas.append(self.setup_manga(i))
        return mangas

    def get_chapters(self, manga: Manga):
        url = f'{self.url_api}/chapter'
        params = {'manga': manga.content_id, 'limit': 1, 'translatedLanguage[]': ['ru', 'en'], 'order[chapter]': 'asc'}
        html = get_html(url, self.headers, params)
        chapters = []
        if html and html.status_code == 200 and html.json():
            params.update({'limit': 100})
            for j in range(html.json().get('total') // 100 + 1):
                params.update({'offset': j * 100})
                html = get_html(url, self.headers, params)
                for i in get_data(html.json(), ['data']):
                    attr = i.get('attributes')
                    chapters.append(Chapter(i.get('id'), self.catalog_id, attr.get('volume'), attr.get('chapter'),
                                            attr.get('title'), attr.get('translatedLanguage')))
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f'{self.url_api}/at-home/server/{chapter.content_id}'
        response = get_html(url, self.headers, content_type='json')
        images = []
        if response:
            image_hash = response.get('chapter').get('hash')
            for img_data in get_data(response, ['chapter', 'data']):
                img_url = f'https://uploads.mangadex.org/data/{image_hash}/{img_data}'
                page = response.get('chapter').get('data').index(img_data) + 1
                images.append(Image('', page, img_url))
        return images

    def get_image(self, image: Image):
        response = get_html(image.img, content_type='content')
        return response

    def get_preview(self, manga: Manga):
        url = f'{self.url_api}/cover'
        params = {'manga[]': manga.content_id}
        html = get_html(url, self.headers, params)
        filename = ''
        if html and html.status_code == 200 and len(html.json()):
            filename = html.json().get('data')[0].get('attributes').get('fileName')
        response = get_html(f'https://uploads.mangadex.org/covers/{manga.content_id}/{filename}.256.jpg',
                            content_type='content')
        return response

    def get_genres(self):
        url = f'{self.url_api}/manga/tag'
        html = get_html(url, headers=self.headers)
        genres = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('data'):
                if i.get('attributes').get('group') not in ['genre', 'theme']:
                    continue
                genres.append(Genre(i.get('id'), self.catalog_id, get_data(i, ['attributes', 'name', 'en']), ''))
        return genres

    def get_kinds(self):
        url = f'{self.url_api}/manga/tag'
        html = get_html(url, headers=self.headers)
        kinds = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('data'):
                if i.get('attributes').get('group') not in ['format']:
                    continue
                kinds.append(Kind(i.get('id'), self.catalog_id, i.get('attributes').get('name').get('en'), ''))
        return kinds

    def get_manga_url(self, manga: Manga) -> str:
        return f'{self.url}/title/{manga.content_id}'


class MangaDexLib(MangaDex, LibParser):
    def __init__(self):
        super().__init__()
        self.fields = 2
        self.session = Auth()

    def search_manga(self, form: RequestForm):
        mangas = []
        match form.lib_list:
            case LibList.planned:
                lib_list = 'plan_to_read'
            case _:
                lib_list = form.lib_list.name
        html_statuses = self.session.get(f'{self.url_api}/manga/status', params={'status': lib_list})
        params = {'limit': form.limit, 'offset': form.offset}
        html = self.session.get(f'{self.url_api}/user/follows/manga', params=params)
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('data'):
                manga = self.setup_manga(i)
                if manga.content_id in html_statuses.json().get('statuses'):
                    mangas.append(manga)
        return mangas

    def get_user(self):
        whoami = self.session.get(f'{self.url_api}/user/me')
        if whoami and whoami.status_code == 200:
            data = whoami.json().get('data')
            return User(data.get('id'), data.get('attributes').get('username'), '')
        return User(None, None, None)


@singleton
class Auth:
    def __init__(self):
        self.url_api = URL_MANGA_DEX_API
        self.tokens = TokenManager.load_token(MangaDex.catalog_name)
        self.is_authorized = False

    def get_refresh(self):
        if self.check_token():
            return self.token.get('refresh')

    def check_token(self) -> bool:
        if not self.tokens:
            return False
        return True

    def check_auth(self):
        response = get_html(f'{self.url_api}/auth/check', headers=self.headers)
        if response.status_code and response.json():
            self.is_authorized = response.json().get('isAuthenticated')
            return response.json().get('isAuthenticated')
        self.is_authorized = False
        return False

    def update_token(self, token):
        if token:
            token = token.json().get('token')
            TokenManager.save_token(token, MangaDex.catalog_name)
            self.tokens = token

    def refresh_token(self):
        token = requests.post(f'{self.url_api}/auth/refresh', json={"token": self.get_refresh()})
        match token.status_code:
            case 200:
                self.update_token(token)

    def auth_login(self, params):
        token = requests.post(f"{self.url_api}/auth/login", json=params)
        match token.status_code:
            case 200:
                self.update_token(token)

    def get(self, url, params=None):
        if self.check_auth():
            response = get_html(url, params=params, headers=self.headers)
            return response

    @property
    def token(self):
        if self.check_token():
            if self.check_auth():
                return self.tokens.get('session')
            else:
                self.refresh_token()

    @property
    def headers(self):
        return {'Authorization': self.tokens.get('session')}
