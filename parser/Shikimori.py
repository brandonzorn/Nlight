from oauthlib.oauth2.rfc6749.errors import InvalidGrantError
from requests_oauthlib import OAuth2Session

from const import SHIKIMORI_HEADERS, URL_SHIKIMORI_API
from const import URL_SHIKIMORI, URL_SHIKIMORI_TOKEN
from items import Manga, Chapter, Image, Genre, RequestForm, User, Kind
from keys import SHIKIMORI_CLIENT_ID, SHIKIMORI_CLIENT_SECRET
from parser.Parser import Parser
from utils import get_html
from utils import token_loader, token_saver


class Shikimori(Parser):
    catalog_name = 'Shikimori'

    def __init__(self):
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS
        self.catalog_id = 1
        self.fields = 1
        self.session = Auth()

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/mangas/{manga.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and len(html.json()):
            data = html.json()
            manga.description = data.get('description')
        return manga

    def search_manga(self, params: RequestForm):
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

    def get_chapters(self, manga: Manga):
        return []

    def get_images(self, manga: Manga, chapter: Chapter):
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

    def get_orders(self):
        pass

    def get_kinds(self):
        url = f'{self.url_api}/constants/manga'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and len(html.json()):
            return [Kind({'id': 0, 'name': i}) for i in html.json().get('kind')]
        return []

    def get_manga_login(self, params: RequestForm):
        url = f'{self.url_api}/mangas'
        params = {'limit': params.limit, 'page': params.page, 'mylist': params.mylist, 'search': params.search}
        html = self.session.get(url, params)
        manga = []
        if html and html.status_code == 200 and len(html.json()):
            for i in html.json():
                data = i
                data.update({'catalog_id': self.catalog_id})
                manga.append(Manga(data))
        return manga

    def get_user(self) -> User:
        whoami = self.session.get('https://shikimori.one/api/users/whoami')
        user = User()
        if whoami:
            match whoami.status_code:
                case 401:
                    print(whoami.json())
                case 200:
                    data = whoami.json()
                    user.id = data.get('id')
                    user.nickname = data.get('nickname')
                    user.avatar = data.get('avatar')
                    user.locale = data.get('locale')
        return user


class Auth:
    def __init__(self, token=None, scope=None):
        self.client_id = SHIKIMORI_CLIENT_ID
        self.client_secret = SHIKIMORI_CLIENT_SECRET
        self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
        self.extra = {'client_id': self.client_id, 'client_secret': self.client_secret}
        self.tokens = token_loader(Shikimori.catalog_name)
        self.headers = {'User-Agent': 'Shikimori', 'Authorization': f'Bearer {self.tokens.get("access_token")}'}
        self.client = self.get_client(scope, self.redirect_uri, token)
        self.is_authorized = False
        self.check_auth()

    def auth_login(self, data):
        pass

    def get_client(self, scope, redirect_uri, token):
        client = OAuth2Session(self.client_id, auto_refresh_url=URL_SHIKIMORI_TOKEN, auto_refresh_kwargs=self.extra,
                               scope=scope, redirect_uri=redirect_uri, token=token,
                               token_updater=token_saver)
        client.headers.update(self.headers)
        return client

    def get_auth_url(self):
        auth_url = URL_SHIKIMORI + '/oauth/authorize'
        return self.client.authorization_url(auth_url)[0]

    def fetch_token(self, code):
        try:
            self.client.fetch_token(URL_SHIKIMORI_TOKEN, code, client_secret=self.client_secret)
        except InvalidGrantError:
            return
        token_saver(self.token, Shikimori.catalog_name)
        return self.token

    def update_token(self, token):
        if token:
            token = token.get('token')
            token_saver(token, Shikimori.catalog_name)
            self.tokens = token

    def refresh_token(self):
        if not token_loader(Shikimori.catalog_name):
            return False
        self.client.headers.clear()
        self.client.headers.update({'User-Agent': 'Shikimori'})
        self.client.refresh_token(URL_SHIKIMORI_TOKEN,
                                  refresh_token=token_loader(Shikimori.catalog_name).get('refresh_token'))
        self.update_token(self.token)
        self.client.headers.update({'Authorization': f'Bearer'
                                                     f'{token_loader(Shikimori.catalog_name).get("access_token")}'})
        return self.token

    def get(self, url, params=None):
        if not self.is_authorized:
            return
        resp = self.client.request('GET', url, params)
        match resp.status_code:
            case 401:
                if self.token:
                    self.get(url, params)
        return resp

    def check_auth(self):
        url = 'https://shikimori.one/api/users/whoami'
        whoami = self.client.request('GET', url)
        self.is_authorized = whoami and whoami.json()
        return self.is_authorized

    @property
    def token(self):
        return self.client.token