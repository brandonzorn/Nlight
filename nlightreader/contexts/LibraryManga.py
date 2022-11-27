from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu


class LibraryMangaMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QMenu{background-color: rgb(45, 45, 45);color: rgb(255, 255, 255);}
            QMenu::item{background-color: rgb(45, 45, 45);color: rgb(255, 255, 255);}
            QMenu::item:selected{background-color: gray;}""")

        self.add_to_lib = QAction('Добавить в библиотеку')
        self.remove_from_lib = QAction('Удалить из библиотеки')
        self.open_in_browser = QAction('Открыть в браузере')

    def set_mode(self, mode: int):
        self.addAction(self.open_in_browser)
        match mode:
            case 0:
                self.addAction(self.add_to_lib)
            case 1:
                self.addAction(self.remove_from_lib)
