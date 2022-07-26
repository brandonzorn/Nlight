from threading import Thread, Lock

from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QWidget, QListWidgetItem, QCheckBox, QRadioButton

from catalog_manager import get_catalog, CATALOGS
from const.icons import search_icon_path, prev_page_icon_path, next_page_icon_path
from database import Database
from form_genres import FormGenres
from forms.desuUI import Ui_Dialog
from items import RequestForm
from utils import with_lock_thread, lock_ui


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
        self.ui.btn_catalogs.clicked.connect(lambda: self.ui.catalog_list.setVisible(
            not self.ui.catalog_list.isVisible()))
        self.ui.catalog_list.doubleClicked.connect(
            lambda: self.update_catalog(self.ui.catalog_list.currentIndex().row()))
        self.mangas = []
        self.order_items = {}
        self.kind_items = {}
        self.cur_page = 1
        self.setup_catalogs()
        self.ui.catalog_list.hide()
        self.Form_genres = FormGenres()
        self.request_params = RequestForm()
        self.db: Database = Database()
        self.catalog = None
        self.update_catalog(0)

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
        self.clear_filters_items()
        self.Form_genres.setup()
        self.ui.genres_frame.setVisible(bool(self.Form_genres.genres_items))
        self.ui.kind_frame.setVisible(bool(self.catalog.get_kinds()))
        self.ui.order_frame.setVisible(bool(self.catalog.get_orders()))
        for i in self.catalog.get_orders():
            item = QRadioButton(i.get_name())
            if not self.order_items:
                item.setChecked(True)
            self.ui.order_grid.addWidget(item)
            self.order_items.update({item: i})
        for i in self.catalog.get_kinds():
            item = QCheckBox(i.get_name())
            self.ui.kind_grid.addWidget(item)
            self.kind_items.update({item: i})

    def clear_filters_items(self):
        self.kind_items.clear()
        self.order_items.clear()
        for i in reversed(range(self.ui.order_grid.count())):
            self.ui.order_grid.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.ui.kind_grid.count())):
            self.ui.kind_grid.itemAt(i).widget().deleteLater()

    def setup_catalogs(self):
        self.ui.catalog_list.clear()
        self.ui.catalog_list.addItems([i.catalog_name for i in CATALOGS.values()])

    @with_lock_thread(lock)
    def get_content(self):
        ui_to_lock = [self.ui.filters_frame, self.ui.search_frame]
        with lock_ui(ui_to_lock):
            self.ui.list_manga.clear()
            self.request_params.page = self.cur_page
            self.mangas = self.catalog.search_manga(self.request_params)
            for i in self.mangas:
                item = QListWidgetItem(i.get_name())
                if self.db.check_manga_library(i):
                    item.setBackground(QColor("ORANGE"))
                self.ui.list_manga.addItem(item)
            self.ui.label_page.setText(f'Страница {self.cur_page}')

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
        self.request_params.order = [self.order_items[i].name for i in self.order_items if i.isChecked()]
        self.request_params.kinds = [self.kind_items[i].name for i in self.kind_items if i.isChecked()]
        self.request_params.search = self.ui.line_search.text()
        self.Form_genres.accept_genres()
        self.request_params.genres = self.Form_genres.selected_genres
        self.get_content()

    def filter_reset(self):
        self.cur_page = 1
        self.request_params.clear()
        self.Form_genres.clear_genres()
        if self.order_items:
            list(self.order_items.keys())[0].setChecked(True)
        [i.setChecked(False) for i in self.kind_items]
        self.ui.line_search.clear()
        self.get_content()
