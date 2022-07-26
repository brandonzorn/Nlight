from requests_oauthlib import OAuth2Session

from const.urls import SHIKIMORI_HEADERS, URL_SHIKIMORI_API, URL_SHIKIMORI, URL_SHIKIMORI_TOKEN
from items import Manga, Genre, RequestForm, User, Kind, UserRate
from keys import SHIKIMORI_CLIENT_ID, SHIKIMORI_CLIENT_SECRET
from parser.Parser import Parser
from utils import get_html, singleton
from utils import token_loader, token_saver


class Shikimori(Parser):
    catalog_name = 'Shikimori'
    is_primary = True

    def __init__(self):
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS
        self.catalog_id = 1
        self.fields = 1
        self.session: Auth = Auth()

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

    def search_manga(self, params: RequestForm):
        url = f'{self.url_api}/mangas'
        params = {'limit': params.limit, 'search': params.search, 'genre': ','.join([i.id for i in params.genres]),
                  'order': 'popularity', 'kind': ','.join(params.kinds), 'page': params.page}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                manga.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian'),
                                   i.get('kind'), i.get('description'), float(i.get('score'))))
        return manga

    def get_preview(self, manga: Manga):
        return get_html(f'https://shikimori.one/system/mangas/preview/{manga.id}.jpg')

    def get_genres(self):
        url = f'{self.url_api}/genres'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and html.json():
            return [Genre(i.get('id'), i.get('name'), i.get('russian'), i.get('kind')) for i in html.json()]
        return []

    def get_kinds(self):
        url = f'{self.url_api}/constants/manga'
        html = get_html(url, headers=self.headers)
        if html and html.status_code == 200 and len(html.json()):
            return [Kind(0, i, '') for i in html.json().get('kind')]
        return []

    def get_manga_login(self, req_params: RequestForm):
        url = f'{self.url_api}/users/{self.get_user().id}/manga_rates'
        params = {"limit": 50, "page": req_params.page}
        html = self.session.get(url, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                if not i.get("status") == req_params.mylist:
                    continue
                i = i.get("manga")
                manga.append(Manga(i.get('id'), self.catalog_id, i.get('name'), i.get('russian'),
                                   i.get('kind'), i.get('description'), float(i.get('score'))))
        return manga

    def get_user(self) -> User:
        whoami = self.session.get('https://shikimori.one/api/users/whoami')
        if whoami and whoami.status_code == 200:
            data = whoami.json()
            return User(data.get('id'), data.get('nickname'), data.get('avatar'))
        return User(None, 'Войти', None)

    def create_user_rate(self, manga: Manga):
        url = f'{self.url_api}/v2/user_rates'
        data = {"user_rate": {'target_type': 'Manga', 'user_id': self.get_user().id, 'target_id': manga.id}}
        self.session.post(url, data)

    def check_user_rate(self, manga: Manga):
        url = f'{self.url_api}/v2/user_rates'
        params = {'target_type': 'Manga', 'user_id': self.get_user().id, 'target_id': manga.id}
        html = self.session.get(url, params)
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                if manga.id == i.get('target_id'):
                    return True
        return False

    def delete_user_rate(self, user_rate: UserRate):
        url = f'{self.url_api}/v2/user_rates/{user_rate.id}'
        self.session.delete(url)

    def get_user_rate(self, manga: Manga) -> UserRate:
        url = f'{self.url_api}/v2/user_rates'
        params = {'target_type': 'Manga', 'user_id': self.get_user().id, 'target_id': manga.id}
        html = self.session.get(url, params)
        if html and html.status_code == 200 and html.json():
            for i in html.json():
                return UserRate(i.get('id'), i.get('user_id'), i.get('target_id'),
                                i.get('score'), i.get('status'), i.get('chapters'))

    def update_user_rate(self, user_rate: UserRate):
        url = f'{self.url_api}/v2/user_rates/{user_rate.id}'
        data = {"user_rate": {"chapters": f"{user_rate.chapters}", "score": f"{user_rate.score}",
                              "status": f"{user_rate.status}"}}
        self.session.patch(url, data).json()


@singleton
class Auth:
    def __init__(self, token=None, scope=None):
        self.client_id = SHIKIMORI_CLIENT_ID
        self.client_secret = SHIKIMORI_CLIENT_SECRET
        self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
        self.extra = {'client_id': self.client_id, 'client_secret': self.client_secret}
        self.tokens = token_loader(Shikimori.catalog_name)
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
                               token_updater=token_saver)
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
        token_saver(self.token, Shikimori.catalog_name)
        return self.token

    def update_token(self, token):
        if token:
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

    def patch(self, url, data):
        if not self.is_authorized:
            return
        resp = self.client.patch(url, json=data)
        return resp

    def post(self, url, data):
        if not self.is_authorized:
            return
        resp = self.client.post(url, json=data)
        return resp

    def delete(self, url):
        if not self.is_authorized:
            return
        resp = self.client.delete(url)
        return resp

    def get_request(self, url, params=None):
        try:
            resp = self.client.request('GET', url, params)
            return resp
        except Exception as e:
            print(e)
            print(url)
            print(params)

    def check_auth(self):
        url = 'https://shikimori.one/api/users/whoami'
        whoami = self.get_request(url)
        self.is_authorized = whoami and whoami.json()
        return self.is_authorized

    @property
    def token(self):
        return self.client.token
