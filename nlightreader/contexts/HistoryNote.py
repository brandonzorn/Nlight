from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu


class HistoryNoteMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.set_as_read = QAction('Отметить прочитанным')
        self.remove_all = QAction('Удалить все')

    def set_mode(self, mode: int):
        match mode:
            case 0:
                self.addAction(self.remove_all)
                self.addAction(self.set_as_read)
            case 1:
                self.addAction(self.remove_all)
