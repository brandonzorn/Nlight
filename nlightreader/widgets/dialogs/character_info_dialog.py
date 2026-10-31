from typing import override

from PySide6.QtCore import Slot
from PySide6.QtGui import QCloseEvent, QImage, QPixmap
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
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
        self._preview_image = QImage()

        self._setup_ui()
        self._setup_connections()

        self.update_description()

        self._worker = NWorker(
            self._get_character_preview,
            callback=self._update_character_preview,
        )
        self._worker.start(None)

    def _setup_ui(self) -> None:
        self.image_frame = SimpleCardWidget(self)
        self.image_frame_layout = QVBoxLayout(self.image_frame)
        self.image_label = QLabel(self.image_frame)
        self.image_frame_layout.addWidget(self.image_label)

        self.title_frame = SimpleCardWidget(self)
        self.title_frame_layout = QVBoxLayout(self.title_frame)
        self.name_label = BodyLabel(
            self._character.name,
            self.title_frame,
        )
        self.russian_label = BodyLabel(
            self._character.russian,
            self.title_frame,
        )

        self.show_spoilers_switch = SwitchButton(self.title_frame)
        spoiler_text = self.tr("Show spoilers")
        self.show_spoilers_switch.setText(spoiler_text)
        self.show_spoilers_switch.setOnText(spoiler_text)
        self.show_spoilers_switch.setOffText(spoiler_text)

        self.title_frame_layout.addWidget(self.name_label)
        self.title_frame_layout.addWidget(self.russian_label)
        self.title_frame_layout.addStretch(1)
        self.title_frame_layout.addWidget(self.show_spoilers_switch)

        self.description_text = TextEdit(self)
        self.description_text.setReadOnly(True)

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

    @Slot()
    def _update_character_preview(self) -> None:
        if self._preview_image.isNull():
            self.image_frame.hide()
            return
        result_pixmap = QPixmap.fromImage(self._preview_image)
        result_pixmap.setDevicePixelRatio(self.devicePixelRatio())
        self.image_label.setPixmap(result_pixmap)


__all__ = ["CharacterInfoDialog"]
