from functools import reduce
from typing import Any, Optional

import requests
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication

from nlightreader.consts import DEFAULT_HEADERS, MangaKinds, StyleColors
from nlightreader.consts.files import LangIcons, Translations, Styles


def get_html(url: str, headers=None, params=None, json=None, data=None, cookies=None, content_type=None):
    """
    Sends an HTTP GET request to the specified URL with the given headers, query parameters, and cookies.

    :param url: The URL to request.
    :param headers: Optional dictionary of request headers.
    :param params: Optional dictionary of query parameters.
    :param json: Optional dictionary of json to include in the request.
    :param data: Optional dictionary of data to include in the request.
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
        return
    try:
        response = requests.get(
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
        print(f"Error fetching URL: {url}")
        print(f"  Reason: {e}")
        print(f"  Headers: {headers}")
        print(f"  Params: {params}")
        print(f"  Cookies: {cookies}")
        print(f"  Json: {json}")
        print(f"  Data: {data}")


def make_request(url: str, method: str, *,
                 headers=None, params=None, json=None, data=None, cookies=None, content_type=None):
    """
    Sends an HTTP GET request to the specified URL with the given headers, query parameters, and cookies.

    :param url: The URL to request.
    :param method: The type of request (GET, POST, PUT, DELETE).
    :param headers: Optional dictionary of request headers.
    :param params: Optional dictionary of query parameters.
    :param json: Optional dictionary of json to include in the request.
    :param data: Optional dictionary of data to include in the request.
    :param cookies: Optional dictionary of cookies to include in the request.
    :param content_type: Optional string indicating the expected content type of the response ('content' or 'json').
    :return: If content_type is 'content', returns the raw response content (bytes).
             If content_type is 'json', returns the JSON-decoded response.
             Otherwise, returns the full requests.Response object.
             Returns None if there was an error.
    """
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
        print(f"Error fetching URL: {url}")
        print(f"  Reason: {e}")
        print(f"  Headers: {headers}")
        print(f"  Params: {params}")
        print(f"  Cookies: {cookies}")
        print(f"  Json: {json}")
        print(f"  Data: {data}")


def get_language_icon(lang_code: str) -> str:
    """
    Returns the file path to the icon for the specified language.

    :param lang_code: A string representing a language code.
    :return: The file path to the icon associated with the language as a string, or an empty string if no icon is found.
    """
    lang_icons = {
        "ru": LangIcons.Ru,
        "en": LangIcons.Gb,
        "jp": LangIcons.Jp,
        "ua": LangIcons.Ua,
    }
    return lang_icons.get(lang_code, "")


def get_manga_kind(kind: str) -> MangaKinds:
    """
    Returns the corresponding value from the `MangaKinds` enumeration for a given string `kind`.

    Args:
        kind (str): A string representing the kind of manga.
    Returns:
        MangaKinds: The corresponding value from the `MangaKinds` enumeration.
    Raises:
        ValueError: If no matches were found for the input `kind`.
    """
    kinds_matches = {
        "manga": MangaKinds.manga,
        "manhwa": MangaKinds.manhwa,
        "manhua": MangaKinds.manhua,
        "one_shot": MangaKinds.one_shot,
        "doujin": MangaKinds.doujin,
        "ranobe": MangaKinds.ranobe,
    }
    if kind not in kinds_matches:
        raise ValueError(f"No matches found for kind '{kind}'.")
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
    :param path: A list of keys representing the path to the desired value. Each key corresponds to
    a nested level in the dictionary.
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


def get_ui_style(style: str, accent_color: Optional[str] = None) -> str:
    """
    Returns a Qt stylesheet string for the specified UI style.

    :param style: A string representing the desired UI style ("Dark" or "Light").
    :param accent_color: (Optional) A string representing the accent color.
    :return: A Qt stylesheet string corresponding to the selected style.
    :raises KeyError: If an invalid style is provided.
    """
    dark = Styles.Dark
    light = Styles.Light
    if style == "Dark":
        style = dark
        binds = StyleColors.DARK_COLOR_BINDS
        if accent_color:
            binds["@accent_color"] = accent_color
    else:
        style = light
        binds = StyleColors.LIGHT_COLOR_BINDS
    for color_type in StyleColors.DEFAULT_COLOR_BINDS:
        style = style.replace(color_type, StyleColors.DEFAULT_COLOR_BINDS[color_type])
    for color_type in binds:
        style = style.replace(color_type, binds[color_type])
    return style
