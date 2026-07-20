import logging
import os

import requests

from nlightreader.consts.files import LangIcons
from nlightreader.consts.urls import DEFAULT_HEADERS
from nlightreader.core.enums import Language

logger = logging.getLogger(__name__)

IS_TEST_ENV = os.getenv("TEST") == "1"

type _PrimitiveType = str | bytes | int | float | bool
type _PrimitiveCollection = list[_PrimitiveType] | dict[str, _PrimitiveType]
type RequestParams = dict[
    _PrimitiveType,
    _PrimitiveType | _PrimitiveCollection,
]

type JSONValue = str | int | float | bool | JSONArray | JSONObject | None
type JSONObject = dict[str, JSONValue]
type JSONArray = list[JSONValue]


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
            f"make_request: request to {url} blocked. Reason: test state.",
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
        if content_type == "content":
            return response.content
        if content_type == "json":
            return response.json()
        if content_type == "text":
            return response.text
        return response
    except requests.exceptions.RequestException as e:
        logger.error(
            f"\nError fetching: {url}\n"
            f"\tReason: {e}\n"
            f"\tCookies: {cookies}\n"
            f"\tData: {data}"
            f"\tHeaders: {headers}\n"
            f"\tJson: {json}\n"
            f"\tParams: {params}\n",
        )


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
    "make_request",
    "get_language_icon",
]
