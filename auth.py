import oauthlib.oauth2.rfc6749.errors
import requests.models
from requests_oauthlib import OAuth2Session
from const import URL_SHIKIMORI, URL_SHIKIMORI_TOKEN
from keys import SHIKIMORI_CLIENT_ID, SHIKIMORI_CLIENT_SECRET
from static import token_loader, singleton


@singleton
class Auth:
    def __init__(self, token=None, token_saver=None, scope=None):
        self.client_id = SHIKIMORI_CLIENT_ID
        self.client_secret = SHIKIMORI_CLIENT_SECRET
        self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
        self.extra = {'client_id': self.client_id, 'client_secret': self.client_secret}
        self.token_saver = token_saver
        self.tokens = token_loader()
        self.headers = {'User-Agent': 'Shikimori', 'Authorization': f'Bearer {self.tokens.get("access_token")}'}
        self.client = self.get_client(scope, self.redirect_uri, token)

    def get_client(self, scope, redirect_uri, token):
        client = OAuth2Session(self.client_id, auto_refresh_url=URL_SHIKIMORI_TOKEN, auto_refresh_kwargs=self.extra,
                               scope=scope, redirect_uri=redirect_uri, token=token,
                               token_updater=self.token_saver)
        client.headers.update(self.headers)
        return client

    def get_auth_url(self):
        auth_url = URL_SHIKIMORI + '/oauth/authorize'
        return self.client.authorization_url(auth_url)[0]

    def fetch_token(self, code):
        try:
            self.client.fetch_token(URL_SHIKIMORI_TOKEN, code, client_secret=self.client_secret)
        except oauthlib.oauth2.rfc6749.errors.InvalidGrantError:
            return
        self.token_saver(self.token)
        return self.token

    def refresh_token(self):
        if not token_loader():
            return
        self.client.headers.clear()
        self.client.headers.update({'User-Agent': 'Shikimori'})
        self.client.refresh_token(URL_SHIKIMORI_TOKEN, refresh_token=token_loader().get('refresh_token'))
        self.token_saver(self.token)
        self.client.headers.update({'Authorization': f'Bearer {token_loader().get("access_token")}'})
        return self.token

    def get(self, url, params=None) -> requests.models.Response:
        return self.client.request('GET', url, params)

    @property
    def token(self):
        return self.client.token
