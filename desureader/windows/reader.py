from threading import Thread

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

from const.icons import app_icon_path
from data.ui.reader import Ui_MainWindow
from desureader.utils.catalog_manager import get_catalog
from desureader.utils.database import Database
from desureader.utils.file_manager import check_file_exists, get_file, save_file
from items import Manga, Chapter


class Reader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(app_icon_path))

        self.ui.prev_page_btn.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_page_btn.clicked.connect(lambda: self.change_page('+'))
        self.ui.prev_chapter_btn.clicked.connect(lambda: self.change_chapter('-'))
        self.ui.next_chapter_btn.clicked.connect(lambda: self.change_chapter('+'))

        self.ui.fullscreen_btn.clicked.connect(self.change_fullscreen)
        self.ui.text_size_slider.valueChanged.connect(self.update_text_size)

        self.db: Database = Database()
        self.manga = None
        self.chapters = None
        self.images = None
        self.cur_chapter: int = 1
        self.max_chapters: int = 1
        self.cur_page: int = 1
        self.max_page: int = 1
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
        self.change_chapter()

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key.Key_Escape:
                self.close()
        event.accept()

    def resizeEvent(self, event):
        self.ui.img.clear()
        self.attach_image()

    def change_page(self, page=None):
        self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], False)
        match page:
            case '+':
                if self.cur_page == self.max_page:
                    self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], True)
                    self.change_chapter('+')
                else:
                    self.cur_page += 1
            case '-':
                if self.cur_page == 1:
                    self.db.del_history_note(self.chapters[self.cur_chapter - 1])
                    self.change_chapter('-')
                else:
                    self.cur_page -= 1
        self.attach_image()
        self.ui.page_label.setText(f'Страница {self.cur_page} / {self.max_page}')

    def change_chapter(self, page=None):
        match page:
            case '+':
                if self.cur_chapter == self.max_chapters:
                    self.hide()
                    return
                else:
                    self.cur_chapter += 1
            case '-':
                if self.cur_chapter == 1:
                    return
                else:
                    self.cur_chapter -= 1
        self.cur_page = 1
        self.get_images()
        self.change_page()
        self.ui.chapter_label.setText(self.chapters[self.cur_chapter - 1].get_name())

    def change_fullscreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    def attach_image(self):
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.scrollArea.horizontalScrollBar().setValue(0)
        if not self.images:
            return
        if self.manga.kind == 'ranobe':
            text = self.get_text(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1])
            self.ui.img.setText(text)
        else:
            self.ui.scrollAreaWidgetContents.resize(0, 0)
            pixmap = self.get_pixmap(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1])
            self.ui.img.setPixmap(pixmap)

    def update_text_size(self):
        font = self.ui.img.font()
        font.setPointSize(self.ui.text_size_slider.value())
        self.ui.img.setFont(font)

    def get_image(self, chapter, image) -> QPixmap:
        path = f'Desu/images/{self.catalog.catalog_name}/manga/{self.manga.id}/{chapter.id}'
        file_name = f'{image.page}.jpg'
        if not check_file_exists(path, file_name):
            save_file(path, file_name, self.catalog.get_image(image))
        return QPixmap(get_file(path, file_name))

    def get_text(self, chapter, image):
        path = f'Desu/images/{self.catalog.catalog_name}/manga/{self.manga.id}/{chapter.id}'
        file_name = f'{image.page}.txt'
        if not check_file_exists(path, file_name):
            save_file(path, file_name, self.catalog.get_image(image))
        with open(f'{path}/{file_name}', encoding="utf8") as f:
            text = f.read()
            text = text.replace('&nbsp;', u'\xa0')
            text = text.replace('&mdash;', '—')
            return text

    def get_pixmap(self, chapter, image):
        pixmap = self.get_image(chapter, image)
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
        Thread(target=lambda: self.download(self), daemon=True).start()

    def get_chapter_pages(self) -> int:
        if not self.images:
            return 1
        return self.images[-1].page

    def download(self, form):
        images = self.images
        chapter = self.chapters[self.cur_chapter - 1]
        for image in images:
            if form.isHidden() or chapter.id != self.chapters[self.cur_chapter - 1].id or self.manga.kind == 'ranobe':
                break
            path = f'Desu/images/{self.catalog.catalog_name}/manga/{self.manga.id}/{chapter.id}'
            file_name = f'{image.page}.jpg'
            if not check_file_exists(path, file_name):
                save_file(path, file_name, self.catalog.get_image(image))
