from typing import override

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidgetItem, QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.facial import Ui_MainPage
from nlightreader.controlers import FiltersController
from nlightreader.models import Manga
from nlightreader.utils.catalog_manager import USER_CATALOGS
from nlightreader.widgets.dialogs import GenresDialog
from nlightreader.widgets.items.manga_item import MangaItem
from nlightreader.widgets.pages.base_page import BaseMangaPage


class MainPage(BaseMangaPage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_MainPage()
        self._setup_ui()
        self._setup_connections()

        self._genres_dialog = GenresDialog(parent)
        self._filters_controller = FiltersController(
            kinds_layout=self._ui.kindsVLayout,
            orders_layout=self._ui.ordersVLayout,
            genres_dialog=self._genres_dialog,
        )

    @override
    def _setup_ui(self) -> None:
        self._ui.setupUi(self)
        self._ui.catalogs_frame.hide()

        self._ui.next_btn.setIcon(FluentIcon.RIGHT_ARROW)
        self._ui.prev_btn.setIcon(FluentIcon.LEFT_ARROW)
        self._ui.filter_btn.setIcon(FluentIcon.FILTER)

        self._ui.catalogs_list.addItems(
            [i.CATALOG_NAME for i in USER_CATALOGS],
        )

        self.manga_area.install(self._ui.itemsLayout)

    @override
    def _setup_connections(self) -> None:
        self._ui.next_btn.clicked.connect(self.turn_page_next)
        self._ui.prev_btn.clicked.connect(self.turn_page_prev)
        self._ui.title_line.searchSignal.connect(self.search)
        self._ui.apply_btn.clicked.connect(self.apply_filter)
        self._ui.reset_btn.clicked.connect(self.reset_filter)
        self._ui.filter_btn.clicked.connect(self.change_filters_visible)
        self._ui.genresButton.clicked.connect(self.open_genres_dialog)
        self._ui.catalogsButton.clicked.connect(self._toggle_catalogs_list)
        self._ui.catalogs_list.itemClicked.connect(self._catalog_selected)

    @override
    def setup(self) -> None:
        if not self.catalog:
            self.change_catalog(0)
        else:
            self._get_content()

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(manga, pool=self.manga_area.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def change_catalog(self, index: int) -> None:
        self.catalog = USER_CATALOGS[index]()
        self.setup_filters()
        self.apply_filter()

    @override
    def _update_page(self) -> None:
        self._ui.page_label.setText(
            f"{self.tr('Page')} {self.request_params.page}",
        )

    @Slot()
    def search(self) -> None:
        self.request_params.page = 1
        self.request_params.search = self._ui.title_line.text()
        self._get_content()

    @Slot()
    def apply_filter(self) -> None:
        self._update_request_filters()
        self._get_content()

    @Slot()
    def reset_filter(self) -> None:
        self._filters_controller.reset_items()
        self._ui.title_line.clear()

        self.apply_filter()

    def _update_request_filters(self) -> None:
        self.request_params.clear()
        self.request_params.search = self._ui.title_line.text()
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
        self._ui.kindsCard.setVisible(bool(kinds))
        self._ui.ordersCard.setVisible(bool(orders))
        self._ui.genresButton.setVisible(bool(genres))
        self._filters_controller.add_orders(orders)
        self._filters_controller.add_kinds(kinds)
        self._filters_controller.add_genres(genres)

    @Slot()
    def change_filters_visible(self) -> None:
        if self._ui.filter_btn.isChecked():
            self._ui.filters_widget.setVisible(True)
        else:
            self._ui.filters_widget.setVisible(False)
            self._ui.catalogs_frame.setVisible(False)

    @Slot()
    def open_genres_dialog(self) -> None:
        self._genres_dialog.exec()

    @Slot(QListWidgetItem)
    def _catalog_selected(self, item: QListWidgetItem) -> None:
        self.change_catalog(self._ui.catalogs_list.row(item))

    @Slot()
    def _toggle_catalogs_list(self) -> None:
        self._ui.catalogs_frame.setVisible(
            not self._ui.catalogs_list.isVisible(),
        )


__all__ = ["MainPage"]
