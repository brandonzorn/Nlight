import os
from pathlib import Path
from threading import Thread
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from catalog_manager import get_catalog
from database import Database
from form.desu_readerUI import Ui_Dialog
from items import Image, Manga, Chapter


class Reader(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_re = Ui_Dialog()
        self.ui_re.setupUi(self)
        self.ui_re.text_size_slider.hide()
        app_icon_path = os.path.join(Path(__file__).parent, "images/icon.png")
        self.setWindowIcon(QIcon(app_icon_path))
        self.ui_re.prev_page.clicked.connect(lambda: self.press_key('prev_page'))
        self.ui_re.next_page.clicked.connect(lambda: self.press_key('next_page'))
        self.ui_re.prev_chp.clicked.connect(lambda: self.press_key('prev_ch'))
        self.ui_re.next_chp.clicked.connect(lambda: self.press_key('next_ch'))
        self.ui_re.text_size_slider.valueChanged.connect(self.update_text_size)
        self.wd = os.getcwd()
        self.db = Database()
        self.manga: Manga = Manga({})
        self.chapters: list[Chapter] = [Chapter({})]
        self.images: list[Image] = [Image({})]
        self.cur_chapter: int = 1
        self.max_chapters: int = 1
        self.cur_page: int = 1
        self.max_page: int = 1
        self.catalog = None

    def setup(self, manga, chapters, cur_chapter=1):
        self.cur_chapter = cur_chapter
        self.max_chapters = len(chapters)
        self.manga = manga
        self.catalog = get_catalog(manga.catalog_id)()
        self.chapters = chapters
        self.setWindowTitle(self.manga.name)
        self.showFullScreen()
        self.change_chapter()

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
        match page:
            case '+':
                if self.cur_page == self.max_page:
                    self.press_key('next_ch')
                else:
                    self.cur_page += 1
            case '-':
                if self.cur_page == 1:
                    self.press_key('prev_ch')
                else:
                    self.cur_page -= 1
        self.attach_image()
        self.ui_re.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')

    def change_chapter(self, page=None):
        match page:
            case '+':
                self.db.set_complete_chapter(self.chapters[self.cur_chapter - 1])
                if self.cur_chapter == self.max_chapters:
                    self.hide()
                else:
                    self.cur_chapter += 1
            case '-':
                self.db.del_complete_chapter(self.chapters[self.cur_chapter - 1])
                if self.cur_chapter == 1:
                    return
                else:
                    self.cur_chapter -= 1
        self.cur_page = 1
        self.get_images()
        self.change_page()
        self.ui_re.lbl_chp.setText(self.chapters[self.cur_chapter - 1].get_name())

    def attach_image(self):
        self.resize(self.screen().size())
        self.ui_re.scrollArea.verticalScrollBar().setValue(0)
        self.ui_re.scrollArea.horizontalScrollBar().setValue(0)
        if self.images[self.cur_page - 1].is_text:
            self.ui_re.text_size_slider.show()
            text = self.get_text(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1])
            self.ui_re.img.setText(text)
        else:
            pixmap = self.get_pixmap(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1])
            self.ui_re.img.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.ui_re.img.setPixmap(pixmap)
        # "AlignmentFlag.AlignVCenter|AlignJustify"
        # self.showFullScreen()
        # self.ui_re.scrollArea.setWidgetResizable(True)

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
        # for i in self.images:
        #     self.db.add_image(i, chapter)
        # self.images = self.db.get_images(chapter)
        if not self.images:
            self.images = [Image({'page': 1})]
        self.max_page = self.get_images_pages()
        Thread(target=lambda: self.download(self)).start()

    def get_images_pages(self) -> int:
        if not self.images:
            return 1
        return self.images[-1].page

    def download(self, form):
        images = self.images
        chapter = self.chapters[self.cur_chapter - 1]
        for image in images:
            if form.isHidden() or chapter.id != self.chapters[self.cur_chapter - 1].id or image.is_text:
                break
            path = f'{self.wd}/Desu/images/{self.catalog.catalog_name}/{self.manga.id}/{chapter.id}'
            if not os.path.exists(f'{path}/{image.page}.jpg'):
                img = self.catalog.get_image(images[image.page - 1])
                if img:
                    with open(f'{path}/{image.page}.jpg', 'wb') as f:
                        f.write(img.content)
