from threading import Thread

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QDialog

from data.ui.character import Ui_Dialog
from nlightreader.utils import TextFormatter
from nlightreader.utils.catalog_manager import get_catalog
from nlightreader.utils.file_manager import get_character_preview


class FormCharacter(QDialog):
    def __init__(self, character, catalog_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.show_spoilers.clicked.connect(self.update_description)
        self.setFixedSize(QSize(550, 800))
        self.character = character
        self.setWindowTitle(self.character.get_name())
        self.catalog = get_catalog(catalog_id)()
        Thread(target=self.setup_image, daemon=True).start()

    def closeEvent(self, arg__1) -> None:
        self.destroy()
        self.deleteLater()

    def setup(self):
        self.ui.name_label.setText(self.character.name)
        self.ui.russian_label.setText(self.character.russian)
        self.update_description()

    def update_description(self):
        self.ui.description.clear()
        self.ui.description.insertHtml(TextFormatter.description_to_html(self.character.description,
                                                                         self.ui.show_spoilers.isChecked()))

    def setup_image(self):
        self.ui.image.setPixmap(get_character_preview(self.character, self.catalog))
