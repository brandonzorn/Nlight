from PySide6.QtCore import Slot, Qt

from data.ui.widgets.facial import Ui_Form
from nlightreader.controlers import FilterController
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
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.apply_btn.clicked.connect(self.apply_filter)
        self.ui.reset_btn.clicked.connect(self.reset_filter)
        self.ui.filter_btn.clicked.connect(self.change_filters_visible)
        self.ui.catalogs_btn.clicked.connect(lambda: self.ui.catalogs_frame.setVisible(
            not self.ui.catalogs_list.isVisible()))
        self.ui.catalogs_list.doubleClicked.connect(
            lambda: self.change_catalog(self.ui.catalogs_list.currentIndex().row()))
        self.ui.scrollAreaWidgetContents.resizeEvent = self.scroll_resize_event
        self.__filter_controller = FilterController()
        self.Form_genres = FormGenres()
        self.ui.genres_btn.clicked.connect(lambda: self.Form_genres.show())

    def setup(self):
        if not self.catalog:
            self.ui.catalogs_frame.hide()
            self.ui.catalogs_list.clear()
            self.ui.catalogs_list.addItems([i.catalog_name for i in USER_CATALOGS])
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
        size = self.ui.scrollArea.size().width() // self.col_count
        [manga_item.set_size(size) for manga_item in self.manga_items]

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, pool=self.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def change_catalog(self, index: int):
        catalog = USER_CATALOGS[index]
        self.catalog = catalog()
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
        self.request_params.order = self.__filter_controller.get_active_order()
        self.request_params.kinds = self.__filter_controller.get_active_kinds()
        self.request_params.genres = self.Form_genres.selected_genres
        self.request_params.search = self.ui.title_line.text()
        self.get_content()

    @Slot()
    def reset_filter(self):
        self.request_params.clear()
        self.Form_genres.reset_items()
        self.__filter_controller.reset_items()
        self.request_params.order = self.__filter_controller.get_active_order()
        self.ui.title_line.clear()
        self.get_content()

    def setup_filters(self):
        self.clear_filters_items()
        self.__filter_controller.add_orders(
            frame=self.ui.orders_frame, grid=self.ui.orders_grid, items=self.catalog.get_orders())
        self.__filter_controller.add_kinds(
            frame=self.ui.kinds_frame, grid=self.ui.kinds_grid, items=self.catalog.get_kinds())
        self.__filter_controller.add_genres(
            frame=self.ui.genres_frame, widget=self.Form_genres, items=self.catalog.get_genres())

    def clear_filters_items(self):
        self.__filter_controller.clear()
        self.Form_genres.clear()

    @Slot()
    def change_filters_visible(self):
        if self.ui.filter_btn.isChecked():
            self.ui.filters_widget.setVisible(True)
        else:
            self.ui.filters_widget.setVisible(False)
            self.ui.catalogs_frame.setVisible(False)
