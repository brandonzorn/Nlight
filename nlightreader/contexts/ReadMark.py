from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu

from nlightreader.utils import translate


class ReadMarkMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.set_as_read = QAction(translate("Menu", "Mark as read"))
        self.set_as_read_all = QAction(translate("Menu", "Mark as read all previous"))
        self.remove_read_state = QAction(translate("Menu", "Remove read mark"))

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
