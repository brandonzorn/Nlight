from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QListWidgetItem

from database import Database
from form.ui_ui_history import Ui_Dialog


class FormHistory(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = Database()

    def setup(self):
        self.ui.listWidget.clear()
        chapters = self.db.get_chapters_history()
        for chapter in chapters:
            item = QListWidgetItem(chapter.get_name())
            if self.db.check_complete_chapter(chapter):
                item.setBackground(QColor("GREEN"))
            else:
                item.setBackground(QColor("RED"))
            self.ui.listWidget.addItem(item)
