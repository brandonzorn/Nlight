from threading import Thread, Lock

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QWidget, QListWidgetItem

from app_windows.reader import Reader
from catalog_manager import get_catalog
from const.icons import favorite_icon_path, favorite1_icon_path, favorite2_icon_path
from const.lists import lib_lists_en
from database import Database
from file_manager import check_file_exists, get_file, save_file
from form_rate import FormRate
from forms.desu_info import Ui_Form
from items import Manga, Chapter
from utils import get_language_icon, with_lock_thread, lock_ui


class FormInfo(QWidget):

    lock = Lock()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.chapters.doubleClicked.connect(self.open_reader)
        self.ui.btn_add_to_lib.clicked.connect(self.add_to_favorites)
        self.ui.lib_list.currentIndexChanged.connect(self.change_lib_list)
        self.ui.btn_shikimori.clicked.connect(self.open_rate)
        self.ui.manga_relations.doubleClicked.connect(lambda: self.setup(self.get_current_manga()))
        self.db: Database = Database()
        self.catalog = None
        self.manga = None
        self.related_mangas = []
        self.chapters: list[Chapter] = []
        self.lock = Lock()
        self.reader = None
        self.rate = FormRate()

    def resizeEvent(self, a0):
        self.ui.image.clear()
        if not self.catalog:
            return
        pixmap = self.get_preview()
        pixmap = pixmap.scaled(self.ui.image.size(), Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)
        self.ui.image.setPixmap(pixmap)

    def get_current_manga(self):
        return self.catalog.get_manga(self.related_mangas[self.ui.manga_relations.currentIndex().row()])

    def setup(self, manga: Manga):
        ui_to_lock = [self.ui.btn_back]
        with lock_ui(ui_to_lock):
            self.manga = manga
            self.catalog = get_catalog(self.manga.catalog_id)()
            self.ui.add_lib_frame.setVisible(not self.catalog.is_primary)
            self.ui.add_shikimrori_frame.setVisible(self.catalog.is_primary)
            self.db.add_manga(self.manga)
            self.ui.description.setText(self.manga.description)
            self.ui.name.setText(self.manga.name)
            self.ui.russian.setText(self.manga.russian)
            self.ui.rate_frame.setVisible(bool(self.manga.score))
            self.set_score(self.manga.score)
            self.resizeEvent(None)
            if self.db.check_manga_library(self.manga):
                self.ui.lib_list.setCurrentIndex(lib_lists_en.index(self.db.check_manga_library(self.manga)))
                self.ui.btn_add_to_lib.setIcon(QIcon(favorite1_icon_path))
            else:
                self.ui.btn_add_to_lib.setIcon(QIcon(favorite_icon_path))
            Thread(target=self.get_chapters, daemon=True).start()
            Thread(target=self.get_relations, daemon=True).start()

    def open_rate(self):
        self.rate.setup(self.manga)
        self.rate.show()

    def set_score(self, score: float):
        stars = [self.ui.star_1, self.ui.star_2, self.ui.star_3, self.ui.star_4, self.ui.star_5]
        [i.setIcon(QIcon(favorite_icon_path)) for i in stars]
        self.ui.rate.setText(f'Рейтинг: {score}')
        if score > 10:
            return
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

    @with_lock_thread(lock)
    def get_chapters(self):
        ui_to_lock = [self.ui.btn_back]
        with lock_ui(ui_to_lock):
            self.ui.chapters.clear()
            self.chapters: list[Chapter] = self.catalog.get_chapters(self.manga)
            self.chapters.reverse()
            self.chapters.sort(key=lambda ch: ch.language if ch.language else False)
            self.ui.chapters.setVisible(bool(self.chapters))
            self.db.add_chapters(self.chapters, self.manga)
            for chapter in self.chapters:
                item = QListWidgetItem(chapter.get_name())
                if self.db.check_complete_chapter(chapter):
                    if self.db.get_complete_status(chapter):
                        item.setBackground(QColor("GREEN"))
                    else:
                        item.setBackground(QColor("RED"))
                if chapter.language:
                    item.setIcon(QIcon(get_language_icon(chapter.language)))
                self.ui.chapters.addItem(item)

    def get_relations(self):
        self.ui.manga_relations.clear()
        self.related_mangas = self.catalog.get_relations(self.manga)
        self.ui.related_frame.setVisible(bool(self.related_mangas))
        for manga in self.related_mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.manga_relations.addItem(item)

    def open_reader(self):
        self.reader = Reader()
        self.reader.setup(self.manga, self.chapters, self.ui.chapters.currentIndex().row() + 1)

    def get_preview(self) -> QPixmap:
        path = f'Desu/images/{self.catalog.catalog_name}/{self.manga.id}'
        if not check_file_exists(path, 'preview.jpg'):
            save_file(path, 'preview.jpg', self.catalog.get_preview(self.manga))
        return QPixmap(get_file(path, 'preview.jpg'))
