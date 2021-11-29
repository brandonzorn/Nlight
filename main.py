import sys
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import desuUI
import desu_readerUI
import desu_chaptersUI
import desu_genresUI
import desu_mylistUI
from desu import Desu
from reader import Reader
from static import *
from threading import Thread

URL = 'https://desu.me'
URL_API = 'https://desu.me/manga/api'
HEADERS = {'User-Agent': 'Desu'}


class App:
    def __init__(self):
        self.desu = Desu()
        self.cur_page = 1
        self.cur_index = 0
        self.is_favorites = False
        self.params = {'limit': 50, 'page': self.cur_page, 'order': 'popular', 'genres': ''}
        self.window = QStackedWidget()
        self.Form_main = QWidget()
        self.Form_chapters = QWidget()
        self.reader = Reader()
        self.Form_favorites = QWidget()
        self.Form_genres = QDialog()
        self.ui = desuUI.Ui_Dialog()
        self.ui_ml = desu_mylistUI.Ui_Dialog()
        self.ui_ch = desu_chaptersUI.Ui_Dialog()
        self.ui_re = desu_readerUI.Ui_Dialog()
        self.ui_ge = desu_genresUI.Ui_Dialog()
        self.ui.setupUi(self.Form_main)
        self.ui_ml.setupUi(self.Form_favorites)
        self.ui_ch.setupUi(self.Form_chapters)
        self.ui_re.setupUi(self.reader)
        self.ui_ge.setupUi(self.Form_genres)
        self.window.addWidget(self.Form_main)
        self.window.addWidget(self.Form_chapters)
        self.window.addWidget(self.Form_favorites)
        screen_size = [self.window.screen().size().width(), self.window.screen().size().height()]
        self.window.setMinimumSize(QSize(screen_size[0] // 2, screen_size[1] // 2))
        self.Form_genres.setFixedSize(self.Form_genres.minimumSize())
        self.order_by = {self.ui.sort_name: 'name', self.ui.sort_popular: 'popular'}
        self.kinds = {self.ui.type_manga: 'manga', self.ui.type_manhwa: 'manhwa', self.ui.type_manhua: 'manhua',
                      self.ui.type_one_shot: 'one_shot', self.ui.type_comics: 'comics'}
        self.genres = {self.ui_ge.g_dementia: 'Dementia', self.ui_ge.g_martialarts: 'Martial Arts',
                       self.ui_ge.g_color: 'Color', self.ui_ge.g_vampire: 'Vampire', self.ui_ge.g_web: 'Web',
                       self.ui_ge.g_harem: 'Harem', self.ui_ge.g_heroicfantasy: 'Heroic Fantasy',
                       self.ui_ge.g_demons: 'Demons',  self.ui_ge.g_mystery: 'Mystery', self.ui_ge.g_josei: 'Josei',
                       self.ui_ge.g_drama: 'Drama', self.ui_ge.g_yonkoma: 'Yonkoma', self.ui_ge.g_game: 'Game',
                       self.ui_ge.g_isekai: 'Isekai', self.ui_ge.g_historical: 'Historical',
                       self.ui_ge.g_comedy: 'Comedy', self.ui_ge.g_space: 'Space', self.ui_ge.g_litrpg: 'LitRPG',
                       self.ui_ge.g_magic: 'Magic', self.ui_ge.g_mecha: 'Mecha', self.ui_ge.g_mystic: 'Mystic',
                       self.ui_ge.g_music: 'Music', self.ui_ge.g_scifi: 'Sci-Fi', self.ui_ge.g_parody: 'Parody',
                       self.ui_ge.g_sliceoflife: 'Slice of Life', self.ui_ge.g_postapocalyptic: 'Post Apocalyptic',
                       self.ui_ge.g_adventure: 'Adventure', self.ui_ge.g_psychological: 'Psychological',
                       self.ui_ge.g_romance: 'Romance', self.ui_ge.g_samurai: 'Samurai',
                       self.ui_ge.g_supernatural: 'Supernatural', self.ui_ge.g_shoujo: 'Shoujo',
                       self.ui_ge.g_shoujoai: 'Shoujo Ai', self.ui_ge.g_seinen: 'Seinen',
                       self.ui_ge.g_shounen: 'Shounen', self.ui_ge.g_shounenai: 'Shounen Ai',
                       self.ui_ge.g_genderbender: 'Gender Bender', self.ui_ge.g_sports: 'Sports',
                       self.ui_ge.g_superpower: 'Super Power', self.ui_ge.g_tragedy: 'Tragedy',
                       self.ui_ge.g_thriller: 'Thriller', self.ui_ge.g_horror: 'Horror',
                       self.ui_ge.g_fiction: 'Fiction', self.ui_ge.g_fantasy: 'Fantasy', self.ui_ge.g_hentai: 'Hentai',
                       self.ui_ge.g_school: 'School', self.ui_ge.g_action: 'Action', self.ui_ge.g_ecchi: 'Ecchi',
                       self.ui_ge.g_yuri: 'Yuri', self.ui_ge.g_yaoi: 'Yaoi'}
        app_icon_path = os.path.join(Path(__file__).parent, "images/icon.png")
        library_icon_path = os.path.join(Path(__file__).parent, "images/library.png")
        main_icon_path = os.path.join(Path(__file__).parent, "images/main.png")
        back_icon_path = os.path.join(Path(__file__).parent, "images/back.png")
        self.favorite_icon_path = os.path.join(Path(__file__).parent, "images/favorite.png")
        self.favorite1_icon_path = os.path.join(Path(__file__).parent, "images/favorite1.png")
        self.favorite2_icon_path = os.path.join(Path(__file__).parent, "images/favorite2.png")
        self.window.setWindowTitle('Desu')
        self.window.setWindowIcon(QIcon(app_icon_path))
        self.reader.setWindowIcon(QIcon(app_icon_path))
        self.Form_genres.setWindowIcon(QIcon(app_icon_path))
        self.ui.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui_ml.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui.btn_main.setIcon(QIcon(main_icon_path))
        self.ui_ml.btn_main.setIcon(QIcon(main_icon_path))
        self.ui.btn_mylist.setIconSize(self.ui.btn_mylist.size())
        self.ui_ml.btn_mylist.setIconSize(self.ui.btn_mylist.size())
        self.ui.btn_main.setIconSize(self.ui.btn_main.size())
        self.ui_ml.btn_main.setIconSize(self.ui.btn_main.size())
        self.ui_ch.btn_back.setIcon(QIcon(back_icon_path))
        self.ui.btn_main.clicked.connect(self.clicked_main)
        self.ui.btn_mylist.clicked.connect(self.clicked_favorites)
        self.ui.prev_page.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_page.clicked.connect(lambda: self.change_page('+'))
        self.ui.btn_genres_list.clicked.connect(self.clicked_genres)
        self.ui_re.prev_page.clicked.connect(lambda: self.change_page_reader('-'))
        self.ui_re.next_page.clicked.connect(lambda: self.change_page_reader('+'))
        self.ui_re.prev_chp.clicked.connect(lambda: self.change_chapter_reader('-'))
        self.ui_re.next_chp.clicked.connect(lambda: self.change_chapter_reader('+'))
        self.ui.filter_apply.clicked.connect(self.filter_apply)
        self.ui.filter_reset.clicked.connect(self.filter_reset)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.list_manga.doubleClicked.connect(self.double_click)
        self.ui_ch.btn_back.clicked.connect(self.back)
        self.ui_ch.chapters.doubleClicked.connect(self.open_reader)
        self.ui_ch.btn_mylist.clicked.connect(self.add_to_favorites)
        self.ui_ge.buttonBox.accepted.connect(self.genres_accept)
        self.ui_ge.buttonBox.rejected.connect(self.genres_reject)
        self.reader.c.next_page.connect(lambda: self.change_page_reader('+'))
        self.reader.c.prev_page.connect(lambda: self.change_page_reader('-'))
        self.reader.c.next_ch.connect(lambda: self.change_chapter_reader('+'))
        self.reader.c.prev_ch.connect(lambda: self.change_chapter_reader('-'))
        self.ui_ml.btn_main.clicked.connect(self.clicked_main)
        self.ui_ml.list_manga.doubleClicked.connect(self.double_click)
        self.ui_ml.pushButton.clicked.connect(self.download_all)
        self.window.show()
        self.get_content()

    def clicked_main(self):
        self.is_favorites = False
        self.window.setCurrentIndex(0)

    def clicked_chapters(self):
        self.window.setCurrentIndex(1)

    def clicked_favorites(self):
        self.is_favorites = True
        self.ui_ml.list_manga.clear()
        self.window.setCurrentIndex(2)
        self.desu.get_content_favorites()
        [self.ui_ml.list_manga.addItem(i) for i in self.desu.get_manga_favorites()]

    def back(self):
        if self.is_favorites:
            self.clicked_favorites()
        else:
            self.clicked_main()

    def clicked_genres(self):
        self.Form_genres.setWindowTitle('Genres')
        self.Form_genres.show()

    def get_content(self):
        self.ui.list_manga.clear()
        self.params.update({'page': self.cur_page})
        current_url = f'{URL_API}'
        html = get_html(current_url, self.params)
        self.desu.get_content(html)
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        [self.ui.list_manga.addItem(i) for i in self.desu.get_manga()]

    def get_chapters(self):
        self.ui_ch.chapters.clear()
        current_url = f'{URL_API}/{self.desu.manga.id}'
        html = get_html(current_url)
        self.desu.get_chapters(html)
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.reader.max_chapters = len(self.desu.chapters)
        [self.ui_ch.chapters.addItem(i.get_name()) for i in self.desu.chapters]

    def get_images(self):
        self.desu.chapter = self.desu.chapters[self.reader.cur_chapter - 1]
        current_url = f'{URL_API}/{self.desu.manga.id}/chapter/{self.desu.chapter.id}'
        html = get_html(current_url)
        self.desu.get_images(html)
        self.reader.max_page = self.desu.get_images_pages()
        Thread(target=lambda: self.desu.download(self.reader)).start()

    def get_image(self):
        size = self.reader.screen().size()
        self.reader.resize(size)
        self.reader.showFullScreen()
        image = self.desu.images[self.reader.cur_page - 1]
        pixmap = QPixmap(self.desu.get_image(image))
        pixmap = pixmap.scaled(size - QSize(20, 80), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pixmap

    def search(self):
        self.cur_page = 1
        self.params.update({'search': self.ui.line_search.text()})
        self.get_content()

    def open_reader(self):
        self.cur_index = self.ui_ch.chapters.currentIndex().row()
        self.get_images()
        self.reader.manga = self.desu.manga
        self.reader.chapters = self.desu.chapters
        self.change_chapter_reader()
        self.reader.show()

    def download_all(self):
        cur_id = self.ui_ml.list_manga.currentIndex().row()
        if cur_id < 0:
            return
        self.desu.manga_id = self.desu.manga_favorites[cur_id].get('id')
        current_url = f'{URL_API}/{self.desu.manga_id}'
        html = get_html(current_url)
        self.desu.get_chapters(html)
        Thread(target=lambda: self.desu.download_all(self.window)).start()

    def double_click(self):
        if self.window.currentIndex() == 0:
            cur_id = self.ui.list_manga.currentIndex().row()
            a = self.desu.mangas
        else:
            cur_id = self.ui_ml.list_manga.currentIndex().row()
            a = self.desu.manga_favorites
        self.desu.manga = a[cur_id]
        self.reader.hide()
        self.clicked_chapters()
        pixmap = QPixmap(self.desu.get_preview())
        self.ui_ch.image.setPixmap(pixmap)
        self.ui_ch.image.setScaledContents(True)
        self.ui_ch.description.setText(a[cur_id].description)
        self.ui_ch.name.setText(a[cur_id].name)
        self.reader.setWindowTitle(a[cur_id].name)
        self.ui_ch.russian.setText(a[cur_id].russian)
        self.set_score(a[cur_id].score)
        if manga_favorites_check(self.desu.manga.id):
            self.ui_ch.btn_mylist.setIcon(QIcon(self.favorite1_icon_path))
        else:
            self.ui_ch.btn_mylist.setIcon(QIcon(self.favorite_icon_path))
        self.get_chapters()

    def set_score(self, score: float):
        stars = [self.ui_ch.star_1, self.ui_ch.star_2, self.ui_ch.star_3, self.ui_ch.star_4, self.ui_ch.star_5]
        [i.setIcon(QIcon(self.favorite_icon_path)) for i in stars]
        self.ui_ch.rate.setText(f'Рейтинг: {score}')
        score = round(score) / 2
        for i in range(int(score)):
            a = stars[i]
            a.show()
            a.setIcon(QIcon(self.favorite1_icon_path))
        if score - int(score) >= 0.75:
            stars[int(score)].setIcon(QIcon(self.favorite1_icon_path))
            stars[int(score)].show()
        elif 0.25 <= score - int(score) <= 0.5:
            stars[int(score)].setIcon(QIcon(self.favorite2_icon_path))
            stars[int(score)].show()

    def change_page(self, page):
        if page == '+':
            self.cur_page += 1
        elif self.cur_page > 1:
            self.cur_page -= 1
        else:
            return
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.get_content()

    def change_page_reader(self, page=None):
        self.reader.change_page(page)
        pixmap = self.get_image()
        self.ui_re.img.setPixmap(pixmap)
        cur_page, max_page = self.reader.cur_page, self.reader.max_page
        self.ui_re.lbl_page.setText(f'Страница {cur_page} / {max_page}')

    def change_chapter_reader(self, page=None):
        self.reader.change_chapter(page)
        self.get_images()
        pixmap = self.get_image()
        self.ui_re.img.setPixmap(pixmap)
        cur_page, max_page = self.reader.cur_page, self.reader.max_page
        self.ui_re.lbl_page.setText(f'Страница {cur_page} / {max_page}')
        self.ui_re.lbl_chp.setText(self.desu.get_chapter())

    def filter_apply(self):
        self.cur_page = 1
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.params = {'limit': 50}
        [self.params.update({'order': self.order_by.get(i)}) for i in self.order_by if i.isChecked()]
        a = ','.join([self.kinds.get(i) for i in self.kinds if i.isChecked()])
        if len(a) != 0:
            self.params.update({'kinds': a})
        if self.ui.line_search.text() != '':
            self.params.update({'search': self.ui.line_search.text()})
        self.genres_accept()
        self.get_content()

    def filter_reset(self):
        self.cur_page = 1
        self.genres_reject()
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.params = {'limit': 50, 'order': '', 'genres': ''}
        self.genres_reject()
        self.ui.sort_popular.setChecked(True)
        self.ui.line_search.setText('')
        [i.setChecked(False) for i in self.kinds]
        self.get_content()

    def add_to_favorites(self):
        if manga_favorites_check(self.desu.manga.id):
            manga_favorites_rem(self.desu.manga.id)
            self.ui_ch.btn_mylist.setIcon(QIcon(self.favorite_icon_path))
        else:
            manga_favorites_add(self.desu.manga.id)
            self.ui_ch.btn_mylist.setIcon(QIcon(self.favorite1_icon_path))

    def genres_accept(self):
        genres = [self.genres.get(i) for i in self.genres if i.isChecked()]
        self.params.update({'genres': ','.join(genres)})

    def genres_reject(self):
        for i in self.genres:
            if self.genres.get(i) not in self.params.get('genres'):
                i.setChecked(False)
            else:
                i.setChecked(True)


if __name__ == '__main__':
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    App()
    sys.exit(app.exec_())
