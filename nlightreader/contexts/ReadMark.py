from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu


class ReadMarkMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QMenu{background-color: rgb(45, 45, 45);color: rgb(255, 255, 255);}
            QMenu::item{background-color: rgb(45, 45, 45);color: rgb(255, 255, 255);}
            QMenu::item:selected{background-color: gray;}""")

        self.set_as_read = QAction('Отметить прочитанным')
        self.set_as_read_all = QAction('Отметить прочитанным все предыдущие')
        self.remove_read_state = QAction('Удалить отметку о прочтении')

    def set_mode(self, mode: int):
        match mode:
            case 0:
                self.addAction(self.set_as_read)
                self.addAction(self.set_as_read_all)
            case 1:
                self.addAction(self.remove_read_state)
                self.addAction(self.set_as_read_all)
            case 2:
                self.addAction(self.set_as_read)
                self.addAction(self.remove_read_state)
                self.addAction(self.set_as_read_all)
