import contextlib
import json
import os

import requests

from const.icons import ru_icon_path, gb_icon_path, jp_icon_path
from const.lists import lib_lists_en, lib_lists_ru
from const.urls import DEFAULT_HEADERS
from items import Manga, Chapter, Image


def get_html(url: str, headers: dict = DEFAULT_HEADERS, params=None):
    try:
        return requests.get(url, headers=headers, params=params)
    except Exception as e:
        print(f"{e=}")
        print(f"{url=}")
        print(f"{params=}")
        print(f"{headers=}")


def get_lib_list_en(lib_list_ru):
    return lib_lists_en[lib_lists_ru.index(lib_list_ru)]


def get_language_icon(language: str):
    match language:
        case 'ru':
            return ru_icon_path
        case 'en':
            return gb_icon_path
        case 'jp':
            return jp_icon_path
        case _:
            return ''


def get_url(manga: Manga, chapter: Chapter = None, image: Image = None):
    url = f'https://desu.me/manga/api/'
    url += f'/{manga.id}'
    if chapter:
        url += f'/chapter/{chapter.id}'
        if image:
            return f'{os.getcwd()}/Desu/images/{manga.id}/{chapter.id}/{image.page}.jpg'
    return url


def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper


def with_lock_thread(locker):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with locker:
                return func(*args, **kwargs)
        return wrapper
    return decorator


@contextlib.contextmanager
def lock_ui(ui_to_lock: list):
    [i.setEnabled(False) for i in ui_to_lock]
    yield
    [i.setEnabled(True) for i in ui_to_lock]


class TokenManager:
    path = f'Desu/tokens'

    @staticmethod
    def save_token(token, catalog_name='Shikimori'):
        path = f'{TokenManager.path}/{catalog_name}'
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        with open(f'{path}/token.json', 'w') as f:
            f.write(json.dumps(token))

    @staticmethod
    def load_token(catalog_name):
        path = f'{TokenManager.path}/{catalog_name}'
        if os.path.exists(f'{path}/token.json'):
            with open(f'{path}/token.json') as f:
                data = json.load(f)
                if data:
                    return data
        return {}
