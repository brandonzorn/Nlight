import logging
from typing import Any

import requests
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication

from nlightreader.consts.urls import DEFAULT_HEADERS
from nlightreader.consts.enums import Nl
from nlightreader.consts.files import LangIcons, Translations


def make_request(
        url: str, method: str, *, headers=None, params=None, json=None, data=None, cookies=None, content_type=None):
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
        Optional dictionary of json to include in the request.
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
    if "test" in QApplication.arguments():
        return
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
        logging.error(
            f"\n\tError fetching URL: {url}\n"
            f"\t\tReason: {e}\n"
            f"\t\tHeaders: {headers}\n"
            f"\t\tParams: {params}\n"
            f"\t\tCookies: {cookies}\n"
            f"\t\tJson: {json}\n"
            f"\t\tData: {data}",
        )


def get_html(url: str, *, headers=None, params=None, json=None, data=None, cookies=None, content_type=None):
    """
    Sends an HTTP GET request to the specified
    URL with the given headers, query parameters, and cookies.

    :param url:
        The URL to request.
    :param headers:
        Optional dictionary of request headers.
    :param params:
        Optional dictionary of query parameters.
    :param json:
        Optional dictionary of json to include in the request.
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
    return make_request(url, "GET", headers=headers, params=params,
                        json=json, data=data, cookies=cookies, content_type=content_type)


def get_language_icon(language: Nl.Language) -> str:
    """
    Returns the file path to the icon for the specified language.

    :param language: Nl.Language.
    :return:
        The file path to the icon associated
        with the language as a string, or an
        empty string if no icon is found.
    """
    if not isinstance(language, Nl.Language):
        raise TypeError("Language must be Nl.Language")
    lang_icons = {
        Nl.Language.ru: LangIcons.Ru,
        Nl.Language.en: LangIcons.Gb,
        Nl.Language.jp: LangIcons.Jp,
        Nl.Language.uk: LangIcons.Ua,
        Nl.Language.undefined: "",
    }
    return lang_icons.get(language)


def get_locale(locale: QLocale.Language) -> str:
    """
    Returns the translation file path for the specified locale.

    :param locale:
        A QLocale.Language object
        representing the target language.
    :return:
        The file path to the translation
        file associated with the locale as a string,
        or the default translation file if no
        matching translation is found.
    """
    translations = {
        QLocale.Language.Russian: Translations.Ru,
        QLocale.Language.Ukrainian: Translations.Uk,
    }
    return translations.get(locale, Translations.En)


def get_data(data: dict, path: list, default_val=None) -> Any:
    """
    Retrieves a value from a dictionary using a list of nested keys.

    :param data:
        The dictionary to retrieve values from.
    :param path:
        A list of keys representing the path
        to the desired value. Each key corresponds
        to a nested level in the dictionary.
    :param default_val:
        Optional default value to return
        if the specified path does not exist in the dictionary.
    :return:
        The value located at the specified path in the dictionary,
        or the default value if the path does not exist.
    :raises TypeError:
        If the input data is not a dictionary.
    """
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    if default_val is None:
        default_val = None
    try:
        for key in path:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return default_val
