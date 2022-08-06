from PySide6.QtWidgets import QApplication
from requests_oauthlib import OAuth2Session

from const.shikimori_items import ORDERS, KINDS
from const.urls import URL_SHIKIMORI_API, URL_SHIKIMORI_TOKEN, URL_SHIKIMORI, SHIKIMORI_HEADERS
from items import Manga, RequestForm, Genre, Kind, User, UserRate, Order, Character
from keys import SHIKIMORI_CLIENT_SECRET, SHIKIMORI_CLIENT_ID
from parser.Parser import Parser
from utils import get_html, TokenManager, singleton


class ShikimoriBase(Parser):
    catalog_name = 'Shikimori'

    def __init__(self):
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS
        self.catalog_id = 1
        self.is_primary = True

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/mangas/{manga.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = html.json()
            if data.get('volumes'):
                manga.volumes = int(data.get('volumes'))
            if data.get('chapters'):
                manga.chapters = int(data.get('chapters'))
            manga.description = data.get('description')
        return manga

    def get_character(self, character: Character) -> Character:
        url = f'{self.url_api}/characters/{character.id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = html.json()
            character.description = data.get('description')
        return character

    def get_preview(self, manga: Manga):
        return get_html(f'https://shikimori.one/system/mangas/preview/{manga.id}.jpg')

    def get_character_preview(self, character: Character):
        return get_html(f'https://shikimori.one/system/characters/preview/{character.id}.jpg')

    def get_genres(self):
        url = f'{self.url_api}/genres'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and html.json():
            return [Genre(str(i.get('id')), i.get('name'), i.get('russian'), i.get('kind')) for i in html.json()]
        return []

    def get_orders(self) -> list[Order]:
        return [Order('', i['name'], i['russian']) for i in ORDERS]

    def get_relations(self, manga: Manga) -> list[Manga]:
        mangas = []
        url = f'{self.url_api}/mangas/{manga.id}/related'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                if i.get('manga'):
                    i = i.get('manga')
                    mangas.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian'),
                                        i.get('kind'), i.get('description'), float(i.get('score'))))
        return mangas

    def get_characters(self, manga: Manga) -> list[Character]:
        characters = []
        url = f'{self.url_api}/mangas/{manga.id}/roles'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                if i.get('roles'):
                    role = i.get('roles')[0]
                    if role in ['Supporting', 'Main']:
                        data = i.get('character')
                        if data:
                            characters.append(Character(
                                data.get('id'), data.get('name'), data.get('russian'), '', role))
            characters.reverse()
        return characters


class ShikimoriManga(ShikimoriBase):
    catalog_name = 'Shikimori(Manga)'

    def __init__(self):
        super().__init__()

    def search_manga(self, params: RequestForm):
        url = f'{self.url_api}/mangas'
        params = {'limit': params.limit, 'search': params.search, 'genre': ','.join([i.id for i in params.genres]),
                  'order': params.order.name, 'kind': ','.join([i.name for i in params.kinds]), 'page': params.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                manga.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian'),
                                   i.get('kind'), i.get('description'), float(i.get('score'))))
        return manga

    def get_kinds(self):
        return [Kind('', i['name'], i['russian']) for i in KINDS]


class ShikimoriRanobe(ShikimoriBase):
    catalog_name = 'Shikimori(Ranobe)'

    def __init__(self):
        super().__init__()

    def search_manga(self, params: RequestForm):
        url = f'{self.url_api}/ranobe'
        params = {'limit': params.limit, 'search': params.search, 'genre': ','.join([i.id for i in params.genres]),
                  'order': params.order.name, 'kind': ','.join([i.name for i in params.kinds]), 'page': params.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                manga.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian'),
                                   i.get('kind'), i.get('description'), float(i.get('score'))))
        return manga


