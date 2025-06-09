from PySide6.QtWidgets import QLayout
from qfluentwidgets import CheckBox, RadioButton

from nlightreader.models import Genre, Kind, Order
from nlightreader.widgets.dialogs import GenresDialog


class FilterController:
    def __init__(self):
        self.max_genres_per_row = 5

        self._order_items = {}
        self._kind_items = {}

        self._orders_container = None
        self._kinds_container = None
        self._genres_container = None

    def get_active_order(self) -> Order | None:
        for item in self._order_items:
            if item.isChecked():
                return self._order_items[item]

    def get_active_kinds(self) -> list[Kind]:
        return [self._kind_items[i] for i in self._kind_items if i.isChecked()]

    def get_active_genres(self) -> list[Genre]:
        return self._genres_container.selected_genres

    def add_orders(self, items: list[Order]):
        if not self._orders_container:
            raise ValueError("Orders container is not set")
        for item in items:
            item_widget = RadioButton()
            item_widget.setText(item.get_name())
            if not self._order_items:
                item_widget.setChecked(True)
            self._orders_container.addWidget(item_widget)
            self._order_items.update({item_widget: item})

    def add_kinds(self, items: list[Kind]):
        if not self._orders_container:
            raise ValueError("Kinds container is not set")
        for item in items:
            item_widget = CheckBox()
            item_widget.setText(item.get_name())
            self._kinds_container.addWidget(item_widget)
            self._kind_items.update({item_widget: item})

    def add_genres(self, items: list[Genre]):
        if not self._orders_container:
            raise ValueError("Genres container is not set")
        for index, item in enumerate(items):
            item_widget = CheckBox()
            item_widget.setText(item.get_name())
            self._genres_container.genres_items.update({item_widget: item})
            self._genres_container.ui_ge.gridLayout.addWidget(
                item_widget,
                index // self.max_genres_per_row,
                index % self.max_genres_per_row,
            )

    def set_orders_container(self, container):
        if not isinstance(container, QLayout):
            raise ValueError("Container must be a QLayout")
        if self._orders_container:
            raise ValueError("Orders container is already set")
        self._orders_container = container

    def set_kinds_container(self, container):
        if not isinstance(container, QLayout):
            raise ValueError("Container must be a QLayout")
        if self._kinds_container:
            raise ValueError("Kinds container is already set")
        self._kinds_container = container

    def set_genres_container(self, container):
        if not isinstance(container, GenresDialog):
            raise ValueError("Container must be a FormGenres")
        if self._genres_container:
            raise ValueError("Genres container is already set")
        self._genres_container = container

    def clear(self):
        [item.deleteLater() for item in self._order_items]
        [item.deleteLater() for item in self._kind_items]
        self._order_items.clear()
        self._kind_items.clear()
        self._genres_container.clear()

    def reset_items(self):
        if self._order_items:
            list(self._order_items.keys())[0].setChecked(True)
        [i.setChecked(False) for i in self._kind_items]
        self._genres_container.reset_items()


__all__ = [
    "FilterController",
]
