import logging
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess

from PySide6.QtGui import QPixmap

from nlightreader.core.enums import MangaKind
from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.models import Chapter, Character, Image, Manga
from nlightreader.parsers.catalog import AbstractCatalog

logger = logging.getLogger(__name__)


class FileManager:
    __IMAGES_FOLDER = Path("images")
    __MANGA_FOLDER = Path("manga")
    __ANIME_FOLDER = Path("anime")
    __CHARACTERS_FOLDER = Path("characters")
    __EPISODES_FOLDER = Path("episodes")
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
            sanitize_name(manga.content_id),
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
        ) / sanitize_name(chapter.content_id)

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
            sanitize_name(character.content_id),
        )

    @classmethod
    def check_image_exists(
        cls,
        manga: Manga,
        chapter: Chapter,
        image: Image,
        catalog: AbstractCatalog,
    ) -> bool:
        file_name = (
            f"{image.page_number}.txt"
            if manga.kind == MangaKind.ranobe
            else f"{image.page_number}.jpg"
        )
        return check_file_exists(
            cls.__get_chapter_folder(
                manga,
                chapter,
                catalog,
            ),
            file_name,
        )

    @classmethod
    def get_image_file(
        cls,
        manga: Manga,
        chapter: Chapter,
        image: Image,
        catalog: AbstractCatalog,
    ) -> QPixmap:
        path = cls.__get_chapter_folder(manga, chapter, catalog)
        file_name = f"{image.page_number}.jpg"

        if not check_file_exists(path, file_name):
            img_data = catalog.get_image(image)
            if not img_data:
                logger.error(
                    "Failed to download image for page %s",
                    image.page_number,
                )
                return QPixmap()
            save_file(path, file_name, img_data)

        return QPixmap(str(get_full_file_path(path, file_name)))

    @classmethod
    def get_chapter_text_file(
        cls,
        manga: Manga,
        chapter: Chapter,
        image: Image,
        catalog: AbstractCatalog,
    ) -> str:
        path = cls.__get_chapter_folder(manga, chapter, catalog)
        file_name = f"{image.page_number}.txt"

        if not check_file_exists(path, file_name):
            text_data = catalog.get_image(image)
            if not text_data:
                return ""
            save_file(path, file_name, text_data)

        try:
            with get_full_file_path(path, file_name).open(
                encoding="utf-8",
            ) as f:
                return f.read().replace("\n", "<br>")
        except OSError as e:
            logger.error("Failed to read text chapter: %s", e)
            return ""

    @classmethod
    def get_manga_preview(
        cls,
        manga: Manga,
        catalog: AbstractCatalog,
    ) -> QPixmap:
        path = cls.__get_manga_folder(manga, catalog)
        if not check_file_exists(path, cls.__PREVIEW_FILE):
            preview_data = catalog.get_preview(manga)
            if not preview_data:
                return QPixmap()
            save_file(path, cls.__PREVIEW_FILE, preview_data)
        return QPixmap(str(get_full_file_path(path, cls.__PREVIEW_FILE)))

    @classmethod
    def get_character_preview(
        cls,
        character: Character,
        catalog: AbstractCatalog,
    ) -> QPixmap:
        path = cls.__get_character_folder(character, catalog)
        if not check_file_exists(path, cls.__PREVIEW_FILE):
            preview_data = catalog.get_character_preview(character)
            if not preview_data:
                return QPixmap()
            save_file(path, cls.__PREVIEW_FILE, preview_data)
        return QPixmap(str(get_full_file_path(path, cls.__PREVIEW_FILE)))

    @classmethod
    def remove_chapter_files(
        cls,
        manga: Manga,
        chapter: Chapter,
        catalog: AbstractCatalog,
    ) -> None:
        remove_dir(cls.__get_chapter_folder(manga, chapter, catalog))

    @classmethod
    def remove_manga_files(
        cls,
        manga: Manga,
        catalog: AbstractCatalog,
    ) -> None:
        remove_dir(cls.__get_manga_folder(manga, catalog))

    @classmethod
    def open_dir_in_explorer(
        cls,
        manga: Manga,
        catalog: AbstractCatalog,
    ) -> None:
        full_path = get_full_dir_path(cls.__get_manga_folder(manga, catalog))
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)

        match platform.system():
            case "Windows":
                os.startfile(full_path)
            case "Darwin":
                subprocess.Popen(["open", str(full_path)])
            case "Linux" | _:
                subprocess.Popen(["xdg-open", str(full_path)])


def get_full_dir_path(path: Path) -> Path:
    return APP_DATA_PATH / sanitize_path(path)


def get_full_file_path(path: Path, file_name: str | Path) -> Path:
    return get_full_dir_path(path) / file_name


def check_file_exists(path: Path, file_name: str | Path) -> bool:
    return get_full_file_path(path, file_name).exists()


def save_file(
    path: Path,
    file_name: str | Path,
    file_content: str | bytes,
) -> None:
    if not file_content:
        return

    full_path = get_full_dir_path(path)
    full_file_path = full_path / file_name

    if not full_file_path.exists():
        full_path.mkdir(parents=True, exist_ok=True)
        try:
            data_to_write = (
                file_content.encode("utf-8")
                if isinstance(file_content, str)
                else file_content
            )
            with full_file_path.open("wb") as f:
                f.write(data_to_write)
        except OSError as e:
            logger.error("Failed to save file %s: %s", full_file_path, e)


def remove_dir(path: Path) -> None:
    full_path = get_full_dir_path(path)
    if full_path.exists():
        shutil.rmtree(full_path, ignore_errors=True)


def sanitize_name(name: str) -> str:
    return re.sub(r'[<>:"|?*\\/]', "", name)


def sanitize_path(path: Path) -> Path:
    new_path = Path()
    for p_dir in path.parts:
        new_path /= sanitize_name(p_dir)
    return new_path


__all__ = [
    "FileManager",
]
