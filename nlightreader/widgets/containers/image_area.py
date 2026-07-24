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
        self.ui = Ui_ImageArea()
        self.ui.setupUi(self)

        self._content_widget: QLabel = self.ui.imageLabel
        self._image_pixmap = None

    @override
    def resizeEvent(self, event: QResizeEvent, /) -> None:
        super().resizeEvent(event)
        if (self._image_pixmap is None) or (event.oldSize() == event.size()):
            return
        view_w = self.ui.scrollArea.viewport().width()
        self.ui.imageLabel.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.resize(
            self.ui.scrollArea.viewport().size(),
        )
        self._update_image()

    @override
    def _reset_area(self) -> None:
        self.ui.imageLabel.clear()
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.scrollArea.horizontalScrollBar().setValue(0)
        view_w = self.ui.scrollArea.viewport().width()
        self.ui.imageLabel.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.resize(
            self.ui.scrollArea.viewport().size(),
        )

    def _resize_pixmap(self, pixmap: QPixmap) -> QPixmap:
        if pixmap is None or pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            viewport_size = self.ui.scrollArea.viewport().size()
            self.ui.scrollArea.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff,
            )
        else:
            viewport_size = QSize(
                self.ui.scrollArea.viewport().width(),
                pixmap.height(),
            )
            self.ui.scrollArea.setVerticalScrollBarPolicy(
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
        pixmap = self._resize_pixmap(self._image_pixmap)
        self.ui.imageLabel.setPixmap(pixmap)

    @override
    def set_content(self, content: QPixmap) -> None:
        self._image_pixmap = content
        self._reset_area()
        self._update_image()

    @override
    @property
    def _content_layout(self) -> QLayout:
        return self._content_widget.parent().layout()


__all__ = ["ImageArea"]
