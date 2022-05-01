import json
import os

import requests
from const import lib_lists_en, lib_lists_ru, DESU_HEADERS
from items import Manga, Chapter, Image


def get_html(url: str, headers: dict = DESU_HEADERS, params=None):
    try:
        return requests.get(url, headers=headers, params=params)
    except requests.exceptions.ConnectionError:
        print('Connection Error')
        print(url)
        print(params)
    except requests.exceptions.MissingSchema:
        print('Missing Schema')
        print(url)
        print(params)


def get_lib_list_en(lib_list_ru):
    return lib_lists_en[lib_lists_ru.index(lib_list_ru)]


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


def token_saver(token):
    with open('Desu/token.json', 'w') as f:
        f.write(json.dumps(token))


def token_loader():
    if os.path.exists('Desu/token.json'):
        with open('Desu/token.json') as f:
            return json.load(f)
    return {}