class ShikimoriLib(ShikimoriBase):

    def __init__(self):
        super().__init__()
        self.fields = 1
        self.session: Auth = Auth()

    def search_manga(self, req_params: RequestForm):
        url = f'{self.url_api}/users/{self.get_user().id}/manga_rates'
        params = {"limit": 50, "page": req_params.page}
        html = self.session.request('GET', url, params)
        mangas = []
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                if not i.get("status") == req_params.mylist:
                    continue
                i = i.get("manga")
                mangas.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian'),
                                    i.get('kind'), i.get('description'), float(i.get('score'))))
        return mangas

    def get_user(self) -> User:
        whoami = self.session.request('GET', 'https://shikimori.one/api/users/whoami')
        if whoami and whoami.status_code == 200:
            data = whoami.json()
            return User(data.get('id'), data.get('nickname'), data.get('avatar'))
        return User(None, 'Войти', None)

    def create_user_rate(self, manga: Manga):
        url = f'{self.url_api}/v2/user_rates'
        data = {"user_rate": {'target_type': 'Manga', 'user_id': self.get_user().id, 'target_id': manga.id}}
        self.session.request('POST', url, json=data)

    def check_user_rate(self, manga: Manga):
        url = f'{self.url_api}/v2/user_rates'
        params = {'target_type': 'Manga', 'user_id': self.get_user().id, 'target_id': manga.id}
        html = self.session.request('GET', url, params)
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                if manga.id == i.get('target_id'):
                    return True
        return False

    def delete_user_rate(self, user_rate: UserRate):
        url = f'{self.url_api}/v2/user_rates/{user_rate.id}'
        self.session.request('DELETE', url)

    def get_user_rate(self, manga: Manga) -> UserRate:
        url = f'{self.url_api}/v2/user_rates'
        params = {'target_type': 'Manga', 'user_id': self.get_user().id, 'target_id': manga.id}
        html = self.session.request('GET', url, params)
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                return UserRate(i.get('id'), i.get('user_id'), i.get('target_id'),
                                i.get('score'), i.get('status'), i.get('chapters'))

    def update_user_rate(self, user_rate: UserRate):
        url = f'{self.url_api}/v2/user_rates/{user_rate.id}'
        data = {"user_rate": {"chapters": f"{user_rate.chapters}", "score": f"{user_rate.score}",
                              "status": f"{user_rate.status}"}}
        self.session.request('PATCH', url, data).json()


@singleton
class Auth:
    def __init__(self, token=None, scope=None):
        self.client_id = SHIKIMORI_CLIENT_ID
        self.client_secret = SHIKIMORI_CLIENT_SECRET
        self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
        self.extra = {'client_id': self.client_id, 'client_secret': self.client_secret}
        self.tokens = TokenManager.load_token(ShikimoriLib.catalog_name)
        self.headers = {'User-Agent': 'Shikimori', 'Authorization': f'Bearer {self.tokens.get("access_token")}'}
        self.client = self.get_client(scope, self.redirect_uri, token)
        self.refresh_token()
        self.is_authorized = False
        if self.token:
            self.check_auth()

    def auth_login(self, data):
        pass

    def get_client(self, scope, redirect_uri, token):
        client = OAuth2Session(self.client_id, auto_refresh_url=URL_SHIKIMORI_TOKEN, auto_refresh_kwargs=self.extra,
                               scope=scope, redirect_uri=redirect_uri, token=token,
                               token_updater=TokenManager.save_token)
        client.headers.update(self.headers)
        return client

    def get_auth_url(self):
        auth_url = URL_SHIKIMORI + '/oauth/authorize'
        return self.client.authorization_url(auth_url)[0]

    def fetch_token(self, code):
        try:
            self.client.fetch_token(URL_SHIKIMORI_TOKEN, code, client_secret=self.client_secret)
        except Exception as e:
            print(e)
        TokenManager.save_token(self.token, ShikimoriLib.catalog_name)
        return self.token

    def update_token(self, token):
        if token:
            TokenManager.save_token(token, ShikimoriLib.catalog_name)
            self.tokens = token

    def refresh_token(self):
        if not TokenManager.load_token(ShikimoriLib.catalog_name):
            return False
        try:
            self.client.headers.clear()
            self.client.headers.update(SHIKIMORI_HEADERS)
            self.client.refresh_token(URL_SHIKIMORI_TOKEN, refresh_token=TokenManager.load_token(
                ShikimoriLib.catalog_name).get('refresh_token'))
            self.update_token(self.token)
            self.client.headers.update({
                'Authorization': f'Bearer {TokenManager.load_token(ShikimoriLib.catalog_name).get("access_token")}'})
            return self.token
        except Exception as e:
            print(e)

    def request(self, method, url, params=None, json=None, ignore_authorize=False):
        if (not self.is_authorized and not ignore_authorize) or QApplication.arguments()[-1] == '-debug':
            print(f"SHIKIMORI REQUEST IGNORED")
            return
        try:
            return self.client.request(method, url, params, json=json)
        except Exception as e:
            print(e)
            print(f"Request data: {method=}, {url=}, {params=}, {json=}")

    def check_auth(self):
        url = 'https://shikimori.one/api/users/whoami'
        whoami = self.request('GET', url, ignore_authorize=True)
        self.is_authorized = whoami and whoami.json()
        return self.is_authorized

    @property
    def token(self):
        return self.client.token
