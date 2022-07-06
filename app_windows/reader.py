import os
from threading import Thread

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget

from catalog_manager import get_catalog
from const import app_icon_path, next_ch_icon_path, prev_ch_icon_path, next_page_icon_path, prev_page_icon_path, \
    fullscreen_icon_path
from database import Database
from forms.desu_readerUI import Ui_Dialog
from items import Manga, Chapter


class Reader(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_re = Ui_Dialog()
        self.ui_re.setupUi(self)

        self.setWindowIcon(QIcon(app_icon_path))

        self.ui_re.prev_page.setIcon(QIcon(prev_page_icon_path))
        self.ui_re.next_page.setIcon(QIcon(next_page_icon_path))
        self.ui_re.prev_chp.setIcon(QIcon(prev_ch_icon_path))
        self.ui_re.next_chp.setIcon(QIcon(next_ch_icon_path))
        self.ui_re.btn_fullscreen.setIcon(QIcon(fullscreen_icon_path))

        self.ui_re.prev_page.clicked.connect(lambda: self.press_key('prev_page'))
        self.ui_re.next_page.clicked.connect(lambda: self.press_key('next_page'))
        self.ui_re.prev_chp.clicked.connect(lambda: self.press_key('prev_ch'))
        self.ui_re.next_chp.clicked.connect(lambda: self.press_key('next_ch'))

        self.ui_re.btn_fullscreen.clicked.connect(self.change_fullscreen)
        self.ui_re.text_size_slider.valueChanged.connect(self.update_text_size)

        self.wd = os.getcwd()
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
            self.ui_re.text_size_slider.show()
        else:
            self.ui_re.img.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.ui_re.text_size_slider.hide()
        self.chapters = chapters
        self.cur_chapter = cur_chapter
        self.max_chapters = len(chapters)
        self.catalog = get_catalog(manga.catalog_id)()
        self.setWindowTitle(self.manga.name)
        self.change_chapter()

    def resizeEvent(self, a0):
        self.attach_image()

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key.Key_Escape:
                self.hide()
            case Qt.Key.Key_Left:
                self.press_key('prev_page')
            case Qt.Key.Key_Right:
                self.press_key('next_page')
            case Qt.Key.Key_Down:
                self.press_key('prev_ch')
            case Qt.Key.Key_Up:
                self.press_key('next_ch')
        event.accept()

    def press_key(self, e):
        if self.isActiveWindow():
            match e:
                case 'next_page':
                    self.change_page('+')
                case 'prev_page':
                    self.change_page('-')
                case 'next_ch':
                    self.change_chapter('+')
                case 'prev_ch':
                    self.change_chapter('-')

    def change_page(self, page=None):
        self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], False)
        match page:
            case '+':
                if self.cur_page == self.max_page:
                    self.db.add_history_note(self.manga, self.chapters[self.cur_chapter - 1], True)
                    self.press_key('next_ch')
                else:
                    self.cur_page += 1
            case '-':
                if self.cur_page == 1:
                    self.db.del_history_note(self.chapters[self.cur_chapter - 1])
                    self.press_key('prev_ch')
                else:
                    self.cur_page -= 1
        self.attach_image()
        self.ui_re.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')

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
        self.ui_re.lbl_chp.setText(self.chapters[self.cur_chapter - 1].get_name())

    def change_fullscreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    def attach_image(self):
        self.ui_re.scrollArea.verticalScrollBar().setValue(0)
        self.ui_re.scrollArea.horizontalScrollBar().setValue(0)
        if not self.images:
            return
        if self.manga.kind == 'ranobe':
            text = self.get_text(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1])
            self.ui_re.img.setText(text)
        else:
            pixmap = self.get_pixmap(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1])
            self.ui_re.img.setPixmap(pixmap)

    def update_text_size(self):
        font = self.ui_re.img.font()
        font.setPointSize(self.ui_re.text_size_slider.value())
        self.ui_re.img.setFont(font)

    def get_image(self, chapter, image) -> str:
        path = f'{self.wd}/Desu/images/{self.catalog.catalog_name}/{self.manga.id}/{chapter.id}'
        if not os.path.exists(f'{path}/{image.page}.jpg'):
            os.makedirs(path, exist_ok=True)
            img = self.catalog.get_image(image)
            if img:
                with open(f'{path}/{image.page}.jpg', 'wb') as f:
                    f.write(img.content)
        return f'{path}/{image.page}.jpg'

    def get_text(self, chapter, image):
        path = f'{self.wd}/Desu/images/{self.catalog.catalog_name}/{self.manga.id}/{chapter.id}'
        if not os.path.exists(f'{path}/{image.page}.txt'):
            os.makedirs(path, exist_ok=True)
            img = self.catalog.get_image(image)
            if img:
                with open(f'{path}/{image.page}.txt', 'wb') as f:
                    f.write(img.content)
        with open(f'{path}/{image.page}.txt', encoding="utf8") as f:
            text = f.read()
            text = text.replace('&nbsp;', u'\xa0')
            text = text.replace('&mdash;', '—')
            return text

    def get_pixmap(self, chapter, image):
        pixmap = QPixmap(self.get_image(chapter, image))
        if pixmap.isNull():
            return QPixmap()
        if 0.5 < pixmap.width() / pixmap.height() < 2:
            pixmap = pixmap.scaled(self.ui_re.img.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
        return pixmap

    def get_images(self):
        chapter = self.chapters[self.cur_chapter - 1]
        self.images = self.catalog.get_images(self.manga, chapter)
        # self.db.add_images(self.images, chapter)
        # self.images = self.db.get_images(chapter)
        self.max_page = self.get_images_pages()
        Thread(target=lambda: self.download(self), daemon=True).start()

    def get_images_pages(self) -> int:
        if not self.images:
            return 1
        return self.images[-1].page

    def download(self, form):
        images = self.images
        chapter = self.chapters[self.cur_chapter - 1]
        for image in images:
            if form.isHidden() or chapter.id != self.chapters[self.cur_chapter - 1].id or self.manga.kind == 'ranobe':
                break
            path = f'{self.wd}/Desu/images/{self.catalog.catalog_name}/{self.manga.id}/{chapter.id}'
            if not os.path.exists(f'{path}/{image.page}.jpg'):
                img = self.catalog.get_image(images[image.page - 1])
                if img:
                    with open(f'{path}/{image.page}.jpg', 'wb') as f:
                        f.write(img.content)
