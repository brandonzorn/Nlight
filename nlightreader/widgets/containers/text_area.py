from typing import override

from PySide6.QtCore import QMargins, Qt, Slot
from PySide6.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout, QWidget
from qfluentwidgets import SimpleCardWidget, Slider, TextEdit

from nlightreader.widgets.containers.content_container import (
    AbstractContentContainer,
)


class TextArea(QWidget, AbstractContentContainer[str]):
    _MIN_FONT_SIZE = 8
    _MAX_FONT_SIZE = 32
    _DEFAULT_FONT_SIZE = 14

    def __init__(self) -> None:
        super().__init__()
        self._setup_ui()
        self._setup_connections()

    def _setup_ui(self) -> None:
        margins = QMargins(0, 0, 0, 0)

        self._fontSizeWidget = SimpleCardWidget(self)
        self._fontSizeSlider = Slider(
            Qt.Orientation.Horizontal,
            self._fontSizeWidget,
        )
        self._fontSizeSlider.setRange(self._MIN_FONT_SIZE, self._MAX_FONT_SIZE)
        self._fontSizeSlider.setValue(self._DEFAULT_FONT_SIZE)

        self._fontSizeLayout = QHBoxLayout(self._fontSizeWidget)
        self._fontSizeLayout.setContentsMargins(margins)
        self._fontSizeLayout.addWidget(self._fontSizeSlider)

        self._contentWidget = SimpleCardWidget(self)
        self._contentText = TextEdit(self._contentWidget)
        self._contentText.setReadOnly(True)

        self._contentLayout = QHBoxLayout(self._contentWidget)
        self._contentLayout.setContentsMargins(margins)
        self._contentLayout.addWidget(self._contentText)

        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self._fontSizeWidget)
        self._layout.addWidget(self._contentWidget)

    def _setup_connections(self) -> None:
        self._fontSizeSlider.valueChanged.connect(self._set_font_size)

    @Slot(int)
    def _set_font_size(self, value: int) -> None:
        font = self._contentText.font()
        font.setPixelSize(value)
        self._contentText.setFont(font)

    @override
    def _reset_area(self) -> None:
        self._contentText.clear()

    @override
    def set_content(self, content: str) -> None:
        self._reset_area()
        self._contentText.setHtml(content)

    @override
    @property
    def _content_layout(self) -> QLayout:
        return self._contentLayout

    @override
    @property
    def _content_widget(self) -> QWidget:
        return self._contentText


__all__ = ["TextArea"]
