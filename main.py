import sys
import os
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import desuUI
import desu_chaptersUI
import desu_mylistUI
from const import URL_API
from desu import Desu
from form_genres import FormGenres
from reader import Reader
from static import *
from threading import Thread


class App:
    def __init__(self):
        self.Desu = Desu()
        self.cur_page = 1
        self.is_favorites = False
        self.params = {'limit': 50, 'page': self.cur_page, 'order': 'popular', 'genres': ''}
        self.window = QStackedWidget()
        self.Form_main = QWidget()
        self.Form_chapters = QWidget()
        self.Form_favorites = QWidget()
        self.Form_genres = FormGenres()
        self.ui = desuUI.Ui_Dialog()
        self.ui_ml = desu_mylistUI.Ui_Dialog()
        self.ui_ch = desu_chaptersUI.Ui_Dialog()
        self.ui.setupUi(self.Form_main)
        self.ui_ml.setupUi(self.Form_favorites)
        self.ui_ch.setupUi(self.Form_chapters)
        self.window.addWidget(self.Form_main)
        self.window.addWidget(self.Form_chapters)
        self.window.addWidget(self.Form_favorites)
        screen_size = [self.window.screen().size().width(), self.window.screen().size().height()]
        self.window.setMinimumSize(QSize(screen_size[0] // 2, screen_size[1] // 2))
        self.Form_genres.setFixedSize(self.Form_genres.minimumSize())
        self.order_by = {self.ui.sort_name: 'name', self.ui.sort_popular: 'popular'}
        self.kinds = {self.ui.type_manga: 'manga', self.ui.type_manhwa: 'manhwa', self.ui.type_manhua: 'manhua',
                      self.ui.type_one_shot: 'one_shot', self.ui.type_comics: 'comics'}
        app_icon_path = os.path.join(Path(__file__).parent, "images/icon.png")
        library_icon_path = os.path.join(Path(__file__).parent, "images/library.png")
        main_icon_path = os.path.join(Path(__file__).parent, "images/main.png")
        back_icon_path = os.path.join(Path(__file__).parent, "images/back.png")
        self.favorite_icon_path = os.path.join(Path(__file__).parent, "images/favorite.png")
        self.favorite1_icon_path = os.path.join(Path(__file__).parent, "images/favorite1.png")
        self.favorite2_icon_path = os.path.join(Path(__file__).parent, "images/favorite2.png")
        self.window.setWindowTitle('Desu')
        self.window.setWindowIcon(QIcon(app_icon_path))
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
        self.ui.filter_apply.clicked.connect(self.filter_apply)
        self.ui.filter_reset.clicked.connect(self.filter_reset)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.list_manga.doubleClicked.connect(self.double_click)
        self.ui_ch.btn_back.clicked.connect(self.back)
        self.ui_ch.chapters.doubleClicked.connect(self.open_reader)
        self.ui_ch.btn_mylist.clicked.connect(self.add_to_favorites)
        self.ui_ml.btn_main.clicked.connect(self.clicked_main)
        self.ui_ml.list_manga.doubleClicked.connect(self.double_click)
        self.ui_ml.b_download.clicked.connect(self.download_all)
        self.window.show()
        self.readers = []
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
        self.Desu.get_content_favorites()
        [self.ui_ml.list_manga.addItem(i) for i in self.Desu.get_manga_favorites()]

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
        self.Desu.get_content(html)
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        [self.ui.list_manga.addItem(i) for i in self.Desu.get_manga()]

    def get_chapters(self):
        self.ui_ch.chapters.clear()
        current_url = f'{URL_API}/{self.Desu.manga.id}'
        html = get_html(current_url)
        self.Desu.get_chapters(html)
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        [self.ui_ch.chapters.addItem(i.get_name()) for i in self.Desu.chapters]

    def search(self):
        self.cur_page = 1
        self.params.update({'search': self.ui.line_search.text()})
        self.get_content()

    def open_reader(self):
        self.readers.append(Reader(self.Desu.manga, self.Desu.chapters, self.ui_ch.chapters.currentIndex().row() + 1))

    def download_all(self):
        self.readers[-1].close_reader()
        cur_id = self.ui_ml.list_manga.currentIndex().row()
        if cur_id < 0:
            return
        self.Desu.manga = self.Desu.manga_favorites[cur_id]
        current_url = f'{URL_API}/{self.Desu.manga.id}'
        html = get_html(current_url)
        self.Desu.get_chapters(html)
        Thread(target=lambda: self.Desu.download_all(self.window)).start()

    def double_click(self):
        if self.window.currentIndex() == 0:
            cur_id = self.ui.list_manga.currentIndex().row()
            a = self.Desu.mangas
        else:
            cur_id = self.ui_ml.list_manga.currentIndex().row()
            a = self.Desu.manga_favorites
        self.Desu.manga = a[cur_id]
        if self.readers:
            self.readers[-1].hide()
            self.readers[-1].setWindowTitle(a[cur_id].name)
        self.clicked_chapters()
        pixmap = QPixmap(self.Desu.get_preview())
        self.ui_ch.image.setPixmap(pixmap)
        self.ui_ch.image.setScaledContents(True)
        self.ui_ch.description.setText(a[cur_id].description)
        self.ui_ch.name.setText(a[cur_id].name)
        self.ui_ch.russian.setText(a[cur_id].russian)
        self.set_score(a[cur_id].score)
        if self.Desu.db.check_manga_library(self.Desu.manga.id):
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
        self.Form_genres.accept_genres()
        self.params.update(self.Form_genres.selected_genres)
        self.get_content()

    def filter_reset(self):
        self.cur_page = 1
        self.Form_genres.reject_genres()
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.params = {'limit': 50, 'order': '', 'genres': ''}
        self.Form_genres.reject_genres()
        self.ui.sort_popular.setChecked(True)
        self.ui.line_search.setText('')
        [i.setChecked(False) for i in self.kinds]
        self.get_content()

    def add_to_favorites(self):
        if self.Desu.db.check_manga_library(self.Desu.manga.id):
            self.Desu.db.rem_manga_library(self.Desu.manga.id)
            self.ui_ch.btn_mylist.setIcon(QIcon(self.favorite_icon_path))
        else:
            self.Desu.db.add_manga_library(self.Desu.manga.id)
            self.ui_ch.btn_mylist.setIcon(QIcon(self.favorite1_icon_path))


if __name__ == '__main__':
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    App()
    sys.exit(app.exec_())
