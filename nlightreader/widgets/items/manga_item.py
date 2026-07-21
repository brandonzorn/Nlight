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
from nlightreader.database.services.owm import Database
from nlightreader.models import Manga
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.threads import NWorker
from nlightreader.widgets.contexts import LibraryMangaMenu, LibraryMenuMode


class MangaItem(QWidget):
    _HOVERED_OPACITY = 0.3

    manga_clicked = Signal(Manga)
    manga_changed = Signal()

    def __init__(
        self,
        manga: Manga,
        *,
        parent: QWidget,
        is_added_to_lib: bool = True,
        pool: QThreadPool | None = None,
    ) -> None:
        super().__init__()
        self._ui = Ui_MangaItem()
        self._ui.setupUi(self)

        self._parent = parent
        self._pool = pool
        self._is_added_to_lib = is_added_to_lib

        self._manga = manga
        self._catalog = get_catalog_by_id(self._manga.catalog_id)
        self._manga_pixmap = QPixmap()
        self._db = Database()

        self._setup_ui()
        self._setup_connections()

    def _setup_ui(self) -> None:
        self._opacity_effect = QGraphicsOpacityEffect(
            self._ui.image_label,
            opacity=self._HOVERED_OPACITY,
        )
        self._opacity_effect.setEnabled(False)

        self._ui.image_label.setGraphicsEffect(self._opacity_effect)
        self._ui.title_label.setText(self._manga.get_name())

    def _setup_connections(self) -> None:
        self.customContextMenuRequested.connect(self.on_context_menu)

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
        menu = LibraryMangaMenu()
        if self._is_added_to_lib and not self._catalog.is_primary:
            if self._db.library.exists(self._manga.id):
                menu.set_mode(LibraryMenuMode.IN_LIBRARY)
            else:
                menu.set_mode(LibraryMenuMode.NOT_IN_LIBRARY)
        else:
            menu.set_mode(LibraryMenuMode.LOCAL_ONLY)
        menu.add_to_lib.triggered.connect(self._show_add_to_library)
        menu.remove_from_lib.triggered.connect(self._show_remove_from_library)
        menu.open_in_browser.triggered.connect(self._open_in_browser)
        menu.remove_files.triggered.connect(self._show_clear_manga_cache)
        menu.open_local_files.triggered.connect(self._open_local_files)
        menu.exec(self.mapToGlobal(pos))

    def set_size(self, size: int) -> None:
        max_size = QSize(size, int(size * 1.5))
        if self.size() != max_size:
            self.setFixedWidth(max_size.width())
            self._ui.image_card.setFixedSize(max_size)
            self._ui.image_label.setMaximumSize(max_size)
        self.set_image()

    def get_image(self) -> None:
        self._manga_pixmap = FileManager.get_manga_preview(
            self._manga,
            self._catalog,
        )

    def set_image(self) -> None:
        if self._manga_pixmap.isNull():
            return
        pixel_ratio = self.devicePixelRatio()
        result_image_size = self._ui.image_label.maximumSize() * pixel_ratio

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
        self._ui.image_label.setPixmap(result_pixmap)

    def update_image(self) -> None:
        NWorker(
            target=self.get_image,
            callback=self.set_image,
        ).start(self._pool)

    def _open_in_browser(self) -> None:
        webbrowser.open_new_tab(self._catalog.get_manga_url(self._manga))

    def _open_local_files(self) -> None:
        FileManager.open_dir_in_explorer(self._manga, self._catalog)

    def _show_add_to_library(self) -> None:
        self._db.manga.save(self._manga)
        self._db.library.save(self._manga.id)
        InfoBar.success(
            title=self._manga.get_name(),
            content=self.tr(
                "Manga {} has been added.",
            ).format(self._manga.get_name()),
            duration=2000,
            parent=self._parent,
        )

    def _show_remove_from_library(self) -> None:
        self._db.library.remove(self._manga.id)
        InfoBar.success(
            title=self._manga.get_name(),
            content=self.tr(
                "Manga {} has been deleted.",
            ).format(self._manga.get_name()),
            duration=2000,
            parent=self._parent,
        )
        self.manga_changed.emit()

    def _show_clear_manga_cache(self) -> None:
        FileManager.remove_manga_files(self._manga, self._catalog)
        InfoBar.success(
            title=self._manga.get_name(),
            content=self.tr(
                "Files {} have been removed.",
            ).format(self._manga.get_name()),
            duration=2000,
            parent=self._parent,
        )


__all__ = ["MangaItem"]
