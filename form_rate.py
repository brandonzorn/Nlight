from PySide6.QtWidgets import QDialog

from catalog_manager import get_catalog
from const.lists import lib_lists_en, lib_lists_ru
from forms.rateManga import Ui_Dialog
from items import Manga


class FormRate(QDialog):
    def __init__(self):
        super().__init__(None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lib_list.addItems(lib_lists_ru)
        self.ui.btn_add.clicked.connect(self.send_rate)
        self.ui.btn_cancel.clicked.connect(lambda: self.destroy())
        self.catalog = None
        self.manga = None
        self.user_rate = None

    def setup(self, manga: Manga):
        self.manga = manga
        self.catalog = get_catalog(manga.catalog_id)()
        self.user_rate = self.catalog.get_user_rate(manga)
        self.ui.score.setValue(self.user_rate.score)
        self.ui.chapters.setValue(self.user_rate.chapters)
        self.ui.lib_list.setCurrentIndex(lib_lists_en.index(self.user_rate.status))

    def send_rate(self):
        self.user_rate.score = self.ui.score.value()
        self.user_rate.chapters = self.ui.chapters.value()
        self.user_rate.status = lib_lists_en[self.ui.lib_list.currentIndex()]
        self.catalog.update_user_rate(self.user_rate)
