from PySide6.QtCore import Slot

from data.ui.widgets.facial import Ui_Form
from nlightreader.controlers import FilterController
from nlightreader.dialogs import FormGenres
from nlightreader.items import Manga
from nlightreader.utils import USER_CATALOGS, translate
from nlightreader.widgets.NlightContainers.manga_area import MangaArea
from nlightreader.widgets.NlightTemplates.BaseWidget import MangaItemBasedWidget
from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class FormFacial(MangaItemBasedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.manga_area = MangaArea(self.ui.items_layout)

        self.ui.next_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_btn.clicked.connect(self.turn_page_prev)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.apply_btn.clicked.connect(self.apply_filter)
        self.ui.reset_btn.clicked.connect(self.reset_filter)
        self.ui.filter_btn.clicked.connect(self.change_filters_visible)
        self.ui.catalogs_btn.clicked.connect(
            lambda: self.ui.catalogs_frame.setVisible(not self.ui.catalogs_list.isVisible()),
        )
        self.ui.catalogs_list.doubleClicked.connect(
            lambda: self.change_catalog(self.ui.catalogs_list.currentIndex().row()),
        )

        self.Form_genres = FormGenres(self)
        self.__filter_controller = FilterController()
        self.__filter_controller.set_kinds_container(self.ui.kinds_grid)
        self.__filter_controller.set_orders_container(self.ui.orders_grid)
        self.__filter_controller.set_genres_container(self.Form_genres)

        self.ui.genres_btn.clicked.connect(self.open_genres_dialog)

    def setup(self):
        if not self.catalog:
            self.ui.catalogs_frame.hide()
            self.ui.catalogs_list.clear()
            self.ui.catalogs_list.addItems([i.CATALOG_NAME for i in USER_CATALOGS])
            self.change_catalog(0)
        else:
            self.get_content()

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
        self.request_params.genres = self.__filter_controller.get_active_genres()
        self.request_params.search = self.ui.title_line.text()
        self.get_content()

    @Slot()
    def reset_filter(self):
        self.__filter_controller.reset_items()
        self.request_params.clear()
        self.request_params.order = self.__filter_controller.get_active_order()
        self.ui.title_line.clear()
        self.get_content()

    def setup_filters(self):
        self.clear_filters_items()
        orders = self.catalog.get_orders()
        kinds = self.catalog.get_kinds()
        genres = self.catalog.get_genres()
        self.ui.kinds_frame.setVisible(bool(kinds))
        self.ui.orders_frame.setVisible(bool(orders))
        self.ui.genres_frame.setVisible(bool(genres))
        self.__filter_controller.add_orders(orders)
        self.__filter_controller.add_kinds(kinds)
        self.__filter_controller.add_genres(genres)

    def clear_filters_items(self):
        self.__filter_controller.clear()

    @Slot()
    def change_filters_visible(self):
        if self.ui.filter_btn.isChecked():
            self.ui.filters_widget.setVisible(True)
        else:
            self.ui.filters_widget.setVisible(False)
            self.ui.catalogs_frame.setVisible(False)

    @Slot()
    def open_genres_dialog(self):
        self.Form_genres.exec()
