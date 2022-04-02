import os
from threading import Thread

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget

from const import back_icon_path, favorite_icon_path, favorite1_icon_path, favorite2_icon_path, URL_API, lib_lists_en
from database import db
from desu_info import Ui_Dialog
from reader import Reader
from static import get_html, get_lib_list_en


class Communicate(QObject):
    turn_back = pyqtSignal()


class FormInfo(QWidget):
    def __init__(self, manga):
        super().__init__()
        self.ui_ch = Ui_Dialog()
        self.ui_ch.setupUi(self)
        self.ui_ch.btn_back.clicked.connect(self.back)
        self.ui_ch.chapters.doubleClicked.connect(self.open_reader)
        self.ui_ch.btn_mylist.clicked.connect(self.add_to_favorites)
        self.ui_ch.btn_back.setIcon(QIcon(back_icon_path))
        self.ui_ch.lib_list.currentIndexChanged.connect(self.change_lib_list)
        self.db = db
        self.c = Communicate()
        self.manga = manga
        self.chapters = []
        self.reader = None

    def back(self):
        self.c.turn_back.emit()

    def setup(self):
        self.ui_ch.image.setPixmap(QPixmap(self.get_preview()))
        self.ui_ch.image.setScaledContents(True)
        self.ui_ch.description.setText(self.manga.description)
        self.ui_ch.name.setText(self.manga.name)
        self.ui_ch.russian.setText(self.manga.russian)
        self.set_score(self.manga.score)
        if self.db.check_manga_library(self.manga.id):
            self.ui_ch.btn_mylist.setIcon(QIcon(favorite1_icon_path))
        else:
            self.ui_ch.btn_mylist.setIcon(QIcon(favorite_icon_path))
        self.get_chapters()

    def set_score(self, score: float):
        stars = [self.ui_ch.star_1, self.ui_ch.star_2, self.ui_ch.star_3, self.ui_ch.star_4, self.ui_ch.star_5]
        [i.setIcon(QIcon(favorite_icon_path)) for i in stars]
        self.ui_ch.rate.setText(f'Рейтинг: {score}')
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
        if self.db.check_manga_library(self.manga.id):
            self.db.rem_manga_library(self.manga.id)
            self.ui_ch.btn_mylist.setIcon(QIcon(favorite_icon_path))
        else:
            self.db.add_manga_library(self.manga.id)
            self.ui_ch.btn_mylist.setIcon(QIcon(favorite1_icon_path))
            self.change_lib_list()

    def change_lib_list(self):
        if self.db.check_manga_library(self.manga.id):
            lib_list = lib_lists_en[self.ui_ch.lib_list.currentIndex()]
            self.db.add_manga_library(self.manga.id, lib_list)

    def get_chapters(self):
        self.ui_ch.chapters.clear()
        current_url = f'{URL_API}/{self.manga.id}'
        html = get_html(current_url)
        self.chapters = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return
            chapters = html.json().get('response').get('chapters').get('list')
            if chapters:
                for i in chapters:
                    self.db.add_chapters(i, self.manga.id, chapters[::-1].index(i))
        self.chapters = self.db.get_chapters(self.manga.id)
        self.chapters.reverse()
        [self.ui_ch.chapters.addItem(i.get_name()) for i in self.chapters]

    def open_reader(self):
        self.reader = Reader(self.manga, self.chapters, self.ui_ch.chapters.currentIndex().row() + 1)

    def get_preview(self) -> str:
        wd = os.getcwd()
        if not os.path.exists(f'{wd}/Desu/images/{self.manga.id}/preview.jpg'):
            os.makedirs(f'{wd}/Desu/images/{self.manga.id}', exist_ok=True)
            img = get_html(f'https://desu.me/data/manga/covers/preview/{self.manga.id}.jpg')
            with open(f'{wd}/Desu/images/{self.manga.id}/preview.jpg', 'wb') as f:
                f.write(img.content)
        return f'{wd}/Desu/images/{self.manga.id}/preview.jpg'

    def download_all(self):
        chapters = self.chapters
        manga = self.manga
        for chapter in chapters:
            current_url = f'https://desu.me/manga/api/{manga.id}/chapter/{chapter.id}'
            html = get_html(current_url)
            images = html.json().get('response').get('pages').get('list')
            if images:
                for image in images:
                    if self.isHidden():
                        return
                    self.db.add_images(image, chapter.id, images.index(image))
                    page = image.get('page')
                    if not os.path.exists(f'{self.wd}/Desu/images/{manga.id}/{chapter.id}/{page}.jpg'):
                        os.makedirs(f'{self.wd}/Desu/images/{manga.id}/{chapter.id}', exist_ok=True)
                        img = get_html(images[page - 1].get('img'))
                        with open(f'{self.wd}/Desu/images/{manga.id}/{chapter.id}/{page}.jpg', 'wb') as f:
                            f.write(img.content)
