import logging
import os

import requests

from nlightreader.consts.files import LangIcons
from nlightreader.consts.urls import DEFAULT_HEADERS
from nlightreader.core.enums import Language
from nlightreader.core.utils.types import (
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
    headers: dict[str, str] | None = None,
    params: RequestParams | None = None,
    json: JSONObject | None = None,
    data: dict[str, str] | None = None,
    cookies: dict[str, str] | None = None,
    content_type: str | None = None,
) -> None | bytes | str | dict | requests.Response:
    """
    Sends an HTTP GET request to the specified URL with the given
    headers, query parameters, and cookies.

    :param url:
        The URL to request.
    :param method:
        The type of request (GET, POST, PUT, DELETE).
    :param headers:
        Optional dictionary of request headers.
    :param params:
        Optional dictionary of query parameters.
    :param json:
        Optional dictionary of JSON to include in the request.
    :param data:
        Optional dictionary of data to include in the request.
    :param cookies:
        Optional dictionary of cookies to include in the request.
    :param content_type:
        Optional string indicating the expected
        content type of the response ('content', 'text', or 'json').
    :return:
        If content_type is 'content', returns the raw response content (bytes).
        If content_type is 'json', returns the JSON-decoded response.
        Otherwise, returns the full requests.Response object.
        Returns None if there was an error.
    """
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


__all__ = [
    "dd_get",
    "get_language_icon",
    "make_request",
]
