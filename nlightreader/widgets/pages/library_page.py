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
        self.ui = Ui_LibraryPage()
        self.ui.setupUi(self)

        self.ui.plannedButton.clicked.connect(
            lambda: self._change_list(LibList.planned),
        )
        self.ui.readingButton.clicked.connect(
            lambda: self._change_list(LibList.reading),
        )
        self.ui.onHoldButton.clicked.connect(
            lambda: self._change_list(LibList.on_hold),
        )
        self.ui.completedButton.clicked.connect(
            lambda: self._change_list(LibList.completed),
        )
        self.ui.droppedButton.clicked.connect(
            lambda: self._change_list(LibList.dropped),
        )
        self.ui.reReadingButton.clicked.connect(
            lambda: self._change_list(LibList.re_reading),
        )

        self.manga_area.install(self.ui.items_layout)

        self.catalog = LocalLibrary()

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(manga, pool=self.manga_area.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        item.manga_changed.connect(self._get_content)
        return item


__all__ = ["LibraryPage"]
