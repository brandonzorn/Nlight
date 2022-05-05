from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from catalog_manager import get_catalog, CATALOGS
from const import library_icon_path, main_icon_path, shikimori_icon_path
from database import Database
from form.desuUI import Ui_Dialog
from form_genres import FormGenres
from items import RequestForm


class FormFacial(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = Database()
        self.cur_page = 1
        self.mangas = []
        self.request_params = RequestForm()
        self.order_by = {self.ui.sort_name: 'name', self.ui.sort_popular: 'popular'}
        self.kinds = {self.ui.type_manga: 'manga', self.ui.type_manhwa: 'manhwa', self.ui.type_manhua: 'manhua',
                      self.ui.type_one_shot: 'one_shot', self.ui.type_comics: 'comics'}
        self.Form_genres = FormGenres()
        self.ui.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui.btn_main.setIcon(QIcon(main_icon_path))
        self.ui.btn_shikimori.setIcon(QIcon(shikimori_icon_path))
        self.ui.prev_page.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_page.clicked.connect(lambda: self.change_page('+'))
        self.ui.btn_genres_list.clicked.connect(self.clicked_genres)
        self.ui.filter_apply.clicked.connect(self.filter_apply)
        self.ui.filter_reset.clicked.connect(self.filter_reset)
        self.ui.btn_search.clicked.connect(self.search)
        self.catalog = get_catalog()()
        self.get_content()

    def clicked_genres(self):
        self.Form_genres.show()

    def get_current_manga(self):
        return self.catalog.get_manga(self.mangas[self.ui.list_manga.currentIndex().row()])

    def update_catalog(self, index):
        catalog = get_catalog(index)
        self.catalog = catalog()
        self.Form_genres.catalog = catalog()
        self.Form_genres.setup()
        self.get_content()

    def setup_catalogs(self):
        self.ui.catalog_list.clear()
        self.ui.catalog_list.addItems([i.catalog_name for i in CATALOGS.values()])

    def get_content(self):
        self.ui.list_manga.clear()
        self.request_params.page = self.cur_page
        self.mangas = self.catalog.search_manga(self.request_params)
        if len(self.mangas) == 0:
            return
        for i in self.mangas:
            self.db.add_manga(i)
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        [self.ui.list_manga.addItem(i) for i in self.get_manga_names()]

    def get_manga_names(self) -> list:
        return [i.get_name() for i in self.mangas]

    def search(self):
        self.cur_page = 1
        self.request_params.search = self.ui.line_search.text()
        self.get_content()

    def change_page(self, page):
        match page:
            case '+':
                self.cur_page += 1
            case '-':
                if self.cur_page > 1:
                    self.cur_page -= 1
            case _:
                return
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.get_content()

    def filter_apply(self):
        self.cur_page = 1
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.request_params.clear()
        self.request_params.order = [self.order_by.get(i) for i in self.order_by if i.isChecked()]
        self.request_params.kinds = [self.kinds.get(i) for i in self.kinds if i.isChecked()]
        self.request_params.search = self.ui.line_search.text()
        self.Form_genres.accept_genres()
        self.request_params.genres = self.Form_genres.selected_genres
        self.get_content()

    def filter_reset(self):
        self.cur_page = 1
        self.Form_genres.clear_genres()
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        self.request_params.clear()
        self.ui.sort_popular.setChecked(True)
        self.ui.line_search.clear()
        [i.setChecked(False) for i in self.kinds]
        self.get_content()
