from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QCheckBox

from data.ui.dialogs.genres import Ui_Dialog
from nlightreader.utils.catalog_manager import get_catalog


class FormGenres(QDialog):
    def __init__(self):
        super().__init__(None)
        self.ui_ge = Ui_Dialog()
        self.ui_ge.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.setWindowTitle('Genres')
        self.ui_ge.buttonBox.accepted.connect(self.accept_genres)
        self.ui_ge.buttonBox.rejected.connect(self.reject_genres)
        self.catalog = get_catalog()()
        self.selected_genres = []
        self.genres_items = {}
        self.setup()

    def setup(self):
        for i in reversed(range(self.ui_ge.gridLayout.count())):
            self.ui_ge.gridLayout.itemAt(i).widget().deleteLater()
        self.genres_items = {}
        self.selected_genres = []
        genres = self.catalog.get_genres()
        for i in range(len(genres)):
            check_box = QCheckBox(genres[i].get_name())
            self.genres_items.update({check_box: genres[i]})
            self.ui_ge.gridLayout.addWidget(check_box, i // 5, i % 5)

    @Slot()
    def accept_genres(self):
        self.selected_genres = [self.genres_items.get(i) for i in self.genres_items if i.isChecked()]

    @Slot()
    def reject_genres(self):
        for i in self.genres_items:
            if self.genres_items.get(i) not in self.selected_genres:
                i.setChecked(False)
            else:
                i.setChecked(True)

    def clear_genres(self):
        [i.setChecked(False) for i in self.genres_items]
        self.accept_genres()
