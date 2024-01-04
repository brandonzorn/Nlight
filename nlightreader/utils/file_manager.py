import os
import re
import shutil
from pathlib import Path

import platformdirs
from PySide6.QtGui import QPixmap

from nlightreader.consts import APP_NAME
from nlightreader.items import Manga, Chapter, Character


class FileManager:
    @staticmethod
    def check_image_exists(manga: Manga, chapter: Chapter, image, catalog) -> bool:
        path = f"images/{catalog.CATALOG_NAME}/manga/{manga.content_id}/{chapter.content_id}"
        file_name = f"{image.page}.jpg"
        if manga.kind == "ranobe":
            file_name = f"{image.page}.txt"
        return check_file_exists(path, file_name)

    @staticmethod
    def get_image_file(manga: Manga, chapter: Chapter, image, catalog):
        path = f"images/{catalog.CATALOG_NAME}/manga/{manga.content_id}/{chapter.content_id}"
        file_name = f"{image.page}.jpg"
        if not check_file_exists(path, file_name):
            save_file(path, file_name, catalog.get_image(image))
        return QPixmap(get_file_path(path, file_name))

    @staticmethod
    def get_chapter_text_file(manga: Manga, chapter: Chapter, image, catalog) -> str:
        path = f"images/{catalog.CATALOG_NAME}/manga/{manga.content_id}/{chapter.content_id}"
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

    @staticmethod
    def get_manga_preview(manga: Manga, catalog):
        path = f"images/{catalog.CATALOG_NAME}/manga/{manga.content_id}"
        if not check_file_exists(path, "preview.jpg"):
            save_file(path, "preview.jpg", catalog.get_preview(manga))
        return QPixmap(get_file_path(path, "preview.jpg"))

    @staticmethod
    def get_character_preview(character: Character, catalog) -> QPixmap:
        path = f"images/{catalog.CATALOG_NAME}/characters/{character.content_id}"
        if not check_file_exists(path, "preview.jpg"):
            save_file(path, "preview.jpg", catalog.get_character_preview(character))
        return QPixmap(get_file_path(path, "preview.jpg"))

    @staticmethod
    def remove_chapter_files(manga: Manga, chapter: Chapter, catalog):
        path = f"images/{catalog.CATALOG_NAME}/manga/{manga.content_id}/{chapter.content_id}"
        remove_file(path)

    @staticmethod
    def remove_manga_files(manga: Manga, catalog):
        path = f"images/{catalog.CATALOG_NAME}/manga/{manga.content_id}"
        remove_file(path)

    @staticmethod
    def open_dir_in_explorer(manga: Manga, catalog):
        path = f"images/{catalog.CATALOG_NAME}/manga/{manga.content_id}"
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
    fixed_name = re.sub(invalid_chars_pattern, "", name)
    return fixed_name


def fix_path(path):
    new_path = []
    for p_dir in path.split("/"):
        new_path.append(fix_folder_name(p_dir))
    return "/".join(new_path)
