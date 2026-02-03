from PySide6.QtWidgets import QLayout
from qfluentwidgets import CheckBox, RadioButton

from nlightreader.models import Genre, Kind, Order
from nlightreader.widgets.dialogs import GenresDialog


class FiltersController:
    def __init__(self) -> None:
        self._order_items = {}
        self._kind_items = {}

        self._orders_container: QLayout | None = None
        self._kinds_container: QLayout | None = None
        self._genres_container: GenresDialog | None = None

    def get_active_order(self) -> Order | None:
        for item in self._order_items:
            if item.isChecked():
                return self._order_items[item]
        return None

    def get_active_kinds(self) -> list[Kind]:
        return [self._kind_items[i] for i in self._kind_items if i.isChecked()]

    def get_active_genres(self) -> list[Genre]:
        return self._genres_container.selected_genres

    def add_orders(self, items: list[Order]) -> None:
        if not self._orders_container:
            msg = "Orders container is not set"
            raise ValueError(msg)
        for item in items:
            item_widget = RadioButton()
            item_widget.setText(item.get_name())
            if not self._order_items:
                item_widget.setChecked(True)
            self._orders_container.addWidget(item_widget)
            self._order_items.update({item_widget: item})

    def add_kinds(self, items: list[Kind]) -> None:
        if not self._orders_container:
            msg = "Kinds container is not set"
            raise ValueError(msg)
        for item in items:
            item_widget = CheckBox()
            item_widget.setText(item.get_name())
            self._kinds_container.addWidget(item_widget)
            self._kind_items.update({item_widget: item})

    def add_genres(self, items: list[Genre]) -> None:
        if not self._orders_container:
            msg = "Genres container is not set"
            raise ValueError(msg)
        self._genres_container.set_genres(items)

    def set_orders_container(self, container) -> None:
        if not isinstance(container, QLayout):
            msg = "Container must be a QLayout"
            raise ValueError(msg)
        if self._orders_container:
            msg = "Orders container is already set"
            raise ValueError(msg)
        self._orders_container = container

    def set_kinds_container(self, container) -> None:
        if not isinstance(container, QLayout):
            msg = "Container must be a QLayout"
            raise ValueError(msg)
        if self._kinds_container:
            msg = "Kinds container is already set"
            raise ValueError(msg)
        self._kinds_container = container

    def set_genres_container(self, container) -> None:
        if not isinstance(container, GenresDialog):
            msg = "Container must be a FormGenres"
            raise ValueError(msg)
        if self._genres_container:
            msg = "Genres container is already set"
            raise ValueError(msg)
        self._genres_container = container

    def clear(self) -> None:
        [item.deleteLater() for item in self._order_items]
        [item.deleteLater() for item in self._kind_items]
        self._order_items.clear()
        self._kind_items.clear()
        self._genres_container.clear()

    def reset_items(self) -> None:
        if self._order_items:
            list(self._order_items.keys())[0].setChecked(True)
        [i.setChecked(False) for i in self._kind_items]
        self._genres_container.reset_items()


__all__ = [
    "FiltersController",
]
