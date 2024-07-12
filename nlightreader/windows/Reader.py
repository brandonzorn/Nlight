import time

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidgetItem, QMainWindow
from qfluentwidgets import FluentIcon, IndeterminateProgressRing

from data.ui.windows.reader import Ui_ReaderWindow
from nlightreader.consts.colors import ItemsColors
from nlightreader.consts.enums import Nl
from nlightreader.items import Chapter, HistoryNote, Image, Manga
from nlightreader.utils import (
    Database,
    FileManager,
    get_catalog_by_id,
    get_language_icon,
    Thread,
    translate,
)
from nlightreader.widgets.NlightContainers import TextArea
from nlightreader.widgets.NlightContainers.content_container import (
    AbstractContentContainer,
)
from nlightreader.widgets.NlightContainers.image_area import ImageArea


class ReaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReaderWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(
            """
            QScrollArea {border: none;}
            """,
        )
        self.ui.fullscreen_btn.setIcon(FluentIcon.FULL_SCREEN)
        self.ui.ch_list_btn.setIcon(FluentIcon.TILES)
        self.ui.next_page_btn.setIcon(FluentIcon.RIGHT_ARROW)
        self.ui.prev_page_btn.setIcon(FluentIcon.LEFT_ARROW)
        self.ui.next_chapter_btn.setIcon(FluentIcon.UP)
        self.ui.prev_chapter_btn.setIcon(FluentIcon.DOWN)

        self.ui.next_page_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_page_btn.clicked.connect(self.turn_page_prev)

        self.ui.next_chapter_btn.clicked.connect(self.turn_chapter_next)
        self.ui.prev_chapter_btn.clicked.connect(self.turn_chapter_prev)

        self.ui.fullscreen_btn.clicked.connect(self.change_fullscreen)
        self.ui.ch_list_btn.clicked.connect(self.change_chapters_list_visible)

        self.ui.items_list.doubleClicked.connect(self.change_chapter)
        self._set_image_thread = Thread(
            target=self.get_content,
            callback=self.update_image,
        )

        self.__content_container: AbstractContentContainer | None = None

        self.__progressRing = IndeterminateProgressRing()
        self.__progressRing.setVisible(False)

        self.__db: Database = Database()
        self.__manga = None
        self.__chapters: list[Chapter] = []
        self.__images: list[Image] = []
        self.__cur_chapter = 1
        self.__max_chapters = 1
        self.__cur_page = 1
        self.__max_page = 1
        self.__catalog = None

    def setup(self, manga: Manga, chapters: list[Chapter], cur_chapter=1):
        self.ui.chapters_frame.hide()
        self.__manga = manga
        self.setWindowTitle(self.__manga.name)
        self.__content_container = (
            TextArea()
            if (self.__manga.kind == Nl.MangaKind.ranobe)
            else ImageArea()
        )
        self.__content_container.install(self.ui.reader_layout)
        (
            self.__content_container.get_content_widget()
            .parent()
            .layout()
            .addWidget(
                self.__progressRing,
            )
        )
        self.__chapters = chapters
        self.__cur_chapter = cur_chapter
        self.__max_chapters = len(chapters)
        self.__catalog = get_catalog_by_id(manga.catalog_id)
        self.showMaximized()
        self.update_chapters_list()
        self.update_chapter()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        event.accept()

    def closeEvent(self, event):
        self.deleteLater()

    @Slot()
    def change_fullscreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    @Slot()
    def change_chapters_list_visible(self):
        self.ui.chapters_frame.setVisible(
            not self.ui.chapters_frame.isVisible(),
        )

    @Slot()
    def change_chapter(self):
        self.__cur_chapter = self.ui.items_list.currentIndex().row() + 1
        self.update_chapter()

    def update_chapters_list(self):
        self.ui.items_list.clear()
        for chapter in self.__chapters:
            item = QListWidgetItem(chapter.get_name())
            if self.__db.check_complete_chapter(chapter):
                if self.__db.get_complete_status(chapter):
                    item.setBackground(ItemsColors.READ)
                else:
                    item.setBackground(ItemsColors.UNREAD)
            if chapter.language:
                item.setIcon(QIcon(get_language_icon(chapter.language)))
            self.ui.items_list.addItem(item)

    @Slot()
    def turn_page_next(self):
        self.__db.add_history_note(
            HistoryNote(
                self._current_chapter,
                self.__manga,
                False,
            ),
        )
        if self.__cur_page == self.__max_page:
            self.__db.add_history_note(
                HistoryNote(
                    self._current_chapter,
                    self.__manga,
                    True,
                ),
            )
            self.turn_chapter_next()
        else:
            self.__cur_page += 1
            self.update_page()

    @Slot()
    def turn_page_prev(self):
        self.__db.add_history_note(
            HistoryNote(
                self._current_chapter,
                self.__manga,
                False,
            ),
        )
        if self.__cur_page == 1:
            self.__db.del_history_note(self._current_chapter)
            self.turn_chapter_prev()
        else:
            self.__cur_page -= 1
            self.update_page()

    def update_page(self):
        self.ui.page_label.setText(
            f"{translate('Other', 'Page')} "
            f"{self.__cur_page} / {self.__max_page}",
        )
        self.attach_image()

    @Slot()
    def turn_chapter_next(self):
        self.__db.add_history_note(
            HistoryNote(
                self._current_chapter,
                self.__manga,
                True,
            ),
        )
        if self.__cur_chapter == self.__max_chapters:
            self.deleteLater()
        else:
            self.__cur_chapter += 1
        self.update_chapter()

    @Slot()
    def turn_chapter_prev(self):
        if self.__cur_chapter == 1:
            return
        self.__cur_chapter -= 1
        self.update_chapter()

    def update_chapter(self):
        self.__cur_page = 1
        self.get_images()
        self.update_page()
        self.ui.chapter_label.setText(self._current_chapter.get_name())

    def attach_image(self):
        self._set_image_thread.terminate()
        self._set_image_thread.wait()
        if not self.__images:
            return
        self.__progressRing.setVisible(True)
        self.__progressRing.start()
        self.__content_container.get_content_widget().setVisible(False)
        self._set_image_thread.start()

    def get_content(self):
        page = self.__cur_page
        chapter = self.__cur_chapter

        if not FileManager.check_image_exists(
            self.__manga,
            self.__chapters[chapter - 1],
            self.__images[page - 1],
            self.__catalog,
        ):
            time.sleep(0.25)
            if page != self.__cur_page or chapter != self.__cur_chapter:
                return

        if self.__manga.kind == Nl.MangaKind.ranobe:
            return FileManager.get_chapter_text_file(
                self.__manga,
                self.__chapters[chapter - 1],
                self.__images[page - 1],
                self.__catalog,
            )
        return FileManager.get_image_file(
            self.__manga,
            self.__chapters[chapter - 1],
            self.__images[page - 1],
            self.__catalog,
        )

    def update_image(self, content):
        self.__progressRing.stop()
        self.__progressRing.setVisible(False)
        self.__content_container.get_content_widget().setVisible(True)
        self.__content_container.set_content(content)

    def get_images(self):
        chapter = self._current_chapter
        self.__images = self.__catalog.get_images(self.__manga, chapter)
        if not self.__images:
            self.__images = [Image.get_empty_instance()]
        self.__max_page = self.get_chapter_pages()

    def get_chapter_pages(self) -> int:
        return self.__images[-1].page

    @property
    def _current_chapter(self) -> Chapter:
        return self.__chapters[self.__cur_chapter - 1]
