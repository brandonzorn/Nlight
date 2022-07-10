import contextlib
import os
from threading import Thread, Lock

from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QWidget, QListWidgetItem

from catalog_manager import get_catalog, CATALOGS
from const.icons import search_icon_path, prev_page_icon_path, next_page_icon_path
from database import Database
from form_genres import FormGenres
from forms.desuUI import Ui_Dialog
from items import RequestForm
from utils import with_lock_thread


class FormFacial(QWidget):

    lock = Lock()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.prev_page.setIcon(QIcon(prev_page_icon_path))
        self.ui.next_page.setIcon(QIcon(next_page_icon_path))
        self.ui.btn_search.setIcon(QIcon(search_icon_path))
        self.ui.prev_page.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_page.clicked.connect(lambda: self.change_page('+'))
        self.ui.btn_genres_list.clicked.connect(self.clicked_genres)
        self.ui.filter_apply.clicked.connect(self.filter_apply)
        self.ui.filter_reset.clicked.connect(self.filter_reset)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.btn_catalogs.clicked.connect(self.clicked_catalogs)
        self.ui.catalog_list.doubleClicked.connect(
            lambda: self.update_catalog(self.ui.catalog_list.currentIndex().row()))
        self.mangas = []
        self.cur_page = 1
        self.order_by = {self.ui.sort_name: 'name', self.ui.sort_popular: 'popular'}
        self.kinds = {self.ui.type_manga: 'manga', self.ui.type_manhwa: 'manhwa', self.ui.type_manhua: 'manhua',
                      self.ui.type_one_shot: 'one_shot', self.ui.type_comics: 'comics'}
        self.setup_catalogs()
        self.ui.catalog_list.hide()
        self.Form_genres = FormGenres()
        self.request_params = RequestForm()
        self.db: Database = Database()
        self.catalog = get_catalog()()
        self.wd = os.getcwd()
        Thread(target=self.get_content, daemon=True).start()

    def clicked_genres(self):
        self.Form_genres.show()

    def get_current_manga(self):
        return self.catalog.get_manga(self.mangas[self.ui.list_manga.currentIndex().row()])

    def update_catalog(self, index: int):
        catalog = get_catalog(index)
        self.catalog = catalog()
        self.Form_genres.catalog = catalog()
        self.setup_filters()
        self.get_content()

    def setup_filters(self):
        self.Form_genres.setup()
        self.ui.genres_frame.setVisible(bool(self.Form_genres.genres_items))
        self.ui.kind_frame.setVisible(bool(self.catalog.get_kinds()))
        self.ui.order_frame.setVisible(bool(self.catalog.get_orders()))

    def clicked_catalogs(self):
        if self.ui.catalog_list.isHidden():
            self.ui.catalog_list.show()
        else:
            self.ui.catalog_list.hide()

    def setup_catalogs(self):
        self.ui.catalog_list.clear()
        self.ui.catalog_list.addItems([i.catalog_name for i in CATALOGS.values()])

    @with_lock_thread(lock)
    def get_content(self):
        with self.lock_ui():
            self.ui.list_manga.clear()
            self.request_params.page = self.cur_page
            self.mangas = self.catalog.search_manga(self.request_params)
            for i in self.mangas:
                item = QListWidgetItem(i.get_name())
                if self.db.check_manga_library(i):
                    item.setBackground(QColor("ORANGE"))
                self.ui.list_manga.addItem(item)
            self.ui.label_page.setText(f'Страница {self.cur_page}')

    @contextlib.contextmanager
    def lock_ui(self):
        ui_to_lock = (self.ui.filters_frame, self.ui.search_frame)
        [i.setEnabled(False) for i in ui_to_lock]
        yield
        [i.setEnabled(True) for i in ui_to_lock]

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
                else:
                    return
        self.ui.label_page.setText(f'Страница {self.cur_page}')
        Thread(target=self.get_content, daemon=True).start()

    def filter_apply(self):
        self.cur_page = 1
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
        self.request_params.clear()
        self.ui.sort_popular.setChecked(True)
        self.ui.line_search.clear()
        [i.setChecked(False) for i in self.kinds]
        self.get_content()
