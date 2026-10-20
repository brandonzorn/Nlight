from typing import override

from PySide6.QtCore import Qt, QThreadPool
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QLayout, QWidget
from qfluentwidgets import ScrollArea

from widgets.containers.content_container import (
    AbstractContentContainer,
    ContentContainerState,
)
from widgets.items import MangaItem


class MangaArea(ScrollArea, AbstractContentContainer):
    def __init__(self) -> None:
        super().__init__()
        self._column_count = 5
        self._spacing = 12
        self._manga_items: list[MangaItem] = []

        self._thread_pool = QThreadPool(self)
        self._thread_pool.setMaxThreadCount(self._column_count)

        self._setup_ui()

    def _setup_ui(self) -> None:
        self._scrollAreaWidgetContents = QWidget()

        self._scroll_layout = QHBoxLayout(self._scrollAreaWidgetContents)
        self._scroll_layout.setSpacing(0)
        self._scroll_layout.setContentsMargins(0, 0, 0, 0)

        self._content_grid = QGridLayout()
        self._content_grid.setSpacing(self._spacing)
        self._content_grid.setContentsMargins(0, 0, 24, 0)
        self._content_grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._scroll_layout.addLayout(self._content_grid)

        self.setWidget(self._scrollAreaWidgetContents)
        self.setWidgetResizable(True)
        self.enableTransparentBackground()

    @override
    def resizeEvent(self, arg__1: QResizeEvent, /) -> None:
        if arg__1.oldSize().width() != arg__1.size().width():
            self._scrollAreaWidgetContents.setFixedWidth(arg__1.size().width())
            if self._state == ContentContainerState.SHOW_CONTENT:
                self.update_items()
        super().resizeEvent(arg__1)

    def add_items(self, items: list[MangaItem]) -> None:
        if self._state != ContentContainerState.SHOW_CONTENT:
            msg = "this method is now available in this state"
            raise PermissionError(msg)

        for index, item in enumerate(items):
            row, col = divmod(index, self._column_count)
            self._manga_items.append(item)

            self._content_grid.addWidget(
                item,
                row,
                col,
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
            )
        self.update_items()
        for item in items:
            item.update_image(self._thread_pool)

    def delete_items(self) -> None:
        self._thread_pool.clear()
        self.verticalScrollBar().setValue(0)
        for item in self._manga_items:
            self._content_grid.removeWidget(item)
            item.deleteLater()
        self._manga_items.clear()

    def update_items(self) -> None:
        if self._state != ContentContainerState.SHOW_CONTENT:
            msg = "this method is now available in this state"
            raise PermissionError(msg)
        size = (
            self.size().width()
            - (self._content_grid.horizontalSpacing() * self._column_count)
        ) // self._column_count
        for item in self._manga_items:
            item.set_size(size)

    @override
    @property
    def _content_layout(self) -> QLayout:
        return self._scroll_layout

    @override
    @property
    def _content_widget(self) -> None:
        return None


__all__ = ["MangaArea"]
