from typing import override

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QCloseEvent, QPixmap
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
from qfluentwidgets import (
    BodyLabel,
    MessageBoxBase,
    SimpleCardWidget,
    SwitchButton,
    TextEdit,
)

from models import Character
from utils.catalog_manager import get_catalog_by_id
from utils.file_manager import FileManager
from utils.text_formatter import description_to_html
from utils.threads import NWorker


class CharacterInfoDialog(MessageBoxBase):
    def __init__(self, character: Character, parent: QWidget) -> None:
        super().__init__(parent)
        self._character = character
        self._catalog = get_catalog_by_id(character.catalog_id)
        self._preview_image = QPixmap()

        self._setup_ui()
        self._setup_connections()

        self.update_description()
        NWorker(
            self._get_character_preview,
            callback=self._update_character_preview,
        ).start()

    def _setup_ui(self) -> None:
        self.image_frame = SimpleCardWidget()
        self.image_frame_layout = QVBoxLayout(self.image_frame)
        self.image_label = QLabel()
        self.image_frame_layout.addWidget(self.image_label)

        self.title_frame = SimpleCardWidget()
        self.title_frame_layout = QVBoxLayout(self.title_frame)
        self.name_label = BodyLabel(self._character.name)
        self.russian_label = BodyLabel(self._character.russian)
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

        self.title_frame_layout.addWidget(self.name_label)
        self.title_frame_layout.addWidget(self.russian_label)
        self.title_frame_layout.addItem(self.title_frame_spacer)
        self.title_frame_layout.addWidget(self.show_spoilers_switch)

        self.description_text = TextEdit()
        self.description_text.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.description_text.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.row = QHBoxLayout()
        self.row.addWidget(self.image_frame)
        self.row.addWidget(self.title_frame)

        self.viewLayout.addLayout(self.row)
        self.viewLayout.addWidget(self.description_text)

        self.cancelButton.hide()

    def _setup_connections(self) -> None:
        self.show_spoilers_switch.checkedChanged.connect(
            self.update_description,
        )

    @override
    def closeEvent(self, arg__1: QCloseEvent, /) -> None:
        super().closeEvent(arg__1)
        self.deleteLater()

    @Slot()
    def update_description(self) -> None:
        self.description_text.setHtml(
            description_to_html(
                self._character.description,
                self.show_spoilers_switch.isChecked(),
            ),
        )

    def _get_character_preview(self) -> None:
        self._preview_image = FileManager.get_character_preview(
            self._character,
            self._catalog,
        )

    def _update_character_preview(self) -> None:
        if self._preview_image.isNull():
            self.image_frame.hide()
            return
        self.image_label.setPixmap(self._preview_image)


__all__ = ["CharacterInfoDialog"]
