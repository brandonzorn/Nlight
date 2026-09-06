import logging
from typing import override

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTreeWidgetItem, QWidget

from nlightreader.models import Chapter, Manga
from nlightreader.widgets.items import ModelTreeItem
from nlightreader.widgets.pages.info.base_info_page import BaseInfoPage
from nlightreader.windows.reader_window import ReaderWindow

logger = logging.getLogger(__name__)


class MangaInfoPage(BaseInfoPage):
    def __init__(self, parent: QWidget, manga: Manga) -> None:
        super().__init__(parent, manga)
        self._chapters: list[Chapter] = []
        self._reader_window = None

    @override
    def deleteLater(self, /) -> None:
        self._delete_reader_window()
        super().deleteLater()

    @override
    def get_chapters(self) -> None:
        try:
            self._chapters = self._catalog.get_chapters(self._manga)
        except NotImplementedError:
            logger.warning(
                "get_chapters is not implemented for %s",
                self._catalog.CATALOG_NAME,
            )
            self._chapters.clear()
            return
        self._chapters.reverse()
        self._group_chapters()
        self._db.chapters.save_many(self._chapters, self._manga.id)

    @Slot(QTreeWidgetItem)
    def _open_reader_window(self, item: QTreeWidgetItem) -> None:
        if not isinstance(item, ModelTreeItem):
            return
        try:
            self._delete_reader_window()
        finally:
            selected_model: Chapter = item.model
            selected_group = self._grouped_chapters[selected_model.language][
                selected_model.translator
            ]
            self._reader_window = ReaderWindow(self._manga, selected_group)
            self._reader_window.setup(selected_group.index(selected_model) + 1)

    def _delete_reader_window(self) -> None:
        if self._reader_window is not None:
            self._reader_window.close()
            self._reader_window.deleteLater()
            self._reader_window = None
