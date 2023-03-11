import os

import platformdirs
from PySide6.QtGui import QPixmap

from nlightreader.consts import APP_NAME
from nlightreader.items import Manga, Chapter, Character


def get_file(path, file_name):
    path = f'{platformdirs.user_data_dir()}/{APP_NAME}/{path}/{file_name}'
    return path


def check_file_exists(path, file_name):
    return os.path.exists(f'{platformdirs.user_data_dir()}/{APP_NAME}/{path}/{file_name}')


def save_file(path, file_name, file_content):
    path = f'{platformdirs.user_data_dir()}/{APP_NAME}/{path}'
    if not os.path.exists(f'{path}/{file_name}'):
        os.makedirs(path, exist_ok=True)
        if file_content:
            with open(f'{path}/{file_name}', 'wb') as f:
                f.write(file_content.content)


def get_character_preview(character: Character, catalog) -> QPixmap:
    path = f'images/{catalog.catalog_name}/characters/{character.content_id}'
    if not check_file_exists(path, 'preview.jpg'):
        save_file(path, 'preview.jpg', catalog.get_character_preview(character))
    return QPixmap(get_file(path, 'preview.jpg'))


def get_manga_preview(manga: Manga, catalog) -> QPixmap:
    path = f'images/{catalog.catalog_name}/manga/{manga.content_id}'
    if not check_file_exists(path, 'preview.jpg'):
        save_file(path, 'preview.jpg', catalog.get_preview(manga))
    return QPixmap(get_file(path, 'preview.jpg'))


def get_chapter_image(manga: Manga, chapter: Chapter, image, catalog) -> QPixmap:
    path = f'images/{catalog.catalog_name}/manga/{manga.content_id}/{chapter.content_id}'
    file_name = f'{image.page}.jpg'
    if not check_file_exists(path, file_name):
        save_file(path, file_name, catalog.get_image(image))
    return QPixmap(get_file(path, file_name))


def check_chapter_image(manga: Manga, chapter: Chapter, image, catalog):
    path = f'images/{catalog.catalog_name}/manga/{manga.content_id}/{chapter.content_id}'
    file_name = f'{image.page}.jpg'
    if manga.kind == 'ranobe':
        file_name = f'{image.page}.txt'
    return check_file_exists(path, file_name)


def get_chapter_text(manga: Manga, chapter: Chapter, image, catalog) -> str:
    path = f'images/{catalog.catalog_name}/manga/{manga.content_id}/{chapter.content_id}'
    file_name = f'{image.page}.txt'
    if not check_file_exists(path, file_name):
        save_file(path, file_name, catalog.get_image(image))
    with open(get_file(path, file_name), encoding="utf8") as f:
        text = f.read()
        text = text.replace('\n', '<br>')
        return text
