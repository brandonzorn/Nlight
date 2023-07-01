from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QScrollArea, QLabel, QWidget, QVBoxLayout


class ImageArea(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.setFocusPolicy(Qt.NoFocus)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._scrollAreaWidgetContents = QWidget()
        self._scrollAreaWidgetContents.setAutoFillBackground(True)
        self._scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")

        self._scroll_layout = QVBoxLayout(self._scrollAreaWidgetContents)

        self._scroll_layout.setSpacing(6)
        self._scroll_layout.setContentsMargins(0, 0, 0, 0)

        self._img_lbl = QLabel(self._scrollAreaWidgetContents)
        self._img_lbl.setAlignment(Qt.AlignCenter)
        self._img_lbl.setTextInteractionFlags(Qt.NoTextInteraction)

        self._scroll_layout.addWidget(self._img_lbl)
        self.setWidget(self._scrollAreaWidgetContents)

        self._image_pixmap = None

    def install(self, parent):
        parent.addWidget(self)

    def resizeEvent(self, arg__1):
        super().resizeEvent(arg__1)
        if (self._image_pixmap is None) or (arg__1.oldSize() == arg__1.size()):
            return
        self._img_lbl.clear()

        view_w = self.viewport().width()
        self._img_lbl.setFixedWidth(view_w)
        self._scrollAreaWidgetContents.setFixedWidth(view_w)

        self._scrollAreaWidgetContents.resize(self.viewport().size())

        self.update_image()

    def reset_area(self):
        self._img_lbl.clear()
        self.verticalScrollBar().setValue(0)
        self.horizontalScrollBar().setValue(0)
        self._scrollAreaWidgetContents.resize(self.viewport().size())

    def _resize_pixmap(self, pixmap: QPixmap) -> QPixmap:
        if pixmap is None or pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            pixmap = pixmap.scaled(self.viewport().size(), Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        else:
            w = self.viewport().width()
            h = pixmap.height()
            pixmap = pixmap.scaled(QSize(w, h), Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        return pixmap

    def update_image(self):
        pixmap = self._resize_pixmap(self._image_pixmap)
        self._img_lbl.setPixmap(pixmap)

    def set_image(self, img_pixmap: QPixmap):
        self._image_pixmap = img_pixmap
        self.reset_area()
        self.update_image()

    def set_text(self, text: str):
        self._img_lbl.setText(text)
