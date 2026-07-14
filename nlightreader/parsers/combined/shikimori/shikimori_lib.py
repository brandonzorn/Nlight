import logging
import os
from typing import Any

from authlib.integrations.requests_client import OAuth2Session
from authlib.oauth2.rfc6749 import OAuth2Token
import requests

from nlightreader.consts.urls import (
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
    URL_SHIKIMORI_TOKEN,
)
from nlightreader.core.enums import LibList
from nlightreader.core.utils.decorators import singleton
from nlightreader.items import RequestForm, User, UserRate
from nlightreader.models import Manga
from nlightreader.parsers.catalog import CatalogAuthType, LibParser
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)
from nlightreader.utils.token import TokenManager

logger = logging.getLogger(__name__)

IS_TEST_ENV = os.getenv("TEST") == "1"

try:
    from keys import SHIKIMORI_CLIENT_ID, SHIKIMORI_CLIENT_SECRET
except (ModuleNotFoundError, ImportError):
    logger.warning("Shikimori API keys not found")
    SHIKIMORI_CLIENT_SECRET, SHIKIMORI_CLIENT_ID = "", ""


class ShikimoriLib(ShikimoriBase, LibParser):
    AUTH_TYPE = CatalogAuthType.TOKEN

    def __init__(self) -> None:
        super().__init__()
        self.user: User = User(None, None, None)
        self._client = ShikimoriClient(
            catalog_name=self.CATALOG_NAME,
            headers=self._HEADERS,
        )

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/users/{self.user.id}/manga_rates"
        params = {"limit": 50, "page": form.page}
        response = self._client.request("GET", url, params=params)
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
                if i.get("status") != lib_list:
                    continue
                i = i.get("manga")
                mangas.append(self._setup_manga(i))
        return mangas

    def get_user(self) -> User:
        response = self._client.request(
            "GET",
            f"{self._URL_API}/users/whoami",
        )
        self.user = User(None, None, None)
        if response and (resp_json := response.json()):
            self.user = User(
                str(resp_json.get("id")),
                str(resp_json.get("nickname")),
                str(resp_json.get("avatar")),
            )
        return self.user

    def create_user_rate(self, manga: Manga) -> None:
        url = f"{self._URL_API}/v2/user_rates"
        data = {
            "user_rate": {
                "target_type": "Manga",
                "user_id": self.user.id,
                "target_id": manga.content_id,
            },
        }
        self._client.request("POST", url, json=data)

    def check_user_rate(self, manga: Manga) -> bool:
        url = f"{self._URL_API}/v2/user_rates"
        params = {
            "target_type": "Manga",
            "user_id": self.user.id,
            "target_id": manga.content_id,
        }
        response = self._client.request("GET", url, params=params)
        if not response or not (resp_json := response.json()):
            return False
        for i in resp_json:
            if manga.content_id != i.get("target_id"):
                continue
            return True
        return False

    def delete_user_rate(self, user_rate: UserRate) -> None:
        url = f"{self._URL_API}/v2/user_rates/{user_rate.id}"
        self._client.request("DELETE", url)

    def get_user_rate(self, manga: Manga) -> UserRate | None:
        url = f"{self._URL_API}/v2/user_rates"
        params = {
            "target_type": "Manga",
            "user_id": self.user.id,
            "target_id": manga.content_id,
        }
        response = self._client.request("GET", url, params=params)
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
        self._client.request("PATCH", url, json=data)


@singleton
class ShikimoriClient:
    def __init__(self, catalog_name: str, headers: dict[str, str]) -> None:
        self._is_authorized = False
        initial_token = OAuth2Token.from_dict(
            TokenManager.load_token(catalog_name),
        )

        self._session = OAuth2Session(
            client_id=SHIKIMORI_CLIENT_ID,
            client_secret=SHIKIMORI_CLIENT_SECRET,
            token=initial_token,
            token_endpoint=URL_SHIKIMORI_TOKEN,
            redirect_uri="urn:ietf:wg:oauth:2.0:oob",
            scope="user_rates",
            update_token=self._token_saver,
        )
        self._session.session.headers.clear()
        self._session.session.headers.update(headers)
        if initial_token:
            self._update_actual_auth_status()

    @staticmethod
    def _token_saver(token: OAuth2Token, **_) -> None:
        if not token or "access_token" not in token:
            return
        TokenManager.save_token(
            token,
            catalog_name=ShikimoriLib.CATALOG_NAME,
        )
        logger.info("OAuth token saved.")

    @property
    def authorized(self) -> bool:
        return self._is_authorized

    @property
    def token(self) -> OAuth2Token | None:
        return self._session.token

    def get_authorization_url(self) -> str:
        authorization_url = f"{URL_SHIKIMORI}/oauth/authorize"
        url, _ = self._session.create_authorization_url(authorization_url)
        return url

    def authorize(self, params: dict[str, str]) -> None:
        token = params.get("token")
        if not token:
            return
        token = self._session.fetch_token(
            code=token,
            grant_type="authorization_code",
        )
        self._token_saver(token)
        self._update_actual_auth_status()

    def _update_actual_auth_status(self) -> None:
        self._is_authorized = False
        url = f"{URL_SHIKIMORI_API}/users/whoami"
        response = self.request("GET", url, ignore_authorize=True)
        if response is None:
            return
        data = response.json()
        self._is_authorized = bool(data)

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        ignore_authorize: bool = False,
    ) -> requests.Response | None:
        if (not ignore_authorize and not self._is_authorized) or IS_TEST_ENV:
            logger.warning(f"Request to {url} blocked: Unauthorized state.")
            return None
        try:
            response = self._session.request(
                method,
                url,
                params=params,
                json=json,
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(
                f"\n\tError fetching URL: {url}\n"
                f"\t\tReason: {e}\n"
                f"\t\tHeaders: {self._session.session.headers}\n"
                f"\t\tParams: {params}\n"
                f"\t\tCookies: {self._session.session.cookies}\n"
                f"\t\tJson: {json}\n",
            )
            if e.response is not None and e.response.status_code == 401:
                self._is_authorized = False


__all__ = ["ShikimoriLib"]
