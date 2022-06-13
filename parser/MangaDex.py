import requests

from const import URL_MANGA_DEX_API, DEFAULT_HEADERS
from items import Manga, Chapter, Image, Genre, RequestForm, User
from parser.Parser import Parser
from static import get_html, token_loader, token_saver


class MangaDex(Parser):
    catalog_name = 'MangaDex'

    def __init__(self):
        self.url_api = URL_MANGA_DEX_API
        self.headers = DEFAULT_HEADERS
        self.catalog_id = 2
        self.fields = 2
        self.session = Auth()

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def setup_manga(self, data: dict):
        manga_id = data.get('id')
        kind = data.get('type')
        name = data.get('attributes').get('title').get('en')
        russian = None
        if data.get('attributes').get('altTitles'):
            for j in data.get('attributes').get('altTitles'):
                if 'ru' in j.keys():
                    russian = j.get('ru')
                if not name and 'en' in j.keys():
                    name = j.get('en')
        description = data.get('attributes').get('description')
        if description:
            if description.get('ru'):
                description = description.get('ru')
            else:
                description = description.get('en')
        else:
            description = None
        data = {'id': manga_id, 'kind': kind, 'name': name, 'russian': russian, 'description': description}
        data.update({'catalog_id': self.catalog_id})
        return Manga(data)

    def search_manga(self, params: RequestForm) -> [Manga]:
        url = f'{self.url_api}/manga'
        params = {'limit': 50, 'title': params.search, 'offset': params.offset(),
                  'includedTags[]': [i.id for i in params.genres]}
        manga = []
        html = get_html(url, self.headers, params)
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json().get('data'):
                manga.append(self.setup_manga(i))
        return manga

    def get_chapters(self, manga: Manga) -> [Chapter]:
        url = f'{self.url_api}/chapter'
        params = {'manga': manga.id, 'limit': 1, 'translatedLanguage[]': ['ru', 'en'], 'order[chapter]': 'asc'}
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
                            'title': attr.get('title'), 'language': attr.get('translatedLanguage')}
                    chapters.append(Chapter(data))
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        url = f'{self.url_api}/at-home/server/{chapter.id}'
        html = get_html(url, self.headers)
        images = []
        if html and html.status_code == 200 and len(html.json()):
            image_hash = html.json().get('chapter').get('hash')
            for i in html.json().get('chapter').get('data'):
                i = str(i)
                data = {'hash': image_hash, 'page': html.json().get('chapter').get('data').index(i) + 1, 'img': i}
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

    def get_manga_login(self, params: RequestForm):
        mangas = []
        match params.mylist:
            case 'planned':
                params.mylist = 'plan_to_read'
            case 'watching':
                params.mylist = 'reading'
            case 'rewatching':
                params.mylist = 're_reading'
        html_statuses = self.session.get(f'{self.url_api}/manga/status', params={'status': params.mylist})
        params = {'limit': params.limit, 'offset': params.offset()}
        html = self.session.get(f'{self.url_api}/user/follows/manga', params=params)
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json().get('data'):
                manga = self.setup_manga(i)
                if manga.id in html_statuses.json().get('statuses'):
                    mangas.append(manga)
        return mangas

    def get_user(self) -> User:
        whoami = self.session.get(f'{self.url_api}/user/me')
        user = User()
        match whoami.status_code:
            case 401:
                print(whoami.json())
            case 200:
                data = whoami.json().get('data')
                user.id = data.get('id')
                user.nickname = data.get('attributes').get('username')
        return user


class Auth:
    def __init__(self):
        self.url_api = URL_MANGA_DEX_API
        self.tokens = token_loader(MangaDex.catalog_name)
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
            token_saver(token, MangaDex.catalog_name)
            self.tokens = token

    def refresh_token(self):
        token = requests.post(f'{self.url_api}/auth/refresh', json={"token": self.get_refresh()})
        match token.status_code:
            case 200:
                self.update_token(token)
            case _:
                print(token.status_code)
                print(token.json())

    def auth_login(self, params):
        token = requests.post(f"{self.url_api}/auth/login", json=params)
        match token.status_code:
            case 200:
                self.update_token(token)
            case _:
                print(token.status_code)
                print(token.json())

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
