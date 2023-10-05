from PySide6.QtCore import QSize, Slot
from PySide6.QtWidgets import QDialog

from data.ui.dialogs.character import Ui_Dialog

from nlightreader.utils import description_to_html, Worker
from nlightreader.utils.catalog_manager import get_catalog
from nlightreader.utils.file_manager import FileManager


class FormCharacter(QDialog):
    def __init__(self, character, catalog_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.show_spoilers.clicked.connect(self.update_description)
        self.setFixedSize(QSize(550, 800))
        self.character = character
        self.setWindowTitle(self.character.get_name())
        self.catalog = get_catalog(catalog_id)()
        self.ui.name_label.setText(self.character.name)
        self.ui.russian_label.setText(self.character.russian)
        self.update_description()
        Worker(self.setup_image).start()

    def closeEvent(self, arg__1):
        self.deleteLater()

    @Slot()
    def update_description(self):
        self.ui.description.setHtml(
            description_to_html(
                self.character.description, self.ui.show_spoilers.isChecked()
            )
        )

    def setup_image(self):
        self.ui.image.setPixmap(
            FileManager.get_character_preview(self.character, self.catalog)
        )
