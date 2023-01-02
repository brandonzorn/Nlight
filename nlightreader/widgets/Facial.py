import webbrowser

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QListWidgetItem, QCheckBox, QRadioButton

from const.colors import ItemsColors
from data.ui.facial import Ui_Form
from nlightreader.contexts.LibraryManga import LibraryMangaMenu
from nlightreader.dialogs import FormGenres
from nlightreader.items import RequestForm
from nlightreader.utils import Database, USER_CATALOGS, lock_ui, get_catalog, translate, Worker
from nlightreader.widgets.BaseWidget import BaseWidget


class FormFacial(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.prev_btn.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_btn.clicked.connect(lambda: self.change_page('+'))
        self.ui.genres_btn.clicked.connect(lambda: self.Form_genres.show())
        self.ui.apply_btn.clicked.connect(self.apply_filter)
        self.ui.reset_btn.clicked.connect(self.reset_filter)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.catalogs_btn.clicked.connect(lambda: self.ui.catalogs_frame.setVisible(
            not self.ui.catalogs_list.isVisible()))
        self.ui.catalogs_list.doubleClicked.connect(
            lambda: self.change_catalog(self.ui.catalogs_list.currentIndex().row()))
        self.ui.items_list.customContextMenuRequested.connect(self.on_context_menu)
        self.mangas = []
        self.order_items = {}
        self.kind_items = {}
        self.setup_catalogs()
        self.ui.catalogs_frame.hide()
        self.Form_genres = FormGenres()
        self.request_params = RequestForm()
        self.db: Database = Database()
        self.threadpool = QThreadPool()
        self.catalog = None
        self.change_catalog(0)

    def on_context_menu(self, pos):
        def add_to_lib():
            manga = self.catalog.get_manga(selected_manga)
            self.db.add_manga(manga)
            self.db.add_manga_library(manga)
            selected_item.setBackground(ItemsColors.IN_LIBRARY)

        def remove_from_lib():
            self.db.rem_manga_library(selected_manga)
            selected_item.setBackground(ItemsColors.EMPTY)

        def open_in_browser():
            webbrowser.open_new_tab(get_catalog(selected_manga.catalog_id)().get_manga_url(selected_manga))

        menu = LibraryMangaMenu()
        selected_item = self.ui.items_list.itemAt(pos)
        selected_manga = self.mangas[selected_item.listWidget().indexFromItem(selected_item).row()]
        if self.db.check_manga_library(selected_manga):
            menu.set_mode(1)
        else:
            menu.set_mode(0)
        menu.add_to_lib.triggered.connect(add_to_lib)
        menu.remove_from_lib.triggered.connect(remove_from_lib)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.exec(self.ui.items_list.mapToGlobal(pos))

    def setup(self):
        self.update_content()

    def update_content(self):
        self.ui.items_list.clear()
        for i in self.mangas:
            item = QListWidgetItem(i.get_name())
            if self.db.check_manga_library(i):
                item.setBackground(ItemsColors.IN_LIBRARY)
            self.ui.items_list.addItem(item)

    def setup_catalogs(self):
        self.ui.catalogs_list.clear()
        self.ui.catalogs_list.addItems([i.catalog_name for i in USER_CATALOGS])

    def setup_filters(self):
        self.clear_filters_items()
        self.Form_genres.setup()
        self.ui.genres_frame.setVisible(bool(self.Form_genres.genres_items))
        self.ui.kinds_frame.setVisible(bool(self.catalog.get_kinds()))
        self.ui.orders_frame.setVisible(bool(self.catalog.get_orders()))
        for i in self.catalog.get_orders():
            item = QRadioButton(i.get_name())
            if not self.order_items:
                item.setChecked(True)
            self.ui.orders_grid.addWidget(item)
            self.order_items.update({item: i})
        for i in self.catalog.get_kinds():
            item = QCheckBox(i.get_name())
            self.ui.kinds_grid.addWidget(item)
            self.kind_items.update({item: i})

    def get_current_manga(self):
        return self.catalog.get_manga(self.mangas[self.ui.items_list.currentIndex().row()])

    def change_catalog(self, index: int):
        catalog = USER_CATALOGS[index]
        self.catalog = catalog()
        self.Form_genres.catalog = catalog()
        self.setup_filters()
        self.apply_filter()

    def get_content(self):
        ui_to_lock = [self]
        with lock_ui(ui_to_lock):
            self.mangas = self.catalog.search_manga(self.request_params)
            self.update_content()
            self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.request_params.page}")

    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.title_line.text()
        self.get_content()

    def change_page(self, page):
        match page:
            case '+':
                self.request_params.page += 1
            case '-':
                if self.request_params.page > 1:
                    self.request_params.page -= 1
                else:
                    return
        self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.request_params.page}")
        Worker(self.get_content).start()

    def apply_filter(self):
        self.request_params.clear()
        if self.order_items:
            self.request_params.order = [self.order_items[i] for i in self.order_items if i.isChecked()][-1]
        self.request_params.kinds = [self.kind_items[i] for i in self.kind_items if i.isChecked()]
        self.request_params.search = self.ui.title_line.text()
        self.Form_genres.accept_genres()
        self.request_params.genres = self.Form_genres.selected_genres
        Worker(self.get_content).start()

    def reset_filter(self):
        self.request_params.clear()
        self.Form_genres.clear_genres()
        if self.order_items:
            list(self.order_items.keys())[0].setChecked(True)
            self.request_params.order = [self.order_items[i] for i in self.order_items if i.isChecked()][0]
        [i.setChecked(False) for i in self.kind_items]
        self.ui.title_line.clear()
        Worker(self.get_content).start()

    def clear_filters_items(self):
        self.kind_items.clear()
        self.order_items.clear()
        for i in reversed(range(self.ui.orders_grid.count())):
            self.ui.orders_grid.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.ui.kinds_grid.count())):
            self.ui.kinds_grid.itemAt(i).widget().deleteLater()
