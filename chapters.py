from items import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from desu_chaptersUI import Ui_Dialog


class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.manga: Manga = Manga({})
        self.chapters = []

    def get_chapters(self):
        pass

    def set_chapters(self):
        pass

    def get_score(self):
        pass

    def set_score(self):
        pass
