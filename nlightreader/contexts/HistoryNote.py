from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu

from nlightreader.utils import translate


class HistoryNoteMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.set_as_read = QAction(translate("Menu", "Mark as read"))
        self.remove_all = QAction(translate("Menu", "Remove all"))

    def set_mode(self, mode: int):
        match mode:
            case 0:
                self.addAction(self.remove_all)
                self.addAction(self.set_as_read)
            case 1:
                self.addAction(self.remove_all)
