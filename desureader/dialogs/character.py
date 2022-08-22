from threading import Thread

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QDialog

from data.ui.character import Ui_Dialog
from desureader.utils.catalog_manager import get_catalog
from desureader.utils.file_manager import get_character_preview


class FormCharacter(QDialog):
    def __init__(self, character, catalog_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(550, 800))
        self.character = character
        self.setWindowTitle(self.character.get_name())
        self.ui.name_label.setText(self.character.name)
        self.ui.russian_label.setText(self.character.russian)
        self.ui.description.setText(self.character.description)
        self.catalog = get_catalog(catalog_id)()
        Thread(target=self.setup_image, daemon=True).start()

    def setup_image(self):
        self.ui.image.setPixmap(get_character_preview(self.character, self.catalog))
