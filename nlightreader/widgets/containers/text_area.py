from typing import override

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from data.ui.containers.text_area import Ui_TextArea
from nlightreader.widgets.containers.content_container import (
    AbstractContentContainer,
)


class TextArea(QWidget, AbstractContentContainer[str]):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_TextArea()
        self.ui.setupUi(self)
        self.ui.fontSizeSlider.valueChanged.connect(self._update_text_size)
        self._content_widget = self.ui.textContent

    @Slot()
    def _update_text_size(self) -> None:
        font = self.ui.textContent.font()
        font.setPointSize(self.ui.fontSizeSlider.value())
        self.ui.textContent.setFont(font)

    @override
    def _reset_area(self) -> None:
        self.ui.textContent.clear()

    @override
    def set_content(self, content: str) -> None:
        self._reset_area()
        self.ui.textContent.setHtml(content)

    @override
    def get_content_widget(self) -> QWidget:
        return self.ui.textCard


__all__ = ["TextArea"]
