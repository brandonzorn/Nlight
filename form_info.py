import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QWidget, QListWidgetItem
from threading import Thread
from catalog_manager import get_catalog
from const import back_icon_path, favorite_icon_path, favorite1_icon_path, favorite2_icon_path, lib_lists_en
from database import Database
from form.desu_info import Ui_Form
from items import Manga, Chapter
from reader import Reader
from static import get_language_icon


class FormInfo(QWidget):
    def __init__(self, manga: Manga):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.chapters.doubleClicked.connect(self.open_reader)
        self.ui.btn_add_to_lib.clicked.connect(self.add_to_favorites)
        self.ui.btn_back.setIcon(QIcon(back_icon_path))
        self.ui.lib_list.currentIndexChanged.connect(self.change_lib_list)
        self.db = Database()
        self.wd = os.getcwd()
        self.catalog = None
        self.manga = manga
        self.chapters: list[Chapter] = []

    def resizeEvent(self, a0):
        self.ui.image.clear()
        if not self.catalog:
            return
        pixmap = QPixmap(self.get_preview())
        pixmap = pixmap.scaled(self.ui.image.size(), Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)
        self.ui.image.setPixmap(pixmap)

    def setup(self):
        self.catalog = get_catalog(self.manga.catalog_id)()
        pixmap = QPixmap(self.get_preview())
        pixmap = pixmap.scaled(self.ui.image.size())
        self.ui.image.setPixmap(pixmap)
        self.ui.description.setText(self.manga.description)
        self.ui.name.setText(self.manga.name)
        self.ui.russian.setText(self.manga.russian)
        self.set_score(self.manga.score)
        if self.db.check_manga_library(self.manga):
            self.ui.lib_list.setCurrentIndex(lib_lists_en.index(self.db.check_manga_library(self.manga)))
            self.ui.btn_add_to_lib.setIcon(QIcon(favorite1_icon_path))
        else:
            self.ui.btn_add_to_lib.setIcon(QIcon(favorite_icon_path))
        thread = Thread(target=self.get_chapters)
        thread.start()

    def set_score(self, score: float):
        stars = [self.ui.star_1, self.ui.star_2, self.ui.star_3, self.ui.star_4, self.ui.star_5]
        [i.setIcon(QIcon(favorite_icon_path)) for i in stars]
        self.ui.rate.setText(f'Рейтинг: {score}')
        score = round(score) / 2
        for i in range(int(score)):
            a = stars[i]
            a.show()
            a.setIcon(QIcon(favorite1_icon_path))
        if score - int(score) >= 0.75:
            stars[int(score)].setIcon(QIcon(favorite1_icon_path))
            stars[int(score)].show()
        elif 0.25 <= score - int(score) <= 0.5:
            stars[int(score)].setIcon(QIcon(favorite2_icon_path))
            stars[int(score)].show()

    def add_to_favorites(self):
        if self.db.check_manga_library(self.manga):
            self.db.rem_manga_library(self.manga)
            self.ui.btn_add_to_lib.setIcon(QIcon(favorite_icon_path))
        else:
            self.db.add_manga_library(self.manga)
            self.ui.btn_add_to_lib.setIcon(QIcon(favorite1_icon_path))
            self.change_lib_list()

    def change_lib_list(self):
        if self.db.check_manga_library(self.manga):
            lib_list = lib_lists_en[self.ui.lib_list.currentIndex()]
            self.db.add_manga_library(self.manga, lib_list)

    def get_chapters(self):
        self.ui.chapters.clear()
        self.chapters: list[Chapter] = self.catalog.get_chapters(self.manga)
        for i in self.chapters:
            self.db.add_chapter(i, self.manga, self.chapters[::-1].index(i))
        # self.chapters = self.db.get_chapters(self.manga)
        self.chapters.reverse()
        self.chapters.sort(key=lambda ch: ch.language if ch.language else False)
        for i in self.chapters:
            item = QListWidgetItem(i.get_name())
            if self.db.check_complete_chapter(i):
                item.setBackground(QColor("GREEN"))
            if i.language:
                item.setIcon(QIcon(get_language_icon(i.language)))
            self.ui.chapters.addItem(item)

    def open_reader(self):
        reader = Reader()
        reader.setup(self.manga, self.chapters, self.ui.chapters.currentIndex().row() + 1)

    def get_preview(self) -> str:
        path = f'{self.wd}/Desu/images/{self.catalog.catalog_name}/{self.manga.id}'
        if not os.path.exists(f'{path}/preview.jpg'):
            os.makedirs(path, exist_ok=True)
            img = self.catalog.get_preview(self.manga)
            if img:
                with open(f'{path}/preview.jpg', 'wb') as f:
                    f.write(img.content)
        return f'{path}/preview.jpg'

    def download_all(self):
        chapters = self.chapters
        manga = self.manga
        catalog = get_catalog(manga.catalog_id)()
        for chapter in chapters:
            images = catalog.get_images(manga, chapter)
            if images:
                for image in images:
                    if self.isHidden():
                        return
                    self.db.add_images(image, chapter.id)
                    page = image.get('page')
                    path = f'{self.wd}/Desu/images/{catalog.catalog_name}/{manga.id}/{chapter.id}'
                    if not os.path.exists(f'{path}/{page}.jpg'):
                        os.makedirs(path, exist_ok=True)
                        img = catalog.get_image(images[page - 1])
                        with open(f'{path}/{page}.jpg', 'wb') as f:
                            f.write(img.content)
