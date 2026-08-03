import logging
from typing import override

from nlightreader.consts.urls import (
    URL_SHIKIMORI,
    URL_SHIKIMORI_API,
    URL_SHIKIMORI_TOKEN,
)
from nlightreader.core.enums import LibList
from nlightreader.core.network.oauth_client import OAuthClient
from nlightreader.core.utils.decorators import singleton
from nlightreader.items import RequestForm, User, UserRate
from nlightreader.models import Manga
from nlightreader.parsers.catalog import CatalogAuthType, LibParser
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)

logger = logging.getLogger(__name__)

try:
    from keys import SHIKIMORI_CLIENT_ID, SHIKIMORI_CLIENT_SECRET
except (ModuleNotFoundError, ImportError):
    logger.warning("Shikimori API keys not found")


@singleton
class ShikimoriLib(ShikimoriBase, LibParser):
    AUTH_TYPE = CatalogAuthType.TOKEN

    def __init__(self) -> None:
        super().__init__()
        self.user: User = User(None, None, None)
        self._client: OAuthClient = ShikimoriClient(
            url=URL_SHIKIMORI,
            url_api=URL_SHIKIMORI_API,
            catalog_name=self.CATALOG_NAME,
            headers=self._HEADERS,
        )

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/users/{self.user.id}/manga_rates"
        params = {"limit": 50, "page": form.page}
        response = self._client.request("GET", url, params=params)
        status = self._lib_list_to_str(form.lib_list)

        mangas: list[Manga] = []
        if response and (resp_json := response.json()):
            for i in resp_json:
                if i.get("status") != status:
                    continue
                manga_data = i.get("manga")
                mangas.append(self._setup_manga(manga_data))
        return mangas

    @override
    def get_user(self) -> User:
        response = self._client.request(
            "GET",
            f"{self._URL_API}/users/whoami",
        )
        self.user = User(None, None, None)
        if response and (user_data := response.json()):
            user_id = user_data.get("id")
            if not user_id:
                return self.user
            self.user = User(
                str(user_id),
                str(user_data.get("nickname")),
                str(user_data.get("avatar")),
            )
        return self.user

    @override
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

    @override
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

    @override
    def delete_user_rate(self, user_rate: UserRate) -> None:
        url = f"{self._URL_API}/v2/user_rates/{user_rate.id}"
        self._client.request("DELETE", url)

    @override
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

    @override
    def update_user_rate(self, user_rate: UserRate) -> None:
        url = f"{self._URL_API}/v2/user_rates/{user_rate.id}"
        status = self._lib_list_to_str(user_rate.status)
        data = {
            "user_rate": {
                "chapters": f"{user_rate.chapters}",
                "score": f"{user_rate.score}",
                "status": status,
            },
        }
        self._client.request("PATCH", url, json=data)

    @override
    def _lib_list_to_str(self, lib_list: LibList) -> str:
        match lib_list:
            case LibList.PLANNED:
                return "planned"
            case LibList.READING:
                return "watching"
            case LibList.RE_READING:
                return "rewatching"
            case LibList.COMPLETED:
                return "completed"
            case LibList.ON_HOLD:
                return "on_hold"
            case LibList.DROPPED:
                return "dropped"


class ShikimoriClient(OAuthClient):
    _token_url = URL_SHIKIMORI_TOKEN
    _redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
    _scope = "user_rates"
    _client_id = SHIKIMORI_CLIENT_ID
    _client_secret = SHIKIMORI_CLIENT_SECRET

    @override
    def get_authorization_url(self) -> str:
        authorization_url = f"{self._url}/oauth/authorize"
        url, _ = self._session.create_authorization_url(authorization_url)
        return url

    @override
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

    @override
    def _update_actual_auth_status(self) -> None:
        self._is_authorized = False
        url = f"{URL_SHIKIMORI_API}/users/whoami"
        response = self.request("GET", url, ignore_authorize=True)
        if response is None:
            return
        data = response.json()
        self._is_authorized = bool(data)


__all__ = ["ShikimoriLib"]
