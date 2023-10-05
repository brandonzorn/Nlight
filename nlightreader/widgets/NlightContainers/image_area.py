from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from data.ui.containers.image_area import Ui_Form


class ImageArea(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._image_pixmap = None

    def install(self, parent):
        parent.addWidget(self)

    def resizeEvent(self, arg__1):
        super().resizeEvent(arg__1)
        if (self._image_pixmap is None) or (arg__1.oldSize() == arg__1.size()):
            return
        view_w = self.ui.scrollArea.viewport().width()
        self.ui.img_lbl.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.resize(self.ui.scrollArea.viewport().size())
        self.update_image()

    def reset_area(self):
        self.ui.img_lbl.clear()
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.scrollArea.horizontalScrollBar().setValue(0)
        view_w = self.ui.scrollArea.viewport().width()
        self.ui.img_lbl.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.resize(self.ui.scrollArea.viewport().size())

    def _resize_pixmap(self, pixmap: QPixmap) -> QPixmap:
        if pixmap is None or pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            pixmap = pixmap.scaled(
                self.ui.scrollArea.viewport().size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        else:
            w = self.ui.scrollArea.viewport().width()
            h = pixmap.height()
            pixmap = pixmap.scaled(
                QSize(w, h),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        return pixmap

    def update_image(self):
        pixmap = self._resize_pixmap(self._image_pixmap)
        self.ui.img_lbl.setPixmap(pixmap)

    def set_image(self, img_pixmap: QPixmap):
        self._image_pixmap = img_pixmap
        self.reset_area()
        self.update_image()

    def set_text(self, text: str):
        self.ui.img_lbl.setText(text)
