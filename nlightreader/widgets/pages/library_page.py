from typing import override

from PySide6.QtWidgets import QWidget

from data.ui.widgets.library import Ui_LibraryPage
from nlightreader.core.enums import LibList
from nlightreader.models import Manga
from nlightreader.parsers import LocalLibrary
from nlightreader.widgets.items.manga_item import MangaItem
from nlightreader.widgets.pages.base_page import BaseMangaLibraryPage


class LibraryPage(BaseMangaLibraryPage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_LibraryPage()
        self._setup_ui()
        self._setup_connections()

        self.catalog = LocalLibrary()

    @override
    def _setup_ui(self) -> None:
        self._ui.setupUi(self)
        self.manga_area.install(self._ui.items_layout)

    @override
    def _setup_connections(self) -> None:
        self._ui.plannedButton.clicked.connect(
            lambda: self._change_list(LibList.PLANNED),
        )
        self._ui.readingButton.clicked.connect(
            lambda: self._change_list(LibList.READING),
        )
        self._ui.onHoldButton.clicked.connect(
            lambda: self._change_list(LibList.ON_HOLD),
        )
        self._ui.completedButton.clicked.connect(
            lambda: self._change_list(LibList.COMPLETED),
        )
        self._ui.droppedButton.clicked.connect(
            lambda: self._change_list(LibList.DROPPED),
        )
        self._ui.reReadingButton.clicked.connect(
            lambda: self._change_list(LibList.RE_READING),
        )

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(
            manga,
            parent=self,
            pool=self.manga_area.manga_thread_pool,
        )
        item.manga_clicked.connect(self.manga_open.emit)
        item.manga_changed.connect(self._get_content)
        return item


__all__ = ["LibraryPage"]
