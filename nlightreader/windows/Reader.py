import time

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from data.ui.reader import Ui_MainWindow
from nlightreader.items import Manga, Chapter, Image
from nlightreader.utils import Database, get_catalog, get_chapter_text, get_chapter_image, translate, Worker


class Reader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.next_page_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_page_btn.clicked.connect(self.turn_page_prev)

        self.ui.next_chapter_btn.clicked.connect(self.turn_chapter_next)
        self.ui.prev_chapter_btn.clicked.connect(self.turn_chapter_prev)

        self.ui.fullscreen_btn.clicked.connect(self.change_fullscreen)
        self.ui.text_size_slider.valueChanged.connect(self.update_text_size)

        self.db: Database = Database()
        self.manga = None
        self.chapters: list[Chapter] = []
        self.images: list[Image] = []
        self.cur_chapter = 1
        self.max_chapters = 1
        self.cur_page = 1
        self.max_page = 1
        self.catalog = None

    def setup(self, manga: Manga, chapters: list[Chapter], cur_chapter=1):
        self.showMaximized()
        self.manga = manga
        if self.manga.kind == 'ranobe':
            self.ui.size_frame.show()
        else:
            self.ui.img.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.ui.size_frame.hide()
        self.chapters = chapters
        self.cur_chapter = cur_chapter
        self.max_chapters = len(chapters)
        self.catalog = get_catalog(manga.catalog_id)()
        self.setWindowTitle(self.manga.name)
        self.update_chapter()

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key.Key_Escape:
                self.deleteLater()
        event.accept()

    def resizeEvent(self, event):
        if not self.chapters:
            return
        self.reset_reader_area()
        self.set_image()

    @Slot()
    def change_fullscreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    @Slot()
    def turn_page_next(self):
        self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], False)
        if self.cur_page == self.max_page:
            self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], True)
            self.turn_chapter_next()
        else:
            self.cur_page += 1
            self.update_page()

    @Slot()
    def turn_page_prev(self):
        self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], False)
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
        self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], True)
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
        if not self.images:
            return
        if self.manga.kind == 'ranobe':
            text = get_chapter_text(self.manga, self.chapters[self.cur_chapter - 1],
                                    self.images[self.cur_page - 1], self.catalog)
            self.ui.img.setText(text)
        else:
            Worker(self.set_image, True).start()

    def set_image(self, check_wait=False):
        page = self.cur_page
        if check_wait:
            time.sleep(0.25)
            if page != self.cur_page:
                return
        pixmap = get_chapter_image(self.manga, self.chapters[self.cur_chapter - 1],
                                   self.images[self.cur_page - 1], self.catalog)
        if page == self.cur_page:
            pixmap = self.resize_pixmap(pixmap)
            self.ui.img.setPixmap(pixmap)

    @Slot()
    def update_text_size(self):
        font = self.ui.img.font()
        font.setPointSize(self.ui.text_size_slider.value())
        self.ui.img.setFont(font)

    def resize_pixmap(self, pixmap: QPixmap):
        if pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            pixmap = pixmap.scaled(self.ui.img.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
        return pixmap

    def get_images(self):
        chapter = self.chapters[self.cur_chapter - 1]
        self.images = self.catalog.get_images(self.manga, chapter)
        self.max_page = self.get_chapter_pages()
        Worker(self.download_images, self.chapters[self.cur_chapter - 1]).start()

    def get_chapter_pages(self) -> int:
        if not self.images:
            return 1
        return self.images[-1].page

    def download_image(self, chapter, image):
        get_chapter_image(self.manga, chapter, image, self.catalog)

    def download_images(self, chapter: Chapter):
        images = self.images.copy()
        page = self.cur_page
        while True:
            if self.isHidden() or chapter.id != self.chapters[self.cur_chapter - 1].id or self.manga.kind == 'ranobe':
                break
            if page == self.cur_page:
                diff = len(images) - page
                if diff == 1:
                    self.download_image(chapter, images[self.cur_page])
                elif diff > 1:
                    self.download_image(chapter, images[self.cur_page])
                    self.download_image(chapter, images[self.cur_page + 1])
            image = images[self.cur_page - 1]
            page = self.cur_page
            self.download_image(chapter, image)
            time.sleep(0.35)
