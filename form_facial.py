from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from const import URL_API, library_icon_path, main_icon_path
from database import db
from desuUI import Ui_Dialog
from form_genres import FormGenres
from items import Manga
from static import get_html


class Communicate(QObject):
    clicked_library = pyqtSignal()
    double_click = pyqtSignal()


class FormFacial(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = db
        self.c = Communicate()
        self.cur_page = 1
        self.mangas = []
        self.params = {'limit': 50, 'page': self.cur_page, 'order': 'popular', 'genres': ''}
        self.order_by = {self.ui.sort_name: 'name', self.ui.sort_popular: 'popular'}
        self.kinds = {self.ui.type_manga: 'manga', self.ui.type_manhwa: 'manhwa', self.ui.type_manhua: 'manhua',
                      self.ui.type_one_shot: 'one_shot', self.ui.type_comics: 'comics'}
        self.Form_genres = FormGenres()
        self.ui.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui.btn_main.setIcon(QIcon(main_icon_path))
        self.ui.btn_mylist.clicked.connect(lambda: self.c.clicked_library.emit())
        self.ui.prev_page.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_page.clicked.connect(lambda: self.change_page('+'))
        self.ui.btn_genres_list.clicked.connect(self.clicked_genres)
        self.ui.filter_apply.clicked.connect(self.filter_apply)
        self.ui.filter_reset.clicked.connect(self.filter_reset)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.list_manga.doubleClicked.connect(lambda: self.c.double_click.emit())
        self.get_content()

    def clicked_genres(self):
        self.Form_genres.show()

    def get_content(self):
        self.ui.list_manga.clear()
        self.params.update({'page': self.cur_page})
        current_url = f'{URL_API}'
        html = get_html(current_url, self.params)
        self.mangas = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return None
            for i in html.json().get('response'):
                self.mangas.append(Manga(i))
                self.db.add_manga(i)
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        [self.ui.list_manga.addItem(i) for i in self.get_manga()]

    def get_manga(self) -> list:
        return [i.get_name() for i in self.mangas]

    def search(self):
        self.cur_page = 1
        self.params.update({'search': self.ui.line_search.text()})
        self.get_content()

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
