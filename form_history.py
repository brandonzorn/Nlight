from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QWidget, QListWidgetItem

from const import delete_icon_path
from database import Database
from forms.ui_history import Ui_Dialog


class FormHistory(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_delete.setIcon(QIcon(delete_icon_path))
        self.db = Database()
        self.ui.btn_delete.clicked.connect(self.delete_note)
        self.chapters = []

    def setup(self):
        self.ui.listWidget.clear()
        self.chapters = self.db.get_chapters_history()
        for chapter in self.chapters:
            item = QListWidgetItem(chapter.get_name())
            if self.db.check_complete_chapter(chapter):
                if self.db.get_complete_status(chapter):
                    item.setBackground(QColor("GREEN"))
                else:
                    item.setBackground(QColor("RED"))
            self.ui.listWidget.addItem(item)

    def delete_note(self):
        if self.ui.listWidget.currentIndex().row() >= 0:
            self.db.del_complete_chapter(self.chapters[self.ui.listWidget.currentIndex().row()])
            self.setup()
