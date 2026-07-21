import logging
import os
from typing import Any

import requests

logger = logging.getLogger(__name__)

IS_TEST_ENV = os.getenv("TEST") == "1"


class NetworkClient:
    def __init__(
        self,
        *,
        catalog_name: str,
        headers: dict[str, Any],
        cookies: dict[str, Any] | None = None,
    ) -> None:
        self._catalog_name = catalog_name

        self._session = requests.Session()
        self._session.headers.clear()
        self._session.headers.update(headers)
        if cookies:
            self._session.cookies.update(cookies)

    def _send_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        json: dict | None = None,
        extra_headers: dict[str, str] | None = None,
        extra_cookies: dict[str, str] | None = None,
    ) -> requests.Response | None:
        if IS_TEST_ENV:
            logger.warning(
                "%s: request to %s blocked. Reason: testing.",
                self._catalog_name,
                url,
            )
            return None
        try:
            response = self._session.request(
                method=method,
                url=url,
                headers=extra_headers,
                cookies=extra_cookies,
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
                "\tExtra headers: %s\n"
                "\tJson: %s\n"
                "\tParams: %s",
                self._catalog_name,
                e,
                method,
                extra_cookies,
                self._session.headers,
                extra_headers,
                json,
                params,
            )
            return None
        else:
            return response

    def get_json(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        json: dict | None = None,
        extra_headers: dict[str, str] | None = None,
        extra_cookies: dict[str, str] | None = None,
    ) -> dict[str, Any] | list[dict]:
        response = self._send_request(
            "GET",
            url,
            params=params,
            json=json,
            extra_headers=extra_headers,
            extra_cookies=extra_cookies,
        )
        if response is None:
            return {}
        return response.json()

    def get_bytes(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        json: dict | None = None,
        extra_headers: dict[str, str] | None = None,
        extra_cookies: dict[str, str] | None = None,
    ) -> bytes | None:
        response = self._send_request(
            "GET",
            url,
            params=params,
            json=json,
            extra_headers=extra_headers,
            extra_cookies=extra_cookies,
        )
        if response is None:
            return None
        return response.content

    def get_text(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        json: dict | None = None,
        extra_headers: dict[str, str] | None = None,
        extra_cookies: dict[str, str] | None = None,
    ) -> str | None:
        response = self._send_request(
            "GET",
            url,
            params=params,
            json=json,
            extra_headers=extra_headers,
            extra_cookies=extra_cookies,
        )
        if response is None:
            return None
        return response.text


__all__ = ["NetworkClient"]
