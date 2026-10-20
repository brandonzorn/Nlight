import logging
import os

import requests

from consts.app import APP_BRANCH
from consts.files import LangIcons
from consts.urls import DEFAULT_HEADERS, GITHUB_REPO_API
from core.enums import Language
from core.utils.types import (
    HTTPCookies,
    HTTPData,
    HTTPHeaders,
    JSONArray,
    JSONObject,
    JSONValue,
    RequestParams,
)

logger = logging.getLogger(__name__)

IS_TEST_ENV = os.getenv("TEST") == "1"


def dd_get(
    structure: JSONObject | JSONArray,
    path: str,
    default: JSONValue = None,
) -> JSONValue:
    if not isinstance(structure, (dict, list)):
        msg = f"Expected a dictionary, got {type(structure)}"
        raise TypeError(msg)

    current: JSONValue = structure
    for key in path.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and key.isdigit():
            index = int(key)
            if 0 <= index < len(current):
                current = current[index]
            else:
                return default
        else:
            if default is None:
                default: JSONValue = {}
            return default

    return current


def make_request(
    url: str | bytes,
    method: str,
    *,
    headers: HTTPHeaders | None = None,
    params: RequestParams | None = None,
    json: JSONObject | None = None,
    data: HTTPData | None = None,
    cookies: HTTPCookies | None = None,
    content_type: str | None = None,
) -> bytes | requests.Response | JSONValue:
    if IS_TEST_ENV:
        logger.warning(
            "%s: request to %s blocked. Reason: testing.",
            "make_request",
            url,
        )
        return None
    if headers is None:
        headers = DEFAULT_HEADERS
    try:
        response = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            json=json,
            data=data,
            cookies=cookies,
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError as e:
        logger.warning("%s: Connection error. %s", "make_request", e)
    except requests.exceptions.RequestException:
        logger.exception(
            "\nError fetching: %s\n"
            "\tCookies: %s\n"
            "\tHeaders: %s\n"
            "\tJson: %s\n"
            "\tParams: %s",
            url,
            cookies,
            headers,
            json,
            params,
        )
    else:
        if content_type == "content":
            return response.content
        if content_type == "json":
            return response.json()
        if content_type == "text":
            return response.text
        return response


def get_language_icon(language: Language) -> str:
    """
    Returns the file path to the icon for the specified language.

    :param language: Language.
    :return:
        The file path to the icon associated
        with the language as a string or an
        empty string if no icon is found.
    """
    if not isinstance(language, Language):
        msg = "Language must be Language"
        raise TypeError(msg)
    lang_icons = {
        Language.RUSSIAN: LangIcons.RU,
        Language.ENGLISH: LangIcons.GB,
        Language.JAPANESE: LangIcons.JP,
        Language.UKRAINIAN: LangIcons.UA,
        Language.UNDEFINED: "",
    }
    return lang_icons[language]


def check_for_updates() -> str | None:
    response = make_request(
        f"{GITHUB_REPO_API}/releases",
        "GET",
        params={"per_page": 2},
        content_type="json",
    )
    if not isinstance(response, list):
        return None
    latest_version = None
    for release in reversed(response):
        if not isinstance(release, dict):
            continue
        version = str(release.get("tag_name") or "")
        if APP_BRANCH in version:
            latest_version = version
    return latest_version


__all__ = [
    "check_for_updates",
    "dd_get",
    "get_language_icon",
    "make_request",
]
