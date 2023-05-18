from functools import reduce
from typing import Any

import requests
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication

from nlightreader.consts import DEFAULT_HEADERS, MangaKinds
from nlightreader.consts.files import LangIcons, Translations, Styles


def get_html(url: str, headers=None, params=None, json=None, cookies=None, content_type=None):
    """
        Sends an HTTP GET request to the specified URL with the given headers, query parameters, and cookies.

        :param url: The URL to request.
        :param headers: Optional dictionary of request headers.
        :param params: Optional dictionary of query parameters.
        :param cookies: Optional dictionary of cookies to include in the request.
        :param content_type: Optional string indicating the expected content type of the response ('content' or 'json').
        :return: If content_type is 'content', returns the raw response content (bytes).
                 If content_type is 'json', returns the JSON-decoded response.
                 Otherwise, returns the full requests.Response object.
                 Returns None if there was an error.
        """
    if headers is None:
        headers = DEFAULT_HEADERS
    if "test" in QApplication.arguments():
        return None
    try:
        response = requests.get(url, headers=headers, params=params, json=json, cookies=cookies)
        response.raise_for_status()
        if content_type == 'content':
            return response.content
        elif content_type == 'json':
            return response.json()
        else:
            return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}")
        print(f"  Reason: {e}")
        print(f"  Headers: {headers}")
        print(f"  Params: {params}")
        print(f"  Cookies: {cookies}")
        return None


def get_language_icon(language: str) -> str:
    """
    Returns the file path to the icon for the specified language.

    :param language: A string representing a language code.
    :return: The file path to the icon associated with the language as a string, or an empty string if no icon is found.
    """
    match language:
        case 'ru':
            return LangIcons.Ru
        case 'en':
            return LangIcons.Gb
        case 'jp':
            return LangIcons.Jp
        case 'ua':
            return LangIcons.Ua
        case _:
            return ''


def get_manga_kind(kind: str) -> MangaKinds:
    kinds_matches = {'manga': MangaKinds.manga, 'manhwa': MangaKinds.manhwa, 'manhua': MangaKinds.manhua,
                     'one_shot': MangaKinds.one_shot, 'doujin': MangaKinds.doujin, 'ranobe': MangaKinds.ranobe}
    assert kind in kinds_matches, f"Not fond matches for {kind}"
    return kinds_matches[kind]


def get_locale(locale: QLocale.Language) -> str:
    """
    Returns the translation file path for the specified locale.

    :param locale: A QLocale.Language object representing the target language.
    :return: The file path to the translation file associated with the locale as a string,
    or the default translation file if no matching translation is found.
    """
    match locale:
        case QLocale.Language.Russian:
            return Translations.Ru
        case QLocale.Language.Ukrainian:
            return Translations.Uk
        case _:
            return Translations.En


def get_data(data: dict, path: list, default_val=None) -> Any:
    """
    Retrieves a value from a dictionary using a list of nested keys.

    :param data: The dictionary to retrieve values from.
    :param path: A list of keys representing the path to the desired value. Each key corresponds to a nested level in the dictionary.
    :param default_val: Optional default value to return if the specified path does not exist in the dictionary.
    :return: The value located at the specified path in the dictionary, or the default value if the path does not exist.
    :raises TypeError: If the input data is not a dictionary.
    """
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    if default_val is None:
        default_val = None
    current_data = data
    try:
        return reduce(dict.__getitem__, path, current_data)
    except (KeyError, TypeError):
        return default_val


def get_ui_style(style: str) -> str:
    """
    Returns a Qt stylesheet string for the specified UI style.

    :param style: A string representing the desired UI style ('Dark' or 'Light').
    :return: A Qt stylesheet string corresponding to the selected style.
    :raises KeyError: If an invalid style is provided.
    """
    dark = Styles.Dark
    light = Styles.Light
    themes = {"Dark": dark, "Light": light}
    return themes[style]
