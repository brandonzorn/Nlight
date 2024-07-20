from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from data.ui.containers.image_area import Ui_Form
from nlightreader.widgets.NlightContainers.content_container import (
    AbstractContentContainer,
)


class ImageArea(QWidget, AbstractContentContainer):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setStyleSheet(
            """
            QWidget {background: transparent;}
            QScrollArea {border: none;}
            """,
        )
        self._content_widget = self.ui.img_lbl
        self.__image_pixmap = None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if (self.__image_pixmap is None) or (event.oldSize() == event.size()):
            return
        view_w = self.ui.scrollArea.viewport().width()
        self.ui.img_lbl.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.resize(
            self.ui.scrollArea.viewport().size(),
        )
        self.__update_image()

    def _reset_area(self):
        self.ui.img_lbl.clear()
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.scrollArea.horizontalScrollBar().setValue(0)
        view_w = self.ui.scrollArea.viewport().width()
        self.ui.img_lbl.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.setFixedWidth(view_w)
        self.ui.scrollAreaWidgetContents.resize(
            self.ui.scrollArea.viewport().size(),
        )

    def _resize_pixmap(self, pixmap: QPixmap) -> QPixmap:
        if pixmap is None or pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            w, h = self.ui.scrollArea.viewport().size().toTuple()
            self.ui.scrollArea.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff,
            )
        else:
            w, h = self.ui.scrollArea.viewport().width(), pixmap.height()
            self.ui.scrollArea.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAsNeeded,
            )
        return pixmap.scaled(
            QSize(w, h),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def __update_image(self):
        pixmap = self._resize_pixmap(self.__image_pixmap)
        self.ui.img_lbl.setPixmap(pixmap)

    def set_content(self, img_pixmap: QPixmap):
        self.__image_pixmap = img_pixmap
        self._reset_area()
        self.__update_image()

    def get_content_widget(self):
        return self.ui.img_lbl.parent()
