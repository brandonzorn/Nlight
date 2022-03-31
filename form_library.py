from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from const import library_icon_path, main_icon_path
from database import db
from desu_library import Ui_Dialog


class Communicate(QObject):
    clicked_main = pyqtSignal()
    double_click = pyqtSignal()


class FormLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.c = Communicate()
        self.manga_library = []
        self.db = db
        self.ui.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui.btn_main.setIcon(QIcon(main_icon_path))
        self.ui.btn_main.clicked.connect(lambda: self.c.clicked_main.emit())
        self.ui.list_manga.doubleClicked.connect(lambda: self.c.double_click.emit())

    def update_list(self):
        self.ui.list_manga.clear()
        self.get_content_library()
        [self.ui.list_manga.addItem(i) for i in self.get_manga_library()]

    def get_content_library(self):
        self.manga_library = []
        for i in self.db.get_manga_library():
            self.manga_library.append(i)

    def get_manga_library(self) -> list:
        return [i.get_name() for i in self.manga_library]
