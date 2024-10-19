from PySide6.QtCore import QSize, Slot
from PySide6.QtWidgets import QDialog

from data.ui.dialogs.character import Ui_Dialog
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.text_formatter import description_to_html
from nlightreader.utils.threads import Worker


class FormCharacter(QDialog):
    def __init__(self, character, catalog_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.show_spoilers.checkedChanged.connect(self.update_description)
        self.setFixedSize(QSize(550, 800))
        self.__character = character
        self.setWindowTitle(self.__character.get_name())
        self.__catalog = get_catalog_by_id(catalog_id)
        self.ui.name_label.setText(self.__character.name)
        self.ui.russian_label.setText(self.__character.russian)
        self.update_description()
        Worker(self.setup_image).start()

    def closeEvent(self, arg__1):
        self.deleteLater()

    @Slot()
    def update_description(self):
        self.ui.description.setHtml(
            description_to_html(
                self.__character.description,
                self.ui.show_spoilers.isChecked(),
            ),
        )

    def setup_image(self):
        self.ui.image.setPixmap(
            FileManager.get_character_preview(
                self.__character,
                self.__catalog,
            ),
        )
