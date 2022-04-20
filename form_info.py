import os
from threading import Thread

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget

from const import back_icon_path, favorite_icon_path, favorite1_icon_path, favorite2_icon_path, lib_lists_en
from database import Database
from form.desu_info import Ui_Form
from parser.Desu import Desu
from reader import Reader


class FormInfo(QWidget):
    def __init__(self, manga):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.chapters.doubleClicked.connect(self.open_reader)
        self.ui.btn_add_to_lib.clicked.connect(self.add_to_favorites)
        self.ui.btn_back.setIcon(QIcon(back_icon_path))
        self.ui.lib_list.currentIndexChanged.connect(self.change_lib_list)
        self.db = Database()
        self.manga = manga
        self.chapters = []

    def setup(self):
        if self.db.check_manga_library(self.manga):
            self.ui.lib_list.setCurrentIndex(lib_lists_en.index(self.db.check_manga_library(self.manga)))
        self.ui.image.setPixmap(QPixmap(self.get_preview()))
        self.ui.image.setScaledContents(True)
        self.ui.description.setText(self.manga.description)
        self.ui.name.setText(self.manga.name)
        self.ui.russian.setText(self.manga.russian)
        self.set_score(self.manga.score)
        if self.db.check_manga_library(self.manga):
            self.ui.btn_add_to_lib.setIcon(QIcon(favorite1_icon_path))
        else:
            self.ui.btn_add_to_lib.setIcon(QIcon(favorite_icon_path))
        self.get_chapters()

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
        self.chapters = Desu().get_chapters(self.manga)
        for i in self.chapters:
            self.db.add_chapter(i, self.manga, self.chapters[::-1].index(i))
        self.chapters = self.db.get_chapters(self.manga)
        self.chapters.reverse()
        [self.ui.chapters.addItem(i.get_name()) for i in self.chapters]

    def open_reader(self):
        reader = Reader()
        reader.setup(self.manga, self.chapters, self.ui.chapters.currentIndex().row() + 1)

    def get_preview(self) -> str:
        wd = os.getcwd()
        if not os.path.exists(f'{wd}/Desu/images/{self.manga.id}/preview.jpg'):
            os.makedirs(f'{wd}/Desu/images/{self.manga.id}', exist_ok=True)
            img = Desu().get_preview(self.manga)
            with open(f'{wd}/Desu/images/{self.manga.id}/preview.jpg', 'wb') as f:
                f.write(img.content)
        return f'{wd}/Desu/images/{self.manga.id}/preview.jpg'

    def download_all(self):
        chapters = self.chapters
        manga = self.manga
        for chapter in chapters:
            images = Desu().get_images(manga, chapter)
            if images:
                for image in images:
                    if self.isHidden():
                        return
                    self.db.add_images(image, chapter.id)
                    page = image.get('page')
                    if not os.path.exists(f'{self.wd}/Desu/images/{manga.id}/{chapter.id}/{page}.jpg'):
                        os.makedirs(f'{self.wd}/Desu/images/{manga.id}/{chapter.id}', exist_ok=True)
                        img = Desu().get_image(images[page - 1])
                        with open(f'{self.wd}/Desu/images/{manga.id}/{chapter.id}/{page}.jpg', 'wb') as f:
                            f.write(img.content)
