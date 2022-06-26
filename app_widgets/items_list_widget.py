from PySide6.QtWidgets import QWidget

from forms.itemsList import Ui_Form


class ItemsList(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def add_item(self, name: str):
        self.ui.list_manga.addItem(name)