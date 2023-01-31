import time

from PySide6.QtCore import Slot, QMutex, QObject, Signal, Qt
from PySide6.QtWidgets import QCheckBox, QRadioButton, QGridLayout

from data.ui.facial import Ui_Form
from nlightreader.dialogs import FormGenres
from nlightreader.items import RequestForm, Manga
from nlightreader.utils import USER_CATALOGS, translate, Worker
from nlightreader.widgets.BaseWidget import BaseWidget
from nlightreader.widgets.MangaItem import MangaItem


class Signals(QObject):
    manga_open = Signal(Manga)


class FormFacial(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.next_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_btn.clicked.connect(self.turn_page_prev)
        self.ui.genres_btn.clicked.connect(lambda: self.Form_genres.show())
        self.ui.apply_btn.clicked.connect(self.apply_filter)
        self.ui.reset_btn.clicked.connect(self.reset_filter)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.catalogs_btn.clicked.connect(lambda: self.ui.catalogs_frame.setVisible(
            not self.ui.catalogs_list.isVisible()))
        self.ui.catalogs_list.doubleClicked.connect(
            lambda: self.change_catalog(self.ui.catalogs_list.currentIndex().row()))
        self.ui.close_filters_btn.clicked.connect(self.change_filters_visible)
        self.mangas = []
        self.manga_items = []
        self.order_items = {}
        self.kind_items = {}
        self.signals = Signals()
        self.setup_catalogs()
        self.ui.catalogs_frame.hide()
        self.Form_genres = FormGenres()
        self.request_params = RequestForm()
        self.mutex = QMutex()
        self.catalog = None
        self.change_catalog(0)

    def setup(self):
        self.get_content()

    def resizeEvent(self, event):
        cols = self.ui.content_grid.columnCount()
        cols_available = (self.ui.scrollArea.size().width() // 200) - 1
        state_1 = cols < cols_available
        state_2 = cols > cols_available
        if (state_1 or state_2) and len(self.manga_items) > cols_available:
            self.reset_manga_grid()
            self.update_manga_grid()
        event.accept()

    def update_content(self):
        for item in self.manga_items:
            item.deleteLater()
        self.manga_items.clear()
        for manga in self.mangas:
            item = self.setup_manga_item(manga)
            self.manga_items.append(item)
        self.reset_manga_grid()
        self.update_manga_grid()

    def reset_manga_grid(self):
        for manga_item in self.manga_items:
            self.ui.content_grid.removeWidget(manga_item)
        self.ui.content_grid.deleteLater()
        self.ui.content_grid = QGridLayout()
        self.ui.content_grid.setVerticalSpacing(12)
        self.ui.scroll_layout.addLayout(self.ui.content_grid)

    def update_manga_grid(self):
        i, j = 0, 0
        for manga_item in self.manga_items:
            manga_item.set_size(self.ui.scrollArea.size().width())
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft)
            j += 1
            if j == (self.ui.scrollArea.size().width() // 200) - 1:
                j = 0
                i += 1

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga)
        item.signals.manga_clicked.connect(lambda x: self.signals.manga_open.emit(x))
        return item

    def setup_catalogs(self):
        self.ui.catalogs_list.clear()
        self.ui.catalogs_list.addItems([i.catalog_name for i in USER_CATALOGS])

    def change_filters_visible(self):
        if self.ui.close_filters_btn.isChecked():
            self.ui.filters_widget.setVisible(True)
        else:
            self.ui.filters_widget.setVisible(False)
            self.ui.catalogs_frame.setVisible(False)

    def change_catalog(self, index: int):
        catalog = USER_CATALOGS[index]
        self.catalog = catalog()
        self.Form_genres.catalog = catalog()
        self.setup_filters()
        self.apply_filter()

    def get_content(self):
        def get_content():
            page = self.request_params.page
            time.sleep(0.25)
            self.mutex.tryLock()
            if page != self.request_params.page:
                return
            self.mangas = self.catalog.search_manga(self.request_params)
            self.mutex.unlock()
        self.update_page()
        Worker(target=get_content, callback=self.update_content).start()

    @Slot()
    def turn_page_next(self):
        if self.request_params.page == 999:
            return
        self.request_params.page += 1
        self.get_content()

    @Slot()
    def turn_page_prev(self):
        if self.request_params.page == 1:
            return
        self.request_params.page -= 1
        self.get_content()

    def update_page(self):
        self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.request_params.page}")

    @Slot()
    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.title_line.text()
        self.get_content()

    @Slot()
    def apply_filter(self):
        self.request_params.clear()
        if self.order_items:
            self.request_params.order = [self.order_items[i] for i in self.order_items if i.isChecked()][-1]
        self.request_params.kinds = [self.kind_items[i] for i in self.kind_items if i.isChecked()]
        self.request_params.search = self.ui.title_line.text()
        self.Form_genres.accept_genres()
        self.request_params.genres = self.Form_genres.selected_genres
        self.get_content()

    @Slot()
    def reset_filter(self):
        self.request_params.clear()
        self.Form_genres.clear_genres()
        if self.order_items:
            list(self.order_items.keys())[0].setChecked(True)
            self.request_params.order = [self.order_items[i] for i in self.order_items if i.isChecked()][0]
        [i.setChecked(False) for i in self.kind_items]
        self.ui.title_line.clear()
        self.get_content()

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

    def clear_filters_items(self):
        self.kind_items.clear()
        self.order_items.clear()
        for i in reversed(range(self.ui.orders_grid.count())):
            self.ui.orders_grid.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.ui.kinds_grid.count())):
            self.ui.kinds_grid.itemAt(i).widget().deleteLater()
