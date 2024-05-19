import os
import re
import shutil
from pathlib import Path

import platformdirs
from PySide6.QtGui import QPixmap

from nlightreader.consts.app import APP_NAME
from nlightreader.consts.enums import Nl
from nlightreader.items import Manga, Chapter, Character
from nlightreader.parsers.catalog import AbstractCatalog


class FileManager:
    images_folder = "images"
    manga_folder = "manga"
    preview_file = "preview.jpg"

    @classmethod
    def check_image_exists(cls, manga: Manga, chapter: Chapter, image, catalog: AbstractCatalog) -> bool:
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/{cls.manga_folder}/{manga.content_id}/{chapter.content_id}"
        file_name = f"{image.page}.jpg"
        if manga.kind == Nl.MangaKind.ranobe:
            file_name = f"{image.page}.txt"
        return check_file_exists(path, file_name)

    @classmethod
    def get_image_file(cls, manga: Manga, chapter: Chapter, image, catalog: AbstractCatalog):
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/{cls.manga_folder}/{manga.content_id}/{chapter.content_id}"
        file_name = f"{image.page}.jpg"
        if not check_file_exists(path, file_name):
            save_file(path, file_name, catalog.get_image(image))
        return QPixmap(get_file_path(path, file_name))

    @classmethod
    def get_chapter_text_file(cls, manga: Manga, chapter: Chapter, image, catalog: AbstractCatalog) -> str:
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/{cls.manga_folder}/{manga.content_id}/{chapter.content_id}"
        file_name = f"{image.page}.txt"
        if not check_file_exists(path, file_name):
            save_file(path, file_name, catalog.get_image(image))
        try:
            with Path(get_file_path(path, file_name)).open(encoding="utf8") as f:
                text = f.read()
                text = text.replace("\n", "<br>")
                return text
        except FileNotFoundError:
            return ""

    @classmethod
    def get_manga_preview(cls, manga: Manga, catalog: AbstractCatalog):
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/{cls.manga_folder}/{manga.content_id}"
        if not check_file_exists(path, cls.preview_file):
            save_file(path, cls.preview_file, catalog.get_preview(manga))
        return QPixmap(get_file_path(path, cls.preview_file))

    @classmethod
    def get_character_preview(cls, character: Character, catalog: AbstractCatalog) -> QPixmap:
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/characters/{character.content_id}"
        if not check_file_exists(path, cls.preview_file):
            save_file(path, cls.preview_file, catalog.get_character_preview(character))
        return QPixmap(get_file_path(path, cls.preview_file))

    @classmethod
    def remove_chapter_files(cls, manga: Manga, chapter: Chapter, catalog: AbstractCatalog):
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/{cls.manga_folder}/{manga.content_id}/{chapter.content_id}"
        remove_file(path)

    @classmethod
    def remove_manga_files(cls, manga: Manga, catalog: AbstractCatalog):
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/{cls.manga_folder}/{manga.content_id}"
        remove_file(path)

    @classmethod
    def open_dir_in_explorer(cls, manga: Manga, catalog: AbstractCatalog):
        path = f"{cls.images_folder}/{catalog.CATALOG_NAME}/{cls.manga_folder}/{manga.content_id}"
        os.startfile(get_dir_path(path))


def get_dir_path(path):
    path = fix_path(path)
    return f"{platformdirs.user_data_dir()}/{APP_NAME}/{path}"


def get_file_path(path, file_name):
    path = fix_path(path)
    return f"{platformdirs.user_data_dir()}/{APP_NAME}/{path}/{file_name}"


def check_file_exists(path, file_name):
    path = fix_path(path)
    return Path(get_file_path(path, file_name)).exists()


def save_file(path, file_name, file_content):
    path = fix_path(path)
    path = f"{platformdirs.user_data_dir()}/{APP_NAME}/{path}"
    if not Path(f"{path}/{file_name}").exists():
        Path(path).mkdir(parents=True, exist_ok=True)
        if file_content:
            if isinstance(file_content, str):
                file_content = bytes(file_content, encoding="utf8")
            with Path(f"{path}/{file_name}").open("wb") as f:
                f.write(file_content)


def remove_file(path):
    path = fix_path(path)
    path = Path(f"{platformdirs.user_data_dir()}/{APP_NAME}/{path}")
    if path.exists():
        shutil.rmtree(path, ignore_errors=True)


def fix_folder_name(name):
    invalid_chars_pattern = r'[<>:"|?*\\/]'
    return re.sub(invalid_chars_pattern, "", name)


def fix_path(path):
    new_path = []
    for p_dir in path.split("/"):
        new_path.append(fix_folder_name(p_dir))
    return "/".join(new_path)
