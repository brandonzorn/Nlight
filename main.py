import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from const import app_icon_path
from form_facial import FormFacial
from form_info import FormInfo
from form_library import FormLibrary
from static import *


class App(QStackedWidget):
    def __init__(self):
        super().__init__()
        screen_size = [self.screen().size().width(), self.screen().size().height()]
        self.setMinimumSize(QSize(screen_size[0] // 2, screen_size[1] // 2))
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
        self.Form_facial.c.clicked_library.connect(self.clicked_library)
        self.Form_library.c.clicked_main.connect(self.clicked_main)
        self.Form_facial.c.double_click.connect(self.double_click)
        self.Form_library.c.double_click.connect(self.double_click)
        self.Form_info.c.turn_back.connect(self.back)
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

    def double_click(self, manga):
        self.clicked_chapters(manga)


if __name__ == '__main__':
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication()
    a = App()
    sys.exit(app.exec_())
