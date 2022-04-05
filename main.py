import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QStackedWidget, QApplication

from const import app_icon_path
from form_facial import FormFacial
from form_info import FormInfo
from form_library import FormLibrary
from static import *


class App(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        self.setWindowTitle('Desu')
        self.setWindowIcon(QIcon(app_icon_path))
        self.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(45, 45, 45);')
        self.is_library = False
        self.Form_facial = FormFacial()
        self.Form_info = FormInfo(Manga)
        self.Form_library = FormLibrary()
        self.addWidget(self.Form_facial)
        self.addWidget(self.Form_info)
        self.addWidget(self.Form_library)
        self.Form_facial.ui.btn_mylist.clicked.connect(self.clicked_library)
        self.Form_facial.ui.list_manga.doubleClicked.connect(lambda: self.clicked_chapters(
            self.Form_facial.get_current_manga()))
        self.Form_library.ui.btn_main.clicked.connect(self.clicked_main)
        self.Form_library.ui.list_manga.doubleClicked.connect(lambda: self.clicked_chapters(
            self.Form_library.get_current_manga()))
        self.Form_info.ui.btn_back.clicked.connect(self.back)
        self.Form_facial.ui.btn_main.setIconSize(self.Form_facial.ui.btn_main.size())
        self.Form_facial.ui.btn_mylist.setIconSize(self.Form_facial.ui.btn_mylist.size())
        self.Form_library.ui.btn_main.setIconSize(self.Form_facial.ui.btn_main.size())
        self.Form_library.ui.btn_mylist.setIconSize(self.Form_facial.ui.btn_mylist.size())
        self.show()

    def clicked_main(self):
        self.is_library = False
        self.setCurrentIndex(0)

    def clicked_chapters(self, manga):
        self.Form_info.manga = manga
        self.Form_info.setup()
        self.setCurrentIndex(1)

    def clicked_library(self):
        self.is_library = True
        self.Form_library.update_list()
        self.setCurrentIndex(2)

    def back(self):
        if self.is_library:
            self.clicked_library()
        else:
            self.clicked_main()


if __name__ == '__main__':
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec_())
