import logging
import os
from typing import Any

from authlib.integrations.requests_client import OAuth2Session
from authlib.oauth2.rfc6749 import OAuth2Token
import requests

from nlightreader.utils.token import TokenManager

logger = logging.getLogger(__name__)

IS_TEST_ENV = os.getenv("TEST") == "1"


class OAuthClient:
    _auth_url = None
    _token_url = None
    _redirect_uri = None
    _auth_method = None
    _scope = None
    _client_id = None
    _client_secret = None

    def __init__(
        self,
        *,
        url: str,
        url_api: str,
        catalog_name: str,
        headers: dict[str, str],
    ) -> None:
        self._is_authorized = False
        self._catalog_name = catalog_name
        self._url = url
        self._url_api = url_api

        initial_token = OAuth2Token.from_dict(
            TokenManager.load_token(catalog_name),
        )

        self._session = OAuth2Session(
            client_id=self._client_id,
            client_secret=self._client_secret,
            token=initial_token,
            token_endpoint=self._token_url,
            token_endpoint_auth_method=self._auth_method,
            redirect_uri=self._redirect_uri,
            scope=self._scope,
            update_token=self._token_saver,
        )
        self._session.session.headers.clear()
        self._session.session.headers.update(headers)
        if initial_token:
            self._update_actual_auth_status()

    def _token_saver(self, token: OAuth2Token, **_) -> None:
        if not token or "access_token" not in token:
            return
        TokenManager.save_token(
            token,
            catalog_name=self._catalog_name,
        )
        logger.info("OAuth token saved.")

    @property
    def authorized(self) -> bool:
        return self._is_authorized

    @property
    def token(self) -> OAuth2Token | None:
        return self._session.token

    def get_authorization_url(self) -> str:
        raise NotImplementedError

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
        raise NotImplementedError

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        ignore_authorize: bool = False,
    ) -> requests.Response | None:
        if IS_TEST_ENV:
            logger.warning(
                "%s: request to %s blocked. Reason: testing.",
                self._catalog_name,
                url,
            )
            return None
        if not ignore_authorize and not self._is_authorized:
            logger.warning(
                "%s: request to %s blocked. Reason: unauthorized.",
                self._catalog_name,
                url,
            )
            return None
        try:
            response = self._session.request(
                method,
                url,
                params=params,
                json=json,
            )
            response.raise_for_status()
        except requests.exceptions.ConnectionError as e:
            logger.warning("%s: Connection error. %s", self._catalog_name, e)
        except requests.exceptions.RequestException as e:
            logger.warning(
                "%s: %s [%s]\n"
                "\tCookies: %s\n"
                "\tHeaders: %s\n"
                "\tJson: %s\n"
                "\tParams: %s",
                self._catalog_name,
                e,
                method,
                self._session.session.cookies,
                self._session.session.headers,
                json,
                params,
            )
            if e.response is not None and e.response.status_code == 401:
                self._is_authorized = False
        else:
            return response


__all__ = ["OAuthClient"]
