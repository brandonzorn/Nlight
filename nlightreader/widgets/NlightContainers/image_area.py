from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QScrollArea, QLabel, QWidget, QVBoxLayout, QSizePolicy


class ImageArea(QScrollArea):
    def __init__(self, parent):
        super().__init__()
        self.setWidgetResizable(True)
        self.setFocusPolicy(Qt.NoFocus)
        # size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.setSizePolicy(size_policy)

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

        if parent is not None:
            parent.addWidget(self)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self._image_pixmap is None:
            return
        if event.oldSize() != event.size():
            self._img_lbl.clear()
            self._scrollAreaWidgetContents.resize(0, 0)
            self.update_image()
            event.accept()

    def reset_area(self):
        self._img_lbl.clear()
        self.verticalScrollBar().setValue(0)
        self.horizontalScrollBar().setValue(0)
        self._scrollAreaWidgetContents.resize(0, 0)

    def _resize_pixmap(self, pixmap: QPixmap) -> QPixmap:
        if pixmap is None or pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            pixmap = pixmap.scaled(self._img_lbl.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
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
