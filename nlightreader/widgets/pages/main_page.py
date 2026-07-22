from typing import override

from PySide6.QtCore import qtTrId, Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.facial import Ui_MainPage
from nlightreader.controlers import FiltersController
from nlightreader.models import Manga
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.catalog_manager import USER_CATALOGS
from nlightreader.widgets.dialogs import GenresDialog
from nlightreader.widgets.items.manga_item import MangaItem
from nlightreader.widgets.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)

        self.ui.next_btn.setIcon(FluentIcon.RIGHT_ARROW)
        self.ui.prev_btn.setIcon(FluentIcon.LEFT_ARROW)
        self.ui.filter_btn.setIcon(FluentIcon.FILTER)

        self.manga_area.install(self.ui.itemsLayout)

        self.ui.next_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_btn.clicked.connect(self.turn_page_prev)
        self.ui.title_line.searchSignal.connect(self.search)
        self.ui.apply_btn.clicked.connect(self.apply_filter)
        self.ui.reset_btn.clicked.connect(self.reset_filter)
        self.ui.filter_btn.clicked.connect(self.change_filters_visible)
        self.ui.genresButton.clicked.connect(self.open_genres_dialog)
        self.ui.catalogsButton.clicked.connect(
            lambda: self.ui.catalogs_frame.setVisible(
                not self.ui.catalogs_list.isVisible(),
            ),
        )
        self.ui.catalogs_list.itemClicked.connect(
            lambda: self.change_catalog(
                self.ui.catalogs_list.currentIndex().row(),
            ),
        )

        self._genres_dialog = GenresDialog(self)
        self._filters_controller = FiltersController(
            kinds_layout=self.ui.kindsVLayout,
            orders_layout=self.ui.ordersVLayout,
            genres_dialog=self._genres_dialog,
        )

    @override
    def setup(self) -> None:
        if not self.catalog:
            self.ui.catalogs_frame.hide()
            self.ui.catalogs_list.clear()
            self.ui.catalogs_list.addItems(
                [i.CATALOG_NAME for i in USER_CATALOGS],
            )
            self.change_catalog(0)
        else:
            self.get_content()

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(manga, pool=self.manga_area.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def change_catalog(self, index: int) -> None:
        self.catalog: AbstractCatalog = USER_CATALOGS[index]()
        self.setup_filters()
        self.apply_filter()

    @override
    def update_page(self) -> None:
        self.ui.page_label.setText(
            f"{qtTrId('label.Page')} {self.request_params.page}",
        )

    @Slot()
    def search(self) -> None:
        self.request_params.page = 1
        self.request_params.search = self.ui.title_line.text()
        self.get_content()

    @Slot()
    def apply_filter(self) -> None:
        self._update_request_filters()
        self.get_content()

    @Slot()
    def reset_filter(self) -> None:
        self._filters_controller.reset_items()
        self.ui.title_line.clear()

        self.apply_filter()

    def _update_request_filters(self) -> None:
        self.request_params.clear()
        self.request_params.search = self.ui.title_line.text()
        self.request_params.set_order(
            self._filters_controller.get_active_order(),
        )
        self.request_params.set_kinds(
            self._filters_controller.get_active_kinds(),
        )
        self.request_params.set_genres(
            self._filters_controller.get_active_genres(),
        )

    def setup_filters(self) -> None:
        self._filters_controller.clear()
        orders = self.catalog.get_orders()
        kinds = self.catalog.get_kinds()
        genres = self.catalog.get_genres()
        self.ui.kindsCard.setVisible(bool(kinds))
        self.ui.ordersCard.setVisible(bool(orders))
        self.ui.genresButton.setVisible(bool(genres))
        self._filters_controller.add_orders(orders)
        self._filters_controller.add_kinds(kinds)
        self._filters_controller.add_genres(genres)

    @Slot()
    def change_filters_visible(self) -> None:
        if self.ui.filter_btn.isChecked():
            self.ui.filters_widget.setVisible(True)
        else:
            self.ui.filters_widget.setVisible(False)
            self.ui.catalogs_frame.setVisible(False)

    @Slot()
    def open_genres_dialog(self) -> None:
        self._genres_dialog.exec()


__all__ = ["MainPage"]
