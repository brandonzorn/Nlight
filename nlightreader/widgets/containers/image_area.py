from typing import override

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QResizeEvent
from PySide6.QtWidgets import QLabel, QLayout, QWidget

from data.ui.containers.image_area import Ui_ImageArea
from nlightreader.widgets.containers.content_container import (
    AbstractContentContainer,
)


class ImageArea(QWidget, AbstractContentContainer[QPixmap]):
    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_ImageArea()
        self._ui.setupUi(self)

        self._content_widget: QLabel = self._ui.imageLabel
        self._image_pixmap = QPixmap()

    @override
    def resizeEvent(self, event: QResizeEvent, /) -> None:
        super().resizeEvent(event)
        if event.oldSize() == event.size():
            return
        self._adjust_content_size()
        self._update_image()

    def _adjust_content_size(self) -> None:
        view_w = self._ui.scrollArea.viewport().width()
        self._ui.imageLabel.setFixedWidth(view_w)
        self._ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self._ui.scrollAreaWidgetContents.resize(
            self._ui.scrollArea.viewport().size(),
        )

    @override
    def _reset_area(self) -> None:
        self._image_pixmap = QPixmap()
        self._ui.imageLabel.clear()
        self._ui.scrollArea.verticalScrollBar().setValue(0)
        self._ui.scrollArea.horizontalScrollBar().setValue(0)

        self._adjust_content_size()

    def _resize_pixmap(self, pixmap: QPixmap) -> QPixmap:
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            viewport_size = self._ui.scrollArea.viewport().size()
            self._ui.scrollArea.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff,
            )
        else:
            viewport_size = QSize(
                self._ui.scrollArea.viewport().width(),
                pixmap.height(),
            )
            self._ui.scrollArea.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAsNeeded,
            )
        device_pixel_ratio = self.devicePixelRatio()
        scaled_pixmap = pixmap.scaled(
            viewport_size * device_pixel_ratio,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        scaled_pixmap.setDevicePixelRatio(device_pixel_ratio)
        return scaled_pixmap

    def _update_image(self) -> None:
        if self._image_pixmap.isNull():
            return
        pixmap = self._resize_pixmap(self._image_pixmap)
        self._ui.imageLabel.setPixmap(pixmap)

    @override
    def set_content(self, content: QPixmap) -> None:
        self._reset_area()
        self._image_pixmap = content
        self._update_image()

    @override
    @property
    def _content_layout(self) -> QLayout:
        return self._content_widget.parent().layout()


__all__ = ["ImageArea"]
