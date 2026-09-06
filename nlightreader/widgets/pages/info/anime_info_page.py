import logging
from typing import override

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTreeWidgetItem, QWidget

from nlightreader.models import Episode, Manga
from nlightreader.utils.kodik_server import start_html_video
from nlightreader.widgets.items import ModelTreeItem
from nlightreader.widgets.pages.info.base_info_page import BaseInfoPage

logger = logging.getLogger(__name__)


class AnimeInfoPage(BaseInfoPage):
    def __init__(self, parent: QWidget, manga: Manga) -> None:
        super().__init__(parent, manga)
        self._chapters: list[Episode] = []

    @override
    def get_chapters(self) -> None:
        try:
            self._chapters = self._catalog.get_episodes(self._manga)
        except NotImplementedError:
            logger.warning(
                "get_episodes is not implemented for %s",
                self._catalog.CATALOG_NAME,
            )
            self._chapters.clear()
            return
        self._chapters.reverse()
        self._group_chapters()
        self._db.episodes.save_many(self._chapters, self._manga.id)

    @Slot(QTreeWidgetItem)
    def _open_reader_window(self, item: QTreeWidgetItem) -> None:
        if not isinstance(item, ModelTreeItem):
            return
        selected_model: Episode = item.model
        if isinstance(selected_model, Episode):
            start_html_video(self._manga, selected_model)
