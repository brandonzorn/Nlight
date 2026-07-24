from typing import override
import webbrowser

from PySide6.QtCore import (
    QEvent,
    QPoint,
    QRect,
    QSize,
    Qt,
    QThreadPool,
    Signal,
)
from PySide6.QtGui import (
    QColor,
    QEnterEvent,
    QImage,
    QMouseEvent,
    QPainter,
    QPainterPath,
    QPixmap,
)
from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget
from qfluentwidgets import InfoBar

from data.ui.manga_item import Ui_MangaItem
from nlightreader.models import Manga
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.database import Database
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.threads import Worker
from nlightreader.widgets.contexts import LibraryMangaMenu, LibraryMenuMode


class MangaItem(QWidget):
    _HOVERED_OPACITY = 0.3

    manga_clicked = Signal(Manga)
    manga_changed = Signal()

    def __init__(
        self,
        manga: Manga,
        *,
        is_added_to_lib: bool = True,
        pool: QThreadPool | None = None,
    ) -> None:
        super().__init__()
        self.ui = Ui_MangaItem()
        self.ui.setupUi(self)

        self.customContextMenuRequested.connect(self.on_context_menu)
        self._opacity_effect = QGraphicsOpacityEffect(
            self.ui.imageLabel,
            opacity=self._HOVERED_OPACITY,
        )
        self._opacity_effect.setEnabled(False)

        self._manga = manga
        self._catalog = get_catalog_by_id(self._manga.catalog_id)
        self._manga_pixmap: QPixmap | None = None
        self._is_added_to_lib = is_added_to_lib
        self._db: Database = Database()
        self._pool = pool

        self.ui.imageLabel.setGraphicsEffect(self._opacity_effect)
        self.ui.nameLabel.setText(self._manga.get_name())

    @override
    def enterEvent(self, event: QEnterEvent) -> None:
        super().enterEvent(event)
        if self.isEnabled():
            self._opacity_effect.setEnabled(True)

    @override
    def leaveEvent(self, event: QEvent, /) -> None:
        super().leaveEvent(event)
        self._opacity_effect.setEnabled(False)

    @override
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        if event.button() != Qt.MouseButton.LeftButton:
            return
        if self.rect().contains(event.pos()):
            self.manga_clicked.emit(self._manga)

    def on_context_menu(self, pos: QPoint) -> None:
        manga_title = self._manga.get_name()
        info_bar_duration = 2000

        def add_to_lib() -> None:
            self._db.add_manga(self._manga)
            self._db.add_manga_library(self._manga)
            InfoBar.success(
                title=manga_title,
                content=self.tr(
                    "Manga {} has been added.",
                ).format(self._manga.get_name()),
                duration=info_bar_duration,
                parent=self.window(),
            )

        def remove_from_lib() -> None:
            self._db.rem_manga_library(self._manga)
            InfoBar.success(
                title=manga_title,
                content=self.tr(
                    "Manga {} has been deleted.",
                ).format(self._manga.get_name()),
                duration=info_bar_duration,
                parent=self.window(),
            )
            self.manga_changed.emit()

        def open_in_browser() -> None:
            webbrowser.open_new_tab(self._catalog.get_manga_url(self._manga))

        def remove_files() -> None:
            FileManager.remove_manga_files(self._manga, self._catalog)
            InfoBar.success(
                title=manga_title,
                content=self.tr(
                    "Files {} have been removed.",
                ).format(self._manga.get_name()),
                duration=info_bar_duration,
                parent=self.window(),
            )

        def open_local_files() -> None:
            FileManager.open_dir_in_explorer(self._manga, self._catalog)

        menu = LibraryMangaMenu()
        if self._is_added_to_lib and not self._catalog.is_primary:
            if self._db.check_manga_library(self._manga):
                menu.set_mode(LibraryMenuMode.IN_LIBRARY)
            else:
                menu.set_mode(LibraryMenuMode.NOT_IN_LIBRARY)
        else:
            menu.set_mode(LibraryMenuMode.LOCAL_ONLY)
        menu.add_to_lib.triggered.connect(add_to_lib)
        menu.remove_from_lib.triggered.connect(remove_from_lib)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.remove_files.triggered.connect(remove_files)
        menu.open_local_files.triggered.connect(open_local_files)
        menu.exec(self.mapToGlobal(pos))

    def set_size(self, size: int) -> None:
        max_size = QSize(size, int(size * 1.5))
        if self.size() != max_size:
            self.setFixedWidth(max_size.width())
            self.ui.imageCardWidget.setFixedSize(max_size)
            self.ui.imageLabel.setMaximumSize(max_size)
        if self._manga_pixmap:
            self.set_image()

    def get_image(self) -> None:
        self._manga_pixmap = FileManager.get_manga_preview(
            self._manga,
            self._catalog,
        )

    def set_image(self) -> None:
        if not self._manga_pixmap:
            return
        pixel_ratio = self.devicePixelRatio()
        result_image_size = self.ui.imageLabel.maximumSize() * pixel_ratio

        result_image = QImage(result_image_size, QImage.Format.Format_ARGB32)
        result_image.fill(QColor(0, 0, 0, 0))

        painter = QPainter(result_image)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(
            QRect(
                0,
                0,
                result_image.width(),
                result_image.height(),
            ),
            10,
            10,
        )

        painter.setClipPath(path)

        scaled_pixmap = self._manga_pixmap.scaled(result_image_size)

        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()

        result_pixmap = QPixmap.fromImage(result_image)
        result_pixmap.setDevicePixelRatio(pixel_ratio)
        self.ui.imageLabel.setPixmap(result_pixmap)

    def update_image(self) -> None:
        Worker(
            target=self.get_image,
            callback=self.set_image,
        ).start(self._pool)


__all__ = ["MangaItem"]
