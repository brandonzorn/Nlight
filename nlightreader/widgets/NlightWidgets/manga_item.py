import webbrowser

from PySide6.QtCore import Qt, Signal, QSize
from qfluentwidgets import ElevatedCardWidget, InfoBar

from data.ui.manga_item import Ui_Form
from nlightreader.contexts import LibraryMangaMenu
from nlightreader.items import Manga
from nlightreader.utils import Worker, get_catalog, FileManager, Database, translate


class MangaItem(ElevatedCardWidget):
    manga_clicked = Signal(Manga)
    manga_changed = Signal()

    def __init__(self, manga: Manga, *, is_added_to_lib=True, pool=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.manga = manga
        self._catalog = get_catalog(self.manga.catalog_id)()
        self.manga_pixmap = None
        self._is_added_to_lib = is_added_to_lib
        self._db: Database = Database()
        self._pool = pool
        self.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.name_lbl.setText(self.manga.get_name())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.rect().contains(event.pos()):
                self.manga_clicked.emit(self.manga)
        event.accept()

    def on_context_menu(self, pos):
        catalog = get_catalog(self.manga.catalog_id)()

        def add_to_lib():
            self._db.add_manga(self.manga)
            self._db.add_manga_library(self.manga)
            InfoBar.success(
                title=self.manga.get_name(),
                content=translate("Message", "Manga {} has been added.").format(self.manga.get_name()),
                duration=2000,
                parent=self.parentWidget(),
            )

        def remove_from_lib():
            self._db.rem_manga_library(self.manga)
            InfoBar.success(
                title=self.manga.get_name(),
                content=translate("Message", "Manga {} has been deleted.").format(self.manga.get_name()),
                duration=2000,
                parent=self.parentWidget(),
            )
            self.manga_changed.emit()

        def open_in_browser():
            webbrowser.open_new_tab(catalog.get_manga_url(self.manga))

        def remove_files():
            FileManager.remove_manga_files(self.manga, catalog)
            InfoBar.success(
                title=self.manga.get_name(),
                content=translate("Message", "Files {} have been removed.").format(self.manga.get_name()),
                duration=2000,
                parent=self.parentWidget(),
            )

        def open_local_files():
            FileManager.open_dir_in_explorer(self.manga, catalog)

        menu = LibraryMangaMenu()
        if self._is_added_to_lib and not self._catalog.is_primary:
            if self._db.check_manga_library(self.manga):
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
        max_size = QSize(size, size * 2)
        if self.size() != max_size:
            self.setFixedSize(max_size)
            self.ui.image.setMaximumSize(max_size)
        if self.manga_pixmap:
            self.set_image()

    def get_image(self):
        self.manga_pixmap = FileManager.get_manga_preview(self.manga, self._catalog)

    def set_image(self):
        pixmap = self.manga_pixmap.scaled(
            self.ui.image.maximumSize(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.ui.image.setPixmap(pixmap)

    def update_image(self):
        Worker(target=self.get_image, callback=self.set_image).start(self._pool)
