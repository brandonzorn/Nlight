from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QLayout

from data.ui.dialogs.genres import Ui_Dialog


class FormGenres(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_ge = Ui_Dialog()
        self.ui_ge.setupUi(self)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Genres")
        self.ui_ge.ok_btn.clicked.connect(self.accept_genres)
        self.ui_ge.cancel_btn.clicked.connect(self.reject_genres)
        self.selected_genres = []
        self.genres_items = {}

    @Slot()
    def accept_genres(self):
        self.selected_genres = [
            self.genres_items.get(i) for i in self.genres_items if i.isChecked()
        ]
        self.accept()

    @Slot()
    def reject_genres(self):
        for i in self.genres_items:
            if self.genres_items.get(i) not in self.selected_genres:
                i.setChecked(False)
            else:
                i.setChecked(True)
        self.reject()

    def reset_items(self):
        [i.setChecked(False) for i in self.genres_items]
        self.accept_genres()

    def clear(self):
        self.selected_genres.clear()
        [item.deleteLater() for item in self.genres_items]
        self.genres_items.clear()
