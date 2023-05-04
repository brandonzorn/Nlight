from PySide6.QtWidgets import QRadioButton, QCheckBox

from nlightreader.items import Order


class FilterController:
    def __init__(self):
        self.order_items = {}
        self.kind_items = {}

    def get_active_order(self):
        if not self.order_items:
            return Order.get_empty_instance()
        return [self.order_items[i] for i in self.order_items if i.isChecked()][-1]

    def get_active_kinds(self):
        return [self.kind_items[i] for i in self.kind_items if i.isChecked()]

    def add_orders(self, *, frame, grid, items):
        for i in items:
            item = QRadioButton(i.get_name())
            if not self.order_items:
                item.setChecked(True)
            grid.addWidget(item)
            self.order_items.update({item: i})
        frame.setVisible(bool(items))

    def add_kinds(self, *, frame, grid, items):
        for i in items:
            item = QCheckBox(i.get_name())
            grid.addWidget(item)
            self.kind_items.update({item: i})
        frame.setVisible(bool(items))

    @staticmethod
    def add_genres(*, frame, widget, items):
        for i in range(len(items)):
            check_box = QCheckBox(items[i].get_name())
            widget.genres_items.update({check_box: items[i]})
            widget.ui_ge.gridLayout.addWidget(check_box, i // 5, i % 5)
        frame.setVisible(bool(items))

    def clear(self):
        [item.deleteLater() for item in self.order_items]
        [item.deleteLater() for item in self.kind_items]
        self.order_items.clear()
        self.kind_items.clear()

    def reset_items(self):
        if self.order_items:
            list(self.order_items.keys())[0].setChecked(True)
        [i.setChecked(False) for i in self.kind_items]
