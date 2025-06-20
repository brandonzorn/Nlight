from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)
from qfluentwidgets import (
    BodyLabel,
    MessageBoxBase,
    SimpleCardWidget,
    SwitchButton,
    TextEdit,
)

from nlightreader.models import Character
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.text_formatter import description_to_html
from nlightreader.utils.threads import Worker


class CharacterInfoDialog(MessageBoxBase):
    def __init__(self, character: Character, parent):
        super().__init__(parent)
        self.__character = character
        self.__catalog = get_catalog_by_id(character.catalog_id)

        self.image_frame = SimpleCardWidget()
        self.image_frame_layout = QVBoxLayout(self.image_frame)
        self.image_label = QLabel()
        self.image_frame_layout.addWidget(self.image_label)

        self.title_frame = SimpleCardWidget()
        self.title_frame_layout = QVBoxLayout(self.title_frame)
        self.name_label = BodyLabel(self.__character.name)
        self.russian_label = BodyLabel(self.__character.russian)
        self.title_frame_spacer = QSpacerItem(
            20,
            40,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding,
        )
        self.show_spoilers_switch = SwitchButton()
        self.show_spoilers_switch.setText(self.tr("Show spoilers"))
        self.show_spoilers_switch.setOnText(self.tr("Show spoilers"))
        self.show_spoilers_switch.setOffText(self.tr("Show spoilers"))
        self.show_spoilers_switch.checkedChanged.connect(
            self.update_description,
        )
        self.title_frame_layout.addWidget(self.name_label)
        self.title_frame_layout.addWidget(self.russian_label)
        self.title_frame_layout.addItem(self.title_frame_spacer)
        self.title_frame_layout.addWidget(self.show_spoilers_switch)

        self.description_text = TextEdit()
        self.description_text.setFocusPolicy(
            Qt.FocusPolicy.NoFocus,
        )
        self.description_text.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.row = QHBoxLayout()
        self.row.addWidget(self.image_frame)
        self.row.addWidget(self.title_frame)

        self.viewLayout.addLayout(self.row)
        self.viewLayout.addWidget(self.description_text)

        self.cancelButton.hide()

        self.update_description()
        Worker(self.setup_image).start()

    def closeEvent(self, arg__1):
        self.deleteLater()

    @Slot()
    def update_description(self):
        self.description_text.setHtml(
            description_to_html(
                self.__character.description,
                self.show_spoilers_switch.isChecked(),
            ),
        )

    def setup_image(self):
        self.image_label.setPixmap(
            FileManager.get_character_preview(
                self.__character,
                self.__catalog,
            ),
        )


__all__ = [
    "CharacterInfoDialog",
]
