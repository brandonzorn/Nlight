from threading import Thread

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

from catalog_manager import get_catalog
from file_manager import check_file_exists, save_file, get_file
from forms.character import Ui_Dialog


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
        pixmap = self.get_preview()
        self.ui.image.setPixmap(pixmap)

    def get_preview(self) -> QPixmap:
        path = f'Desu/images/{self.catalog.catalog_name}/characters/{self.character.id}'
        if not check_file_exists(path, 'preview.jpg'):
            save_file(path, 'preview.jpg', self.catalog.get_character_preview(self.character))
        return QPixmap(get_file(path, 'preview.jpg'))
