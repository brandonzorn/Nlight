from threading import Thread, Lock

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QListWidgetItem, QCheckBox, QRadioButton
from nlightreader.dialogs import FormGenres
from nlightreader.utils import Database, USER_CATALOGS, lock_ui, with_lock_thread
from nlightreader.widgets.BaseWidget import BaseWidget

from data.ui.facial import Ui_Form
from items import RequestForm


class FormFacial(BaseWidget):

    lock = Lock()

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
        self.mangas = []
        self.order_items = {}
        self.kind_items = {}
        self.setup_catalogs()
        self.ui.catalogs_frame.hide()
        self.Form_genres = FormGenres()
        self.request_params = RequestForm()
        self.db: Database = Database()
        self.catalog = None
        self.change_catalog(0)

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

    @with_lock_thread(lock)
    def get_content(self):
        ui_to_lock = [self]
        with lock_ui(ui_to_lock):
            self.ui.items_list.clear()
            self.mangas = self.catalog.search_manga(self.request_params)
            for i in self.mangas:
                item = QListWidgetItem(i.get_name())
                if self.db.check_manga_library(i):
                    item.setBackground(QColor("ORANGE"))
                self.ui.items_list.addItem(item)
            self.ui.page_label.setText(f'Страница {self.request_params.page}')

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
        self.ui.page_label.setText(f'Страница {self.request_params.page}')
        Thread(target=self.get_content, daemon=True).start()

    def apply_filter(self):
        self.request_params.clear()
        if self.order_items:
            self.request_params.order = [self.order_items[i] for i in self.order_items if i.isChecked()][-1]
        self.request_params.kinds = [self.kind_items[i] for i in self.kind_items if i.isChecked()]
        self.request_params.search = self.ui.title_line.text()
        self.Form_genres.accept_genres()
        self.request_params.genres = self.Form_genres.selected_genres
        Thread(target=self.get_content).start()

    def reset_filter(self):
        self.request_params.clear()
        self.Form_genres.clear_genres()
        if self.order_items:
            list(self.order_items.keys())[0].setChecked(True)
            self.request_params.order = [self.order_items[i] for i in self.order_items if i.isChecked()][0]
        [i.setChecked(False) for i in self.kind_items]
        self.ui.title_line.clear()
        Thread(target=self.get_content).start()

    def clear_filters_items(self):
        self.kind_items.clear()
        self.order_items.clear()
        for i in reversed(range(self.ui.orders_grid.count())):
            self.ui.orders_grid.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.ui.kinds_grid.count())):
            self.ui.kinds_grid.itemAt(i).widget().deleteLater()
