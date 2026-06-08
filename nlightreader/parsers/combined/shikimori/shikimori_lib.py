import logging
from typing import Any

from PySide6.QtWidgets import QApplication
import requests
from requests_oauthlib import OAuth2Session

from nlightreader.consts.urls import (
    SHIKIMORI_HEADERS,
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
    URL_SHIKIMORI_TOKEN,
)
from nlightreader.core.enums import LibList
from nlightreader.items import RequestForm, User, UserRate
from nlightreader.models import Manga
from nlightreader.parsers.catalog import LibParser
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)
from nlightreader.utils.decorators import singleton
from nlightreader.utils.token import TokenManager

try:
    from keys import SHIKIMORI_CLIENT_ID, SHIKIMORI_CLIENT_SECRET
except (ModuleNotFoundError, ImportError):
    logging.info("Shikimori API keys not found")
    SHIKIMORI_CLIENT_SECRET, SHIKIMORI_CLIENT_ID = "", ""


class ShikimoriLib(ShikimoriBase, LibParser):
    def __init__(self) -> None:
        super().__init__()
        self.fields = 1
        self.session: Auth = Auth()

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/users/{self.session.user.id}/manga_rates"
        params = {"limit": 50, "page": form.page}
        response = self.session.request("GET", url, params=params)
        lib_list = form.lib_list
        if lib_list == LibList.reading:
            lib_list = "watching"
        elif lib_list == LibList.re_reading:
            lib_list = "rewatching"
        else:
            lib_list = form.lib_list.name

        mangas = []
        if response and (resp_json := response.json()):
            for i in resp_json:
                if not i.get("status") == lib_list:
                    continue
                i = i.get("manga")
                mangas.append(self._setup_manga(i))
        return mangas

    def get_user(self) -> User:
        response = self.session.request("GET", f"{self._URL_API}/users/whoami")
        self.session.user = User(None, None, None)
        if response and (resp_json := response.json()):
            self.session.user = User(
                str(resp_json.get("id")),
                str(resp_json.get("nickname")),
                str(resp_json.get("avatar")),
            )
        return self.session.user

    def create_user_rate(self, manga: Manga) -> None:
        url = f"{self._URL_API}/v2/user_rates"
        data = {
            "user_rate": {
                "target_type": "Manga",
                "user_id": self.session.user.id,
                "target_id": manga.content_id,
            },
        }
        self.session.request("POST", url, json=data)

    def check_user_rate(self, manga: Manga) -> bool:
        url = f"{self._URL_API}/v2/user_rates"
        params = {
            "target_type": "Manga",
            "user_id": self.session.user.id,
            "target_id": manga.content_id,
        }
        response = self.session.request("GET", url, params=params)
        if response and (resp_json := response.json()):
            for i in resp_json:
                if manga.content_id == i.get("target_id"):
                    return True
        return False

    def delete_user_rate(self, user_rate: UserRate) -> None:
        url = f"{self._URL_API}/v2/user_rates/{user_rate.id}"
        self.session.request("DELETE", url)

    def get_user_rate(self, manga: Manga) -> UserRate | None:
        url = f"{self._URL_API}/v2/user_rates"
        params = {
            "target_type": "Manga",
            "user_id": self.session.user.id,
            "target_id": manga.content_id,
        }
        response = self.session.request("GET", url, params=params)
        if response and (resp_json := response.json()):
            for i in resp_json:
                return UserRate(
                    i.get("id"),
                    i.get("user_id"),
                    i.get("target_id"),
                    i.get("score"),
                    LibList.from_str(i.get("status")),
                    i.get("chapters"),
                )
        return None

    def update_user_rate(self, user_rate: UserRate) -> None:
        url = f"{self._URL_API}/v2/user_rates/{user_rate.id}"
        status = user_rate.status.to_str()
        if user_rate.status == LibList.reading:
            status = "watching"
        elif user_rate.status == LibList.re_reading:
            status = "rewatching"
        elif user_rate.status == LibList.on_hold:
            status = "on_hold"
        data = {
            "user_rate": {
                "chapters": f"{user_rate.chapters}",
                "score": f"{user_rate.score}",
                "status": status,
            },
        }
        self.session.request("PATCH", url, json=data)


