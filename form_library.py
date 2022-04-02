from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from const import library_icon_path, main_icon_path
from database import db
from desu_library import Ui_Dialog


class Communicate(QObject):
    clicked_main = pyqtSignal()
    double_click = pyqtSignal(object)


class FormLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.c = Communicate()
        self.mangas = []
        self.cur_list = 'planned'
        self.db = db
        self.ui.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui.btn_main.setIcon(QIcon(main_icon_path))
        self.ui.btn_main.clicked.connect(lambda: self.c.clicked_main.emit())
        self.ui.list_manga.doubleClicked.connect(lambda: self.c.double_click.emit(self.get_current_manga()))
        self.ui.b_planned.clicked.connect(lambda: self.update_list('planned'))
        self.ui.b_watching.clicked.connect(lambda: self.update_list('watching'))
        self.ui.b_on_hold.clicked.connect(lambda: self.update_list('on_hold'))
        self.ui.b_completed.clicked.connect(lambda: self.update_list('completed'))
        self.ui.b_dropped.clicked.connect(lambda: self.update_list('dropped'))
        self.ui.b_rewatching.clicked.connect(lambda: self.update_list('rewatching'))

    def get_current_manga(self):
        return self.mangas[self.ui.list_manga.currentIndex().row()]

    def update_list(self, lib_list=None):
        if not lib_list:
            lib_list = self.cur_list
        else:
            self.cur_list = lib_list
        self.ui.list_manga.clear()
        self.get_content_library(lib_list)
        [self.ui.list_manga.addItem(i) for i in self.get_manga_library()]

    def get_content_library(self, lib_list):
        self.mangas = []
        for i in self.db.get_manga_library(lib_list):
            self.mangas.append(i)

    def get_manga_library(self) -> list:
        return [i.get_name() for i in self.mangas]
