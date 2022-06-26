from PySide6.QtWidgets import QWidget

from catalog_manager import get_catalog
from database import Database
from forms.desu_library import Ui_Dialog
from items import Manga


class FormLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.cur_list = 'planned'
        self.db = Database()
        self.ui.b_planned.clicked.connect(lambda: self.update_list('planned'))
        self.ui.b_watching.clicked.connect(lambda: self.update_list('watching'))
        self.ui.b_on_hold.clicked.connect(lambda: self.update_list('on_hold'))
        self.ui.b_completed.clicked.connect(lambda: self.update_list('completed'))
        self.ui.b_dropped.clicked.connect(lambda: self.update_list('dropped'))
        self.ui.b_rewatching.clicked.connect(lambda: self.update_list('rewatching'))

    def get_current_manga(self) -> Manga:
        manga = self.mangas[self.ui.list_manga.currentIndex().row()]
        catalog = get_catalog(manga.catalog_id)()
        return catalog.get_manga(manga)

    def update_list(self, lib_list=None):
        if not lib_list:
            lib_list = self.cur_list
        else:
            self.cur_list = lib_list
        self.ui.list_manga.clear()
        self.get_content_library(lib_list)
        [self.ui.list_manga.addItem(i) for i in self.get_manga_library()]

    def get_content_library(self, lib_list):
        self.mangas = [i for i in self.db.get_manga_library(lib_list)]

    def get_manga_library(self) -> list:
        return [i.get_name() for i in self.mangas]
