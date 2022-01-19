from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from desu_readerUI import Ui_Dialog
from items import *
from static import *
from threading import Thread


URL = 'https://desu.me'
URL_API = 'https://desu.me/manga/api'
HEADERS = {'User-Agent': 'Desu'}


class Reader(QWidget):
    def __init__(self, manga: Manga, chapters: list, cur_chapter: int):
        super().__init__()
        self.cur_chapter: int = cur_chapter
        self.max_chapters: int = 1
        self.cur_page: int = 1
        self.max_page: int = 1
        self.manga: Manga = manga
        self.chapters = chapters
        self.chapter: Chapter = Chapter({})
        self.images = []
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.prev_page.clicked.connect(lambda: self.press_key('prev_page'))
        self.ui.next_page.clicked.connect(lambda: self.press_key('next_page'))
        self.ui.prev_chp.clicked.connect(lambda: self.press_key('prev_ch'))
        self.ui.next_chp.clicked.connect(lambda: self.press_key('next_ch'))
        self.change_chapter()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Left:
            self.press_key('prev_page')
        if event.key() == Qt.Key_Right:
            self.press_key('next_page')
        if event.key() == Qt.Key_Up:
            self.press_key('next_ch')
        if event.key() == Qt.Key_Down:
            self.press_key('prev_ch')
        event.accept()

    def press_key(self, e):
        if self.isActiveWindow():
            if e == 'next_page':
                self.change_page('+')
            if e == 'prev_page':
                self.change_page('-')
            if e == 'next_ch':
                self.change_chapter('+')
            if e == 'prev_ch':
                self.change_chapter('-')

    def change_page(self, page):
        if page == '+':
            if self.cur_page == self.max_page and self.cur_chapter == self.max_chapters:
                return
            elif self.cur_page == self.max_page:
                self.press_key('next_ch')
            else:
                self.cur_page += 1
        elif page == '-':
            if self.cur_page > 1:
                self.cur_page -= 1
            elif self.cur_page == 1 and self.cur_chapter == 1:
                return
            else:
                self.press_key('prev_ch')
        pixmap = self.get_image()
        self.ui.img.setPixmap(pixmap)
        self.ui.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')

    def open(self):
        self.max_chapters = len(self.chapters)
        self.showFullScreen()

    def change_chapter(self, page=None):
        if page == '+':
            if self.cur_chapter != self.max_chapters:
                self.cur_chapter += 1
            else:
                return
        elif page == '-':
            if self.cur_chapter > 1:
                self.cur_chapter -= 1
            elif self.cur_chapter == 1:
                return
        self.cur_page = 1
        self.get_images()
        pixmap = self.get_image()
        self.ui.img.setPixmap(pixmap)
        self.ui.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')
        self.ui.lbl_chp.setText(self.chapter.get_name())

    def get_images(self):
        self.chapter = self.chapters[self.cur_chapter - 1]
        current_url = f'{URL_API}/{self.manga.id}/chapter/{self.chapter.id}'
        html = get_html(current_url)
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return []
            images = html.json().get('response').get('pages').get('list')
            for i in images:
                images_add(i, self.chapter.id, images.index(i))
        self.images = images_get(self.chapter.id)
        self.max_page = self.get_images_pages()

    def get_image(self):
        size = self.screen().size()
        self.resize(size)
        self.showFullScreen()
        image = self.images[self.cur_page - 1]
        pixmap = QPixmap(self.get_imag(self.manga, self.chapter, image))
        if pixmap.isNull():
            return QPixmap()
        pixmap = pixmap.scaled(size - QSize(20, 80), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pixmap

    def get_images_pages(self) -> int:
        if not self.images:
            return 1
        return self.images[-1].page

    @staticmethod
    def get_imag(manga: Manga, chapter: Chapter, image: Image) -> str:
        wd = os.getcwd()
        page = image.page
        if not os.path.exists(f'{wd}/Desu/images/{manga.id}/{chapter.id}/{page}.jpg'):
            os.makedirs(f'{wd}/Desu/images/{manga.id}/{chapter.id}', exist_ok=True)
            img = get_html(image.img)
            with open(f'{wd}/Desu/images/{manga.id}/{chapter.id}/{page}.jpg', 'wb') as f:
                f.write(img.content)
        return f'{wd}/Desu/images/{manga.id}/{chapter.id}/{page}.jpg'
