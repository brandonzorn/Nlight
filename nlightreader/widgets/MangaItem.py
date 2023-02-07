import webbrowser

from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtWidgets import QWidget

from data.ui.manga_item import Ui_manga_item_widget
from nlightreader.contexts import LibraryMangaMenu
from nlightreader.items import Manga
from nlightreader.utils import Worker, get_catalog, get_manga_preview, Database


class MangaItem(QWidget):
    manga_clicked = Signal(Manga)
    manga_changed = Signal()

    def __init__(self, manga: Manga, *, is_added_to_lib=True, pool=None):
        super().__init__()
        self.ui = Ui_manga_item_widget()
        self.ui.setupUi(self)
        self.manga = manga
        self.manga_pixmap = None
        self._is_added_to_lib = is_added_to_lib
        self._db: Database = Database()
        self._pool = pool
        self.ui.manga_item_frame.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.name_lbl.setText(self.manga.get_name())
        self.update_image()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.rect().contains(event.pos()):
                self.manga_clicked.emit(self.manga)
        event.accept()

    def enterEvent(self, event):
        self.ui.manga_widget.setProperty('is_set', 1)
        self.style().polish(self.ui.manga_item_frame)
        self.style().polish(self.ui.name_lbl)
        self.style().polish(self.ui.image)

    def leaveEvent(self, event):
        self.ui.manga_widget.setProperty('is_set', 0)
        self.style().polish(self.ui.manga_item_frame)
        self.style().polish(self.ui.name_lbl)
        self.style().polish(self.ui.image)

    def on_context_menu(self, pos):
        def add_to_lib():
            self._db.add_manga(self.manga)
            self._db.add_manga_library(self.manga)

        def remove_from_lib():
            self._db.rem_manga_library(self.manga)
            self.manga_changed.emit()

        def open_in_browser():
            webbrowser.open_new_tab(get_catalog(self.manga.catalog_id)().get_manga_url(self.manga))

        menu = LibraryMangaMenu()
        if self._is_added_to_lib:
            if self._db.check_manga_library(self.manga):
                menu.set_mode(1)
            else:
                menu.set_mode(0)
        else:
            menu.set_mode(-1)
        menu.add_to_lib.triggered.connect(add_to_lib)
        menu.remove_from_lib.triggered.connect(remove_from_lib)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.exec(self.ui.manga_item_frame.mapToGlobal(pos))

    def set_size(self, size: int):
        max_size = QSize(size, size * 2)
        self.setFixedSize(max_size)
        self.ui.image.setMaximumSize(max_size)
        if self.manga_pixmap:
            self.set_image()

    def get_image(self):
        catalog = get_catalog(self.manga.catalog_id)()
        self.manga_pixmap = get_manga_preview(self.manga, catalog)

    def set_image(self):
        pixmap = self.manga_pixmap.scaled(self.ui.image.maximumSize(), Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
        self.ui.image.setPixmap(pixmap)

    def update_image(self):
        Worker(target=self.get_image, callback=self.set_image).start(self._pool)
