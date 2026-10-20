from functools import partial
from typing import override

from PySide6.QtWidgets import QWidget

from core.enums import LibList
from models import Manga
from parsers import LocalLibrary
from resources.ui.widgets.library import Ui_LibraryPage
from widgets.items.manga_item import MangaItem
from widgets.pages.base_page import BaseMangaLibraryPage


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
        button_mapping = {
            self._ui.plannedButton: LibList.PLANNED,
            self._ui.readingButton: LibList.READING,
            self._ui.onHoldButton: LibList.ON_HOLD,
            self._ui.completedButton: LibList.COMPLETED,
            self._ui.droppedButton: LibList.DROPPED,
            self._ui.reReadingButton: LibList.RE_READING,
        }

        for button, lib_list in button_mapping.items():
            button.clicked.connect(partial(self._change_list, lib_list))

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(manga, parent=self)
        item.manga_clicked.connect(self.manga_open.emit)
        item.manga_changed.connect(self._get_content)
        return item


__all__ = ["LibraryPage"]
