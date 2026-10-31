from typing import override

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QImage, QPixmap, QResizeEvent
from PySide6.QtWidgets import QLayout, QWidget

from resources.ui.containers.image_area import Ui_ImageArea
from widgets.containers.content_container import (
    AbstractContentContainer,
)


def _is_standard_aspect_ratio(image: QImage) -> bool:
    if image.height() == 0:
        return True
    return 0.5 < (image.width() / image.height()) < 2.0


class ImageArea(QWidget, AbstractContentContainer[QImage]):
    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_ImageArea()
        self._ui.setupUi(self)

        self._content_image = QImage()

    @override
    def resizeEvent(self, event: QResizeEvent, /) -> None:
        super().resizeEvent(event)
        if event.oldSize() == event.size():
            return
        self._adjust_content_size()
        self._update_image()

    def _adjust_content_size(self) -> None:
        viewport_size = self._ui.scrollArea.viewport().size()
        view_w = viewport_size.width()
        self._ui.imageLabel.setFixedWidth(view_w)
        self._ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self._ui.scrollAreaWidgetContents.resize(viewport_size)

    def _update_scroll_policy(self) -> None:
        if _is_standard_aspect_ratio(self._content_image):
            policy = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        else:
            policy = Qt.ScrollBarPolicy.ScrollBarAsNeeded

        if self._ui.scrollArea.verticalScrollBarPolicy() != policy:
            self._ui.scrollArea.setVerticalScrollBarPolicy(policy)

    @override
    def _reset_area(self) -> None:
        self._content_image = QImage()
        self._ui.imageLabel.clear()
        self._ui.scrollArea.verticalScrollBar().setValue(0)
        self._ui.scrollArea.horizontalScrollBar().setValue(0)

        self._adjust_content_size()

    def _resize_image(self, image: QImage) -> QImage:
        viewport_size = self._ui.scrollArea.viewport().size()
        if not _is_standard_aspect_ratio(image):
            viewport_size = QSize(viewport_size.width(), image.height())

        device_pixel_ratio = self.devicePixelRatio()
        scaled_image = image.scaled(
            viewport_size * device_pixel_ratio,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        scaled_image.setDevicePixelRatio(device_pixel_ratio)
        return scaled_image

    def _update_image(self) -> None:
        if self._content_image.isNull():
            return
        self._update_scroll_policy()
        scaled_image = self._resize_image(self._content_image)
        self._ui.imageLabel.setPixmap(QPixmap.fromImage(scaled_image))

    @override
    def set_content(self, content: QImage) -> None:
        self._reset_area()
        self._content_image = content
        self._update_image()

    @override
    @property
    def _content_layout(self) -> QLayout:
        return self._ui.scrollAreaHLayout

    @override
    @property
    def _content_widget(self) -> QWidget:
        return self._ui.imageLabel


__all__ = ["ImageArea"]
