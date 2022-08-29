from threading import Thread, Lock

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QWidget, QListWidgetItem

from const.lists import lib_lists_en, lib_lists_ru, LibList
from data.ui.info import Ui_Form
from desureader.dialogs import FormRate, FormCharacter
from desureader.utils import Database, get_manga_preview, lock_ui, get_catalog, get_status, with_lock_thread, \
    get_language_icon, TextFormatter
from desureader.windows.Reader import Reader
from items import Manga, Chapter, Character


class FormInfo(QWidget):

    lock = Lock()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lib_list_box.addItems([i.capitalize() for i in lib_lists_ru])
        self.ui.items_list.doubleClicked.connect(self.open_reader)
        self.ui.characters_list.doubleClicked.connect(self.open_character)
        self.ui.related_list.doubleClicked.connect(lambda: self.setup(self.get_current_manga()))
        self.ui.shikimori_btn.clicked.connect(self.open_rate)
        self.ui.add_btn.clicked.connect(self.add_to_favorites)
        self.ui.lib_list_box.currentIndexChanged.connect(self.change_lib_list)
        self.db: Database = Database()
        self.catalog = None
        self.manga = None
        self.related_mangas: list[Manga] = []
        self.related_characters: list[Character] = []
        self.chapters: list[Chapter] = []
        self.reader_window = None
        self.rate_window = FormRate()
        self.character_window = None

    def resizeEvent(self, a0):
        self.ui.image.clear()
        if not self.catalog:
            return
        pixmap = get_manga_preview(self.manga, self.catalog)
        pixmap = pixmap.scaled(QSize(512, 320), Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)
        self.ui.image.setPixmap(pixmap)

    def get_current_manga(self):
        return self.catalog.get_manga(self.related_mangas[self.ui.related_list.currentIndex().row()])

    def setup(self, manga: Manga):
        ui_to_lock = [self.ui.back_btn]
        with lock_ui(ui_to_lock):
            self.manga = manga
            self.db.add_manga(self.manga)
            self.catalog = get_catalog(self.manga.catalog_id)()
            self.ui.lib_frame.setVisible(not self.catalog.is_primary)
            self.ui.shikimori_frame.setVisible(self.catalog.is_primary)
            self.set_info()
            if self.db.check_manga_library(self.manga):
                self.ui.lib_list_box.setCurrentIndex(self.db.check_manga_library(self.manga).value)
                self.ui.add_btn.setChecked(True)
            else:
                self.ui.add_btn.setChecked(False)
            self.resizeEvent(None)
            Thread(target=self.get_chapters, daemon=True).start()
            Thread(target=self.get_relations, daemon=True).start()
            Thread(target=self.get_characters, daemon=True).start()

    def open_rate(self):
        self.rate_window.setup(self.manga)
        self.rate_window.show()

    def open_character(self):
        character = self.catalog.get_character(self.related_characters[self.ui.characters_list.currentIndex().row()])
        self.character_window = FormCharacter(character, self.manga.catalog_id)
        self.character_window.show()

    def set_info(self):
        self.ui.name_label.setText(self.manga.name)
        self.ui.russian_label.setText(self.manga.russian)
        self.ui.status_label.setVisible(bool(self.manga.status))
        self.ui.status_label.setText(f"Статус: {get_status(self.manga.status)}")
        self.ui.volumes_label.setVisible(bool(self.manga.volumes))
        self.ui.chapters_label.setVisible(bool(self.manga.chapters))
        self.ui.volumes_label.setText(f"Томов: {self.manga.volumes}")
        self.ui.chapters_label.setText(f"Глав: {self.manga.chapters}")
        self.ui.catalog_score_label.setVisible(bool(self.manga.score))
        self.ui.catalog_score_label.setText(f"Рейтинг: {self.manga.score}")
        if self.manga.description:
            self.ui.description_text.insertHtml(TextFormatter.description_to_html(self.manga.description))

    def add_to_favorites(self):
        if self.db.check_manga_library(self.manga):
            self.db.rem_manga_library(self.manga)
        else:
            self.db.add_manga_library(self.manga)
            self.change_lib_list()

    def change_lib_list(self):
        if self.db.check_manga_library(self.manga):
            lib_list = LibList[lib_lists_en[self.ui.lib_list_box.currentIndex()]]
            self.db.add_manga_library(self.manga, lib_list)

    @with_lock_thread(lock)
    def get_chapters(self):
        ui_to_lock = [self.ui.back_btn]
        with lock_ui(ui_to_lock):
            self.ui.items_list.clear()
            self.chapters: list[Chapter] = self.catalog.get_chapters(self.manga)
            self.chapters.reverse()
            self.chapters.sort(key=lambda ch: ch.language if ch.language else False)
            self.ui.items_frame.setVisible(bool(self.chapters))
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
                self.ui.items_list.addItem(item)

    def get_relations(self):
        self.ui.related_list.clear()
        self.related_mangas = self.catalog.get_relations(self.manga)
        self.ui.related_frame.setVisible(bool(self.related_mangas))
        for manga in self.related_mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.related_list.addItem(item)

    def get_characters(self):
        self.ui.characters_list.clear()
        self.related_characters = self.catalog.get_characters(self.manga)
        self.ui.characters_frame.setVisible(bool(self.related_characters))
        for character in self.related_characters:
            item = QListWidgetItem(character.get_name())
            self.ui.characters_list.addItem(item)

    def open_reader(self):
        self.reader_window = Reader()
        self.reader_window.setup(self.manga, self.chapters, self.ui.items_list.currentIndex().row() + 1)