@singleton
class Auth:
    def __init__(self) -> None:
        self.client_id = SHIKIMORI_CLIENT_ID
        self.client_secret = SHIKIMORI_CLIENT_SECRET
        self.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
        self.extra: dict[str, Any] | None = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        self.tokens = TokenManager.load_token(ShikimoriLib.CATALOG_NAME)
        self.headers = SHIKIMORI_HEADERS | {
            "Authorization": f"Bearer {self.tokens.get('access_token')}",
        }
        self.client = self.get_client("user_rates", self.redirect_uri, None)
        self.refresh_token()
        self.user: User = User(None, None, None)
        self.is_authorized = False
        if self.token:
            self.check_auth()

    def auth_login(self, params: dict[str, str]) -> None:
        self.fetch_token(params["token"])
        self.check_auth()

    def get_client(
        self,
        scope: str,
        redirect_uri: str,
        token: dict[str, Any] | None,
    ) -> OAuth2Session:
        client = OAuth2Session(
            self.client_id,
            auto_refresh_url=URL_SHIKIMORI_TOKEN,
            auto_refresh_kwargs=self.extra,
            scope=scope,
            redirect_uri=redirect_uri,
            token=token,
            token_updater=TokenManager.save_token,
        )
        client.headers.update(self.headers)
        return client

    def get_auth_url(self) -> str:
        auth_url = URL_SHIKIMORI + "/oauth/authorize"
        return self.client.authorization_url(auth_url)[0]

    def fetch_token(self, code: str) -> dict[str, Any] | None:
        try:
            self.client.fetch_token(
                URL_SHIKIMORI_TOKEN,
                code,
                client_secret=self.client_secret,
            )
        except Exception as e:
            logging.error(e)
        token = self.token
        if token is not None:
            TokenManager.save_token(token, ShikimoriLib.CATALOG_NAME)
        return token

    def update_token(self, token: dict[str, Any] | None) -> None:
        if token and "access_token" in token and "refresh_token" in token:
            token = {
                "access_token": token["access_token"],
                "refresh_token": token["refresh_token"],
            }
            TokenManager.save_token(
                token,
                catalog_name=ShikimoriLib.CATALOG_NAME,
            )
            self.tokens = token

    def refresh_token(self) -> dict[str, Any] | None:
        if not TokenManager.load_token(ShikimoriLib.CATALOG_NAME):
            return None
        try:
            self.client.headers.clear()
            self.client.headers.update(SHIKIMORI_HEADERS)
            self.client.refresh_token(
                URL_SHIKIMORI_TOKEN,
                refresh_token=TokenManager.load_token(
                    ShikimoriLib.CATALOG_NAME,
                ).get("refresh_token"),
            )
            self.update_token(self.token)
            access_token = TokenManager.load_token(
                ShikimoriLib.CATALOG_NAME,
            ).get("access_token")
            self.client.headers.update(
                {
                    "Authorization": f"Bearer {access_token}",
                },
            )
            return self.token
        except Exception as e:
            logging.error(e)

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        ignore_authorize: bool = False,
    ) -> requests.Response | None:
        if (
            "test" in QApplication.arguments()
            or "noshiki" in QApplication.arguments()
        ):
            return None
        if not ignore_authorize and not self.is_authorized:
            return None
        try:
            response = self.client.request(
                method,
                url,
                params=params,
                json=json,
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.error(
                f"\n\tError fetching URL: {url}\n"
                f"\t\tReason: {e}\n"
                f"\t\tHeaders: {self.client.headers}\n"
                f"\t\tParams: {params}\n"
                f"\t\tCookies: {self.client.cookies}\n"
                f"\t\tJson: {json}\n",
            )

    def check_auth(self) -> bool:
        url = f"{URL_SHIKIMORI_API}/users/whoami"
        whoami = self.request("GET", url, ignore_authorize=True)
        self.is_authorized = bool(whoami) and bool(whoami.json())
        return self.is_authorized

    @property
    def token(self) -> dict[str, Any] | None:
        return self.client.token


__all__ = ["ShikimoriLib"]
