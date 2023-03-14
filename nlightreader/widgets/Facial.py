from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QCheckBox, QRadioButton

from data.ui.widgets.facial import Ui_Form
from nlightreader.dialogs import FormGenres
from nlightreader.items import Manga
from nlightreader.utils import USER_CATALOGS, translate
from nlightreader.widgets.BaseWidget import MangaItemBasedWidget
from nlightreader.widgets.MangaItem import MangaItem


class FormFacial(MangaItemBasedWidget):
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
        self.ui.filter_btn.clicked.connect(self.change_filters_visible)
        self.ui.scrollAreaWidgetContents.resizeEvent = self.scroll_resize_event
        self.order_items = {}
        self.kind_items = {}
        self.Form_genres = FormGenres()

    def setup(self):
        if not self.catalog:
            self.setup_catalogs()
            self.change_catalog(0)
        else:
            self.get_content()

    def add_manga_items(self):
        i, j = 0, 0
        for manga_item in self.manga_items:
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            j += 1
            if j == self.col_count - 1:
                j = 0
                i += 1

    def delete_manga_items(self):
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        for manga_item in self.manga_items:
            self.ui.content_grid.removeWidget(manga_item)
            manga_item.deleteLater()
        self.manga_items.clear()

    def update_manga_items(self):
        [manga_item.set_size(self.ui.scrollArea.size().width() // self.col_count) for manga_item in self.manga_items]

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, pool=self.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def setup_catalogs(self):
        self.ui.catalogs_frame.hide()
        self.ui.catalogs_list.clear()
        self.ui.catalogs_list.addItems([i.catalog_name for i in USER_CATALOGS])

    def change_catalog(self, index: int):
        catalog = USER_CATALOGS[index]
        self.catalog = catalog()
        self.Form_genres.catalog = catalog()
        self.setup_filters()
        self.apply_filter()

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

    @Slot()
    def change_filters_visible(self):
        if self.ui.filter_btn.isChecked():
            self.ui.filters_widget.setVisible(True)
        else:
            self.ui.filters_widget.setVisible(False)
            self.ui.catalogs_frame.setVisible(False)
