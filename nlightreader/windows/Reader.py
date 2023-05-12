import time

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow, QListWidgetItem

from data.ui.windows.reader import Ui_ReaderWindow
from nlightreader.consts import ItemsColors
from nlightreader.items import Manga, Chapter, Image, HistoryNote
from nlightreader.utils import Database, get_catalog, FileManager, translate, Worker, get_language_icon


class ReaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReaderWindow()
        self.ui.setupUi(self)

        self.ui.next_page_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_page_btn.clicked.connect(self.turn_page_prev)

        self.ui.next_chapter_btn.clicked.connect(self.turn_chapter_next)
        self.ui.prev_chapter_btn.clicked.connect(self.turn_chapter_prev)

        self.ui.fullscreen_btn.clicked.connect(self.change_fullscreen)
        self.ui.ch_list_btn.clicked.connect(self.change_chapters_list_visible)
        self.ui.text_size_slider.valueChanged.connect(self.update_text_size)

        self.ui.items_list.doubleClicked.connect(self.change_chapter)

        self.db: Database = Database()
        self.manga = None
        self.chapters: list[Chapter] = []
        self.images: list[Image] = []
        self.cur_image_pixmap = None
        self.cur_chapter = 1
        self.max_chapters = 1
        self.cur_page = 1
        self.max_page = 1
        self.catalog = None

    def setup(self, manga: Manga, chapters: list[Chapter], cur_chapter=1):
        self.showMaximized()
        self.manga = manga
        self.ui.chapters_frame.hide()
        if self.manga.kind == 'ranobe':
            self.ui.image_reader.hide()
        else:
            self.ui.text_reader.hide()
        self.chapters = chapters
        self.cur_chapter = cur_chapter
        self.max_chapters = len(chapters)
        self.catalog = get_catalog(manga.catalog_id)()
        self.setWindowTitle(self.manga.name)
        self.update_chapters_list()
        self.update_chapter()

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key.Key_Escape:
                self.close()
        event.accept()

    def resizeEvent(self, event):
        if (not self.chapters) or (self.manga and self.manga.kind == 'ranobe') or self.cur_image_pixmap is None:
            return
        self.reset_reader_area()
        self.update_image()
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
        self.ui.chapters_frame.setVisible(not self.ui.chapters_frame.isVisible())

    @Slot()
    def change_chapter(self):
        self.cur_chapter = self.ui.items_list.currentIndex().row() + 1
        self.update_chapter()

    def update_chapters_list(self):
        self.ui.items_list.clear()
        for chapter in self.chapters:
            item = QListWidgetItem(chapter.get_name())
            if self.db.check_complete_chapter(chapter):
                if self.db.get_complete_status(chapter):
                    item.setBackground(ItemsColors.READ)
                else:
                    item.setBackground(ItemsColors.UNREAD)
            if chapter.language:
                item.setIcon(QIcon(get_language_icon(chapter.language)))
            self.ui.items_list.addItem(item)

    @Slot()
    def turn_page_next(self):
        self.db.add_history_note(HistoryNote(self.chapters[self.cur_chapter - 1], self.manga, False))
        if self.cur_page == self.max_page:
            self.db.add_history_note(HistoryNote(self.chapters[self.cur_chapter - 1], self.manga, True))
            self.turn_chapter_next()
        else:
            self.cur_page += 1
            self.update_page()

    @Slot()
    def turn_page_prev(self):
        self.db.add_history_note(HistoryNote(self.chapters[self.cur_chapter - 1], self.manga, False))
        if self.cur_page == 1:
            self.db.del_history_note(self.chapters[self.cur_chapter - 1])
            self.turn_chapter_prev()
        else:
            self.cur_page -= 1
            self.update_page()

    def update_page(self):
        self.attach_image()
        self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.cur_page} / {self.max_page}")

    @Slot()
    def turn_chapter_next(self):
        self.db.add_history_note(HistoryNote(self.chapters[self.cur_chapter - 1], self.manga, True))
        if self.cur_chapter == self.max_chapters:
            self.deleteLater()
        else:
            self.cur_chapter += 1
        self.update_chapter()

    @Slot()
    def turn_chapter_prev(self):
        if self.cur_chapter == 1:
            return
        else:
            self.cur_chapter -= 1
        self.update_chapter()

    def update_chapter(self):
        self.cur_page = 1
        self.get_images()
        self.update_page()
        self.ui.chapter_label.setText(self.chapters[self.cur_chapter - 1].get_name())

    def reset_reader_area(self):
        self.ui.img.clear()
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.scrollArea.horizontalScrollBar().setValue(0)
        self.ui.scrollAreaWidgetContents.resize(0, 0)

    def attach_image(self):
        self.reset_reader_area()
        self.cur_image_pixmap = None
        if not self.images:
            return
        Worker(target=self.set_image, callback=self.update_image).start()

    def set_image(self):
        page = self.cur_page
        chapter = self.cur_chapter

        def get_image():
            if not FileManager.check_image_exists(
                    self.manga, self.chapters[chapter - 1], self.images[page - 1], self.catalog):
                time.sleep(0.25)
                if page != self.cur_page or chapter != self.cur_chapter:
                    return
                self.ui.img.setText(translate('Other', 'Page is loading'))
            if self.manga.kind == 'ranobe':
                self.cur_image_pixmap = FileManager.get_chapter_text_file(
                    self.manga, self.chapters[chapter - 1], self.images[page - 1], self.catalog)
            else:
                if not self.cur_image_pixmap:
                    self.cur_image_pixmap = FileManager.get_image_file(
                        self.manga, self.chapters[chapter - 1], self.images[page - 1], self.catalog)
        get_image()
        assert page == self.cur_page or chapter == self.cur_chapter

    def update_image(self):
        if self.manga.kind == 'ranobe':
            self.ui.text.setHtml(self.cur_image_pixmap)
        else:
            pixmap = self.resize_pixmap(self.cur_image_pixmap)
            self.ui.img.setPixmap(pixmap)

    @Slot()
    def update_text_size(self):
        font = self.ui.img.font()
        font.setPointSize(self.ui.text_size_slider.value())
        self.ui.text.setFont(font)

    def resize_pixmap(self, pixmap: QPixmap) -> QPixmap:
        if pixmap is None or pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            pixmap = pixmap.scaled(self.ui.img.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
        return pixmap

    def get_images(self):
        chapter = self.chapters[self.cur_chapter - 1]
        self.images = self.catalog.get_images(self.manga, chapter)
        if not self.images:
            self.images = [Image.get_empty_instance()]
        self.max_page = self.get_chapter_pages()

    def get_chapter_pages(self) -> int:
        return self.images[-1].page
