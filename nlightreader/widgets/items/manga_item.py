import webbrowser

from PySide6 import QtGui
from PySide6.QtCore import QRect, QSize, Qt, Signal
from PySide6.QtGui import QColor, QImage, QPainter, QPixmap
from PySide6.QtWidgets import QWidget
from qfluentwidgets import InfoBar

from data.ui.manga_item import Ui_Form
from nlightreader.models import Manga
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.database import Database
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.threads import Worker
from nlightreader.utils.translator import translate
from nlightreader.widgets.contexts import LibraryMangaMenu


class MangaItem(QWidget):
    manga_clicked = Signal(Manga)
    manga_changed = Signal()

    def __init__(self, manga: Manga, *, is_added_to_lib=True, pool=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__manga = manga
        self.__catalog = get_catalog_by_id(self.__manga.catalog_id)
        self.__manga_pixmap: QPixmap | None = None
        self.__is_added_to_lib = is_added_to_lib
        self.__db: Database = Database()
        self.__pool = pool
        self.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.name_lbl.setText(self.__manga.get_name())

    def enterEvent(self, event):
        super().enterEvent(event)
        if self.isEnabled():
            self.set_image(0.3)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.set_image(1.0)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            if self.rect().contains(event.pos()):
                self.manga_clicked.emit(self.__manga)

    def on_context_menu(self, pos):
        manga_title = self.__manga.get_name()
        info_bar_parent = self.parentWidget().parentWidget()
        info_bar_duration = 2000

        def add_to_lib():
            self.__db.add_manga(self.__manga)
            self.__db.add_manga_library(self.__manga)
            InfoBar.success(
                title=manga_title,
                content=translate(
                    "Message",
                    "Manga {} has been added.",
                ).format(self.__manga.get_name()),
                duration=info_bar_duration,
                parent=info_bar_parent,
            )

        def remove_from_lib():
            self.__db.rem_manga_library(self.__manga)
            InfoBar.success(
                title=manga_title,
                content=translate(
                    "Message",
                    "Manga {} has been deleted.",
                ).format(self.__manga.get_name()),
                duration=info_bar_duration,
                parent=info_bar_parent,
            )
            self.manga_changed.emit()

        def open_in_browser():
            webbrowser.open_new_tab(self.__catalog.get_manga_url(self.__manga))

        def remove_files():
            FileManager.remove_manga_files(self.__manga, self.__catalog)
            InfoBar.success(
                title=manga_title,
                content=translate(
                    "Message",
                    "Files {} have been removed.",
                ).format(self.__manga.get_name()),
                duration=info_bar_duration,
                parent=info_bar_parent,
            )

        def open_local_files():
            FileManager.open_dir_in_explorer(self.__manga, self.__catalog)

        menu = LibraryMangaMenu()
        if self.__is_added_to_lib and not self.__catalog.is_primary:
            if self.__db.check_manga_library(self.__manga):
                menu.set_mode(1)
            else:
                menu.set_mode(0)
        else:
            menu.set_mode(2)
        menu.add_to_lib.triggered.connect(add_to_lib)
        menu.remove_from_lib.triggered.connect(remove_from_lib)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.remove_files.triggered.connect(remove_files)
        menu.open_local_files.triggered.connect(open_local_files)
        menu.exec(self.mapToGlobal(pos))

    def set_size(self, size: int):
        current_size = self.size()
        max_size = QSize(size, int(size * 1.5))
        if current_size != max_size:
            self.setFixedWidth(max_size.width())
            self.ui.image_card.setFixedSize(max_size)
            self.ui.image.setMaximumSize(max_size)
        if self.__manga_pixmap:
            self.set_image()

    def get_image(self):
        self.__manga_pixmap = FileManager.get_manga_preview(
            self.__manga,
            self.__catalog,
        )

    def set_image(self, opacity: float = 1.0):
        if not self.__manga_pixmap:
            return
        device_pixel_ratio = self.devicePixelRatio()
        image_maximum_size = self.ui.image.maximumSize() * device_pixel_ratio

        image = QImage(
            image_maximum_size,
            QImage.Format.Format_ARGB32,
        )
        image.fill(QColor(0, 0, 0, 0))

        painter = QPainter(image)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing,
            True,
        )
        painter.setRenderHint(
            QPainter.RenderHint.SmoothPixmapTransform,
            True,
        )

        path = QtGui.QPainterPath()
        path.addRoundedRect(
            QRect(
                0,
                0,
                image.width(),
                image.height(),
            ),
            10,
            10,
        )

        painter.setClipPath(path)
        painter.setOpacity(opacity if opacity else 1.0)

        scaled_pixmap = self.__manga_pixmap.scaled(image_maximum_size)

        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()

        result_pixmap = QPixmap.fromImage(image)
        result_pixmap.setDevicePixelRatio(device_pixel_ratio)
        self.ui.image.setPixmap(result_pixmap)

    def update_image(self):
        Worker(
            target=self.get_image,
            callback=self.set_image,
        ).start(self.__pool)


__all__ = [
    "MangaItem",
]
