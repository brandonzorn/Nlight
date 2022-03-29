import os

import requests
from const import HEADERS
from items import Manga, Chapter, Image


def get_html(url: str, params=None):
    try:
        return requests.get(url, headers=HEADERS, params=params)
    except Exception as e:
        print(e)


def get_url(manga: Manga=None, chapter: Chapter=None, image: Image=None):
    url = f'https://desu.me/manga/api/'
    if image:
        return f'{os.getcwd()}/Desu/images/{manga.id}/{chapter.id}/{image.page}.jpg'
    if manga:
        url += f'/{manga.id}'
        if chapter:
            url += f'/chapter/{chapter.id}'
    return url
