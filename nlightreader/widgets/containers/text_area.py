from typing import override

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLayout, QWidget
from qfluentwidgets import TextEdit

from data.ui.containers.text_area import Ui_TextArea
from nlightreader.widgets.containers.content_container import (
    AbstractContentContainer,
)


class TextArea(QWidget, AbstractContentContainer[str]):
    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_TextArea()
        self._ui.setupUi(self)
        self._ui.fontSizeSlider.valueChanged.connect(self._set_font_size)
        self._content_widget: TextEdit = self._ui.textContent

    @Slot(int)
    def _set_font_size(self, value: int) -> None:
        font = self._ui.textContent.font()
        font.setPointSize(value)
        self._ui.textContent.setFont(font)

    @override
    def _reset_area(self) -> None:
        self._ui.textContent.clear()

    @override
    def set_content(self, content: str) -> None:
        self._reset_area()
        self._ui.textContent.setHtml(content)

    @override
    @property
    def _content_layout(self) -> QLayout:
        return self._content_widget.parent().layout()


__all__ = ["TextArea"]
