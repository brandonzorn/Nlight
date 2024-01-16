from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy
from qfluentwidgets import ScrollArea

from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class MangaArea(ScrollArea):
    def __init__(self, parent):
        super().__init__()
        self.setWidgetResizable(True)

        self._column_count = 6
        self._manga_items: list[MangaItem] = []

        self._scrollAreaWidgetContents = QWidget()
        self._scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self._scrollAreaWidgetContents.resizeEvent = self._scroll_resize_event

        self._scroll_layout = QVBoxLayout(self._scrollAreaWidgetContents)
        self._scroll_layout.setSpacing(0)
        self._scroll_layout.setContentsMargins(0, 0, 0, 0)

        self._content_grid = QGridLayout()
        self._content_grid.setVerticalSpacing(12)

        self._scroll_layout.addLayout(self._content_grid)

        self._verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self._scroll_layout.addItem(self._verticalSpacer)
        self.setWidget(self._scrollAreaWidgetContents)
        
        self.setStyleSheet("QScrollArea {border: none;}")

        if parent is not None:
            parent.addWidget(self)

    def _scroll_resize_event(self, event):
        if event.oldSize().width() != event.size().width():
            self.update_items()
        event.accept()

    def add_items(self, items: list[MangaItem]):
        i, j = 0, 0
        for item in items:
            self._manga_items.append(item)
            self._content_grid.addWidget(item, i, j, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            item.update_image()
            j += 1
            if j == self._column_count - 1:
                j = 0
                i += 1

    def delete_items(self):
        self.verticalScrollBar().setValue(0)
        for item in self._manga_items:
            self._content_grid.removeWidget(item)
            item.deleteLater()
        self._manga_items.clear()

    def update_items(self):
        size = self.size().width() // self._column_count
        [item.set_size(size) for item in self._manga_items]
