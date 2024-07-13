import os
import re
import shutil
from pathlib import Path

import platformdirs
from PySide6.QtGui import QPixmap

from nlightreader.consts.app import APP_NAME
from nlightreader.consts.enums import Nl
from nlightreader.items import Chapter, Character, Image
from nlightreader.models import Manga
from nlightreader.parsers.catalog import AbstractCatalog


class FileManager:
    __IMAGES_FOLDER = Path("images")
    __MANGA_FOLDER = Path("manga")
    __CHARACTERS_FOLDER = Path("characters")
    __PREVIEW_FILE = Path("preview.jpg")

    @classmethod
    def __get_manga_folder(
        cls,
        manga: Manga,
        catalog: AbstractCatalog,
    ) -> Path:
        return Path(
            cls.__IMAGES_FOLDER,
            catalog.CATALOG_NAME,
            cls.__MANGA_FOLDER,
            fix_folder_name(str(manga.content_id)),
        )

    @classmethod
    def __get_chapter_folder(
        cls,
        manga: Manga,
        chapter: Chapter,
        catalog: AbstractCatalog,
    ) -> Path:
        return cls.__get_manga_folder(
            manga,
            catalog,
        ) / fix_folder_name(
            str(chapter.content_id),
        )

    @classmethod
    def __get_character_folder(
        cls,
        character: Character,
        catalog: AbstractCatalog,
    ) -> Path:
        return Path(
            cls.__IMAGES_FOLDER,
            catalog.CATALOG_NAME,
            cls.__CHARACTERS_FOLDER,
            fix_folder_name(str(character.content_id)),
        )

    @classmethod
    def check_image_exists(
        cls,
        manga: Manga,
        chapter: Chapter,
        image: Image,
        catalog: AbstractCatalog,
    ) -> bool:
        file_name = f"{image.page}.jpg"
        if manga.kind == Nl.MangaKind.ranobe:
            file_name = f"{image.page}.txt"
        return check_file_exists(
            cls.__get_chapter_folder(manga, chapter, catalog),
            file_name,
        )

    @classmethod
    def get_image_file(
        cls,
        manga: Manga,
        chapter: Chapter,
        image: Image,
        catalog: AbstractCatalog,
    ):
        path = cls.__get_chapter_folder(manga, chapter, catalog)
        file_name = f"{image.page}.jpg"
        if not check_file_exists(path, file_name):
            save_file(path, file_name, catalog.get_image(image))
        return QPixmap(get_full_file_path(path, file_name))

    @classmethod
    def get_chapter_text_file(
        cls,
        manga: Manga,
        chapter: Chapter,
        image: Image,
        catalog: AbstractCatalog,
    ) -> str:
        path = cls.__get_chapter_folder(manga, chapter, catalog)
        file_name = f"{image.page}.txt"
        if not check_file_exists(path, file_name):
            save_file(path, file_name, catalog.get_image(image))
        try:
            with Path(
                get_full_file_path(path, file_name),
            ).open(encoding="utf8") as f:
                text = f.read()
                text = text.replace("\n", "<br>")
                return text
        except FileNotFoundError:
            return ""

    @classmethod
    def get_manga_preview(cls, manga: Manga, catalog: AbstractCatalog):
        path = cls.__get_manga_folder(manga, catalog)
        if not check_file_exists(path, cls.__PREVIEW_FILE):
            save_file(path, cls.__PREVIEW_FILE, catalog.get_preview(manga))
        return QPixmap(get_full_file_path(path, cls.__PREVIEW_FILE))

    @classmethod
    def get_character_preview(
        cls,
        character: Character,
        catalog: AbstractCatalog,
    ) -> QPixmap:
        path = cls.__get_character_folder(character, catalog)
        if not check_file_exists(path, cls.__PREVIEW_FILE):
            save_file(
                path,
                cls.__PREVIEW_FILE,
                catalog.get_character_preview(character),
            )
        return QPixmap(get_full_file_path(path, cls.__PREVIEW_FILE))

    @classmethod
    def remove_chapter_files(
        cls,
        manga: Manga,
        chapter: Chapter,
        catalog: AbstractCatalog,
    ):
        remove_file(
            cls.__get_chapter_folder(manga, chapter, catalog),
        )

    @classmethod
    def remove_manga_files(cls, manga: Manga, catalog: AbstractCatalog):
        remove_file(
            cls.__get_manga_folder(manga, catalog),
        )

    @classmethod
    def open_dir_in_explorer(cls, manga: Manga, catalog: AbstractCatalog):
        os.startfile(
            get_full_dir_path(
                cls.__get_manga_folder(manga, catalog),
            ),
        )


def get_full_dir_path(path: Path) -> Path:
    path = fix_path(path)
    return platformdirs.user_data_path() / APP_NAME / path


def get_full_file_path(path: Path, file_name: str | Path) -> Path:
    return get_full_dir_path(path) / file_name


def check_file_exists(path: Path, file_name: str | Path) -> bool:
    return get_full_file_path(path, file_name).exists()


def save_file(path: Path, file_name: str | Path, file_content):
    full_path = get_full_dir_path(path)
    full_file_path = Path(full_path, file_name)
    if not full_file_path.exists():
        full_path.mkdir(parents=True, exist_ok=True)
        if file_content:
            if isinstance(file_content, str):
                file_content = bytes(file_content, encoding="utf8")
            with full_file_path.open("wb") as f:
                f.write(file_content)


def remove_file(path: Path) -> None:
    full_path = get_full_dir_path(path)
    if full_path.exists():
        shutil.rmtree(full_path, ignore_errors=True)


def fix_folder_name(name: str) -> str:
    invalid_chars_pattern = r'[<>:"|?*\\/]'
    return re.sub(invalid_chars_pattern, "", name)


def fix_path(path: Path) -> Path:
    new_path = Path()
    for p_dir in path.parts:
        new_path /= fix_folder_name(p_dir)
    return new_path
