import logging
import time
from typing import override

from PySide6.QtCore import Qt, qtTrId, Slot
from PySide6.QtGui import QKeyEvent, QPixmap
from PySide6.QtWidgets import QListWidgetItem
from qfluentwidgets import (
    FluentIcon,
    SimpleCardWidget,
)

from data.ui.widgets.reader import Ui_ReaderWidget
from nlightreader.consts.colors import ItemsIcons
from nlightreader.core.enums import MangaKind
from nlightreader.core.exceptions.parser_content_exc import (
    BaseContentError,
    FetchContentError,
    NoContentError,
)
from nlightreader.database import Database
from nlightreader.items import HistoryNote
from nlightreader.models import Chapter, Image, ImageStub, Manga
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.threads import NThread
from nlightreader.widgets.containers import TextArea
from nlightreader.widgets.containers.content_container import (
    AbstractContentContainer,
    ContentContainerState,
)
from nlightreader.widgets.containers.image_area import ImageArea
from nlightreader.widgets.items import ModelListItem

logger = logging.getLogger(__name__)


class ReaderWindow(SimpleCardWidget):
    def __init__(self, manga: Manga, chapters: list[Chapter]) -> None:
        super().__init__()
        self._ui = Ui_ReaderWidget()
        self._ui.setupUi(self)

        self.setStyleSheet(
            """
            QWidget {background: transparent;}
            QScrollArea {border: none;}
            """,
        )
        self._set_image_thread = NThread(
            target=self.get_content,
            callback=self.update_image,
            error_callback=self._process_errors,
        )

        self._db = Database()

        self._manga = manga
        self._chapters: list[Chapter] = chapters
        self._images: list[Image] = []
        self._catalog = get_catalog_by_id(manga.catalog_id)

        self._cur_chapter = 1
        self._max_chapters = len(self._chapters)
        self._cur_page = 1
        self._max_page = 1

        self._setup_ui()
        self._setup_connections()

    def _setup_ui(self) -> None:
        self.setWindowTitle(self._manga.name)
        self._ui.chaptersCard.hide()

        self._ui.fullscreenButton.setIcon(FluentIcon.FULL_SCREEN)
        self._ui.chaptersListButton.setIcon(FluentIcon.TILES)
        self._ui.next_page_btn.setIcon(FluentIcon.RIGHT_ARROW)
        self._ui.prev_page_btn.setIcon(FluentIcon.LEFT_ARROW)
        self._ui.next_chapter_btn.setIcon(FluentIcon.UP)
        self._ui.prev_chapter_btn.setIcon(FluentIcon.DOWN)

        self._content_container: AbstractContentContainer = (
            TextArea()
            if (self._manga.kind == MangaKind.RANOBE)
            else ImageArea()
        )
        self._content_container.install(self._ui.reader_layout)

    def _setup_connections(self) -> None:
        self._ui.next_page_btn.clicked.connect(self.turn_page_next)
        self._ui.prev_page_btn.clicked.connect(self.turn_page_prev)

        self._ui.next_chapter_btn.clicked.connect(self.turn_chapter_next)
        self._ui.prev_chapter_btn.clicked.connect(self.turn_chapter_prev)

        self._ui.fullscreenButton.clicked.connect(self.change_fullscreen)
        self._ui.chaptersListButton.clicked.connect(
            self.change_chapters_list_visible,
        )

        self._ui.chaptersList.currentItemChanged.connect(self.change_chapter)

    def setup(self, cur_chapter: int = 1) -> None:
        self._cur_chapter = cur_chapter
        self.showMaximized()
        self.update_chapters_list()
        self.update_chapter()

    @override
    def keyPressEvent(self, event: QKeyEvent) -> None:
        super().keyPressEvent(event)
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    @Slot()
    def change_fullscreen(self) -> None:
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    @Slot()
    def change_chapters_list_visible(self) -> None:
        self._ui.chaptersCard.setVisible(
            not self._ui.chaptersCard.isVisible(),
        )

    @Slot()
    def change_chapter(self, item: QListWidgetItem) -> None:
        self._cur_chapter = self._chapters.index(item.model) + 1
        self.update_chapter()

    def update_chapters_list(self) -> None:
        self._ui.chaptersList.clear()
        for chapter in self._chapters:
            ch_item = ModelListItem(chapter)
            if self._db.history.exists(chapter.id):
                if self._db.history.is_completed(chapter.id):
                    ch_item.setIcon(ItemsIcons.READ.qicon())
                else:
                    ch_item.setIcon(ItemsIcons.UNREAD)
            self._ui.chaptersList.addItem(ch_item)

    @Slot()
    def turn_page_next(self) -> None:
        self._db.history.save(
            HistoryNote(
                self._current_chapter,
                self._manga,
                False,
            ),
        )
        if self._cur_page == self._max_page:
            self._db.history.save(
                HistoryNote(
                    self._current_chapter,
                    self._manga,
                    True,
                ),
            )
            self.turn_chapter_next()
        else:
            self._cur_page += 1
            self.update_page()

    @Slot()
    def turn_page_prev(self) -> None:
        self._db.history.save(
            HistoryNote(
                self._current_chapter,
                self._manga,
                False,
            ),
        )
        if self._cur_page == 1:
            self._db.history.delete_by_chapter(self._current_chapter.id)
            self.turn_chapter_prev()
        else:
            self._cur_page -= 1
            self.update_page()

    def update_page(self) -> None:
        self._ui.pageLabel.setText(
            f"{qtTrId('label.Page')} {self._cur_page} / {self._max_page}",
        )
        self.attach_image()

    @Slot()
    def turn_chapter_next(self) -> None:
        self._db.history.save(
            HistoryNote(
                self._current_chapter,
                self._manga,
                True,
            ),
        )
        if self._cur_chapter == self._max_chapters:
            self.close()
        else:
            self._cur_chapter += 1
        self.update_chapter()

    @Slot()
    def turn_chapter_prev(self) -> None:
        if self._cur_chapter == 1:
            return
        self._cur_chapter -= 1
        self.update_chapter()

    def update_chapter(self) -> None:
        self._cur_page = 1
        self.get_images()
        self.update_page()
        self._ui.chapterLabel.setText(self._current_chapter.get_name())

    def attach_image(self) -> None:
        self._set_image_thread.terminate()
        self._set_image_thread.wait()
        if not self._images:
            return
        self._content_container.set_state(ContentContainerState.FETCH_CONTENT)
        self._set_image_thread.start()

    def _process_errors(self, e: BaseContentError) -> None:
        if isinstance(e, FetchContentError):
            logger.error(e)
            self._content_container.set_state(
                ContentContainerState.FETCH_ERROR,
            )
        elif isinstance(e, NoContentError):
            logger.warning(e)
            self._content_container.set_state(
                ContentContainerState.NO_CONTENT,
            )
        else:
            logger.error("Unhandled error %s", e)

    def get_content(self) -> str | QPixmap | None:
        page = self._cur_page
        chapter = self._cur_chapter

        if not FileManager.check_image_exists(
            self._manga,
            self._chapters[chapter - 1],
            self._images[page - 1],
            self._catalog,
        ):
            time.sleep(0.25)
            if page != self._cur_page or chapter != self._cur_chapter:
                return None

        if self._manga.kind == MangaKind.RANOBE:
            return FileManager.get_chapter_text_file(
                self._manga,
                self._chapters[chapter - 1],
                self._images[page - 1],
                self._catalog,
            )
        return FileManager.get_image_file(
            self._manga,
            self._chapters[chapter - 1],
            self._images[page - 1],
            self._catalog,
        )

    def update_image(self, content: str | QPixmap) -> None:
        self._content_container.set_state(ContentContainerState.SHOW_CONTENT)
        self._content_container.set_content(content)

    def get_images(self) -> None:
        self._images = self._catalog.get_images(
            self._manga,
            self._current_chapter,
        )
        if not self._images:
            self._images = [ImageStub()]
        self._max_page = self._images[-1].page_number

    @property
    def _current_chapter(self) -> Chapter:
        return self._chapters[self._cur_chapter - 1]


__all__ = ["ReaderWindow"]
