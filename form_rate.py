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
        self.catalog = None
        self.ui.lib_list.addItems(lib_lists_ru)

    def setup(self, manga: Manga):
        self.catalog = get_catalog(manga.catalog_id)()
        rate = self.catalog.get_user_rate(manga)
        self.ui.score.setValue(rate.score)
        self.ui.lib_list.setCurrentIndex(lib_lists_en.index(rate.status))
