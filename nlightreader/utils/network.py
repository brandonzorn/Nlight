import logging
import os
from typing import Any

import requests

logger = logging.getLogger(__name__)

IS_TEST_ENV = os.getenv("TEST", "False") == "True"


class NetworkClient:
    def __init__(
        self,
        *,
        headers: dict[str, Any],
        cookies: dict[str, Any] | None = None,
    ) -> None:
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
            return response
        except requests.exceptions.RequestException as e:
            logger.error(
                f"Network error occurred.\n"
                f"URL: {url} [{method}]\n"
                f"Reason: {e}\n"
                f"Context data:\n"
                f"\t{self._session.headers=}\n"
                f"\t{extra_headers=}\n"
                f"\t{params=}\n"
                f"\t{json=}",
            )
            return None

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
