from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget
from const import library_icon_path, main_icon_path
from database import db
from desu_library import Ui_Dialog


class Communicate(QObject):
    clicked_main = Signal()
    double_click = Signal(object)


class FormLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.c = Communicate()
        self.mangas = []
        self.db = db
        self.ui.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui.btn_main.setIcon(QIcon(main_icon_path))
        self.ui.btn_main.clicked.connect(lambda: self.c.clicked_main.emit())
        self.ui.list_manga.doubleClicked.connect(lambda: self.c.double_click.emit(self.get_current_manga()))

    def get_current_manga(self):
        return self.mangas[self.ui.list_manga.currentIndex().row()]

    def update_list(self):
        self.ui.list_manga.clear()
        self.get_content_library()
        [self.ui.list_manga.addItem(i) for i in self.get_manga_library()]

    def get_content_library(self):
        self.mangas = []
        for i in self.db.get_manga_library():
            self.mangas.append(i)

    def get_manga_library(self) -> list:
        return [i.get_name() for i in self.mangas]
