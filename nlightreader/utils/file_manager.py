import os

from PySide6.QtGui import QPixmap

from nlightreader.consts import APP_NAME
from nlightreader.items import Manga, Chapter, Character


def get_file(path, file_name):
    path = f'{os.getcwd()}/{path}/{file_name}'
    return path


def check_file_exists(path, file_name):
    return os.path.exists(f'{os.getcwd()}/{path}/{file_name}')


def save_file(path, file_name, file_content):
    path = f'{os.getcwd()}/{path}'
    if not os.path.exists(f'{path}/{file_name}'):
        os.makedirs(path, exist_ok=True)
        if file_content:
            with open(f'{path}/{file_name}', 'wb') as f:
                f.write(file_content.content)


def init_app_paths(paths: list[str]):
    for path in paths:
        path = f'{os.getcwd()}/{path}'
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)


def get_character_preview(character: Character, catalog) -> QPixmap:
    path = f'{APP_NAME}/images/{catalog.catalog_name}/characters/{character.content_id}'
    if not check_file_exists(path, 'preview.jpg'):
        save_file(path, 'preview.jpg', catalog.get_character_preview(character))
    return QPixmap(get_file(path, 'preview.jpg'))


def get_manga_preview(manga: Manga, catalog) -> QPixmap:
    path = f'{APP_NAME}/images/{catalog.catalog_name}/manga/{manga.content_id}'
    if not check_file_exists(path, 'preview.jpg'):
        save_file(path, 'preview.jpg', catalog.get_preview(manga))
    return QPixmap(get_file(path, 'preview.jpg'))


def get_chapter_image(manga: Manga, chapter: Chapter, image, catalog) -> QPixmap:
    path = f'{APP_NAME}/images/{catalog.catalog_name}/manga/{manga.content_id}/{chapter.content_id}'
    file_name = f'{image.page}.jpg'
    if not check_file_exists(path, file_name):
        save_file(path, file_name, catalog.get_image(image))
    return QPixmap(get_file(path, file_name))


def check_chapter_image(manga: Manga, chapter: Chapter, image, catalog):
    path = f'{APP_NAME}/images/{catalog.catalog_name}/manga/{manga.content_id}/{chapter.content_id}'
    file_name = f'{image.page}.jpg'
    if manga.kind == 'ranobe':
        file_name = f'{image.page}.txt'
    return check_file_exists(path, file_name)


def get_chapter_text(manga: Manga, chapter: Chapter, image, catalog) -> str:
    path = f'{APP_NAME}/images/{catalog.catalog_name}/manga/{manga.content_id}/{chapter.content_id}'
    file_name = f'{image.page}.txt'
    if not check_file_exists(path, file_name):
        save_file(path, file_name, catalog.get_image(image))
    with open(f'{path}/{file_name}', encoding="utf8") as f:
        text = f.read()
        text = text.replace('&nbsp;', u'\xa0')
        text = text.replace('&mdash;', '—')
        return text
