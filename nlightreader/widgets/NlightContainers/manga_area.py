from PySide6.QtCore import Qt, QThreadPool
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGridLayout

from nlightreader.utils import Thread
from nlightreader.widgets.NlightContainers.content_container import AbstractContentContainer
from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class MangaArea(QScrollArea, AbstractContentContainer):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)

        self._column_count = 5
        self._manga_items: list[MangaItem] = []

        self._scrollAreaWidgetContents = QWidget()
        self._scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self._scrollAreaWidgetContents.resizeEvent = self._scroll_resize_event

        self._scroll_layout = QVBoxLayout(self._scrollAreaWidgetContents)
        self._scroll_layout.setSpacing(0)
        self._scroll_layout.setContentsMargins(0, 0, 0, 0)

        self._content_grid = QGridLayout()
        self._content_grid.setVerticalSpacing(12)
        self._content_grid.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._scroll_layout.addLayout(self._content_grid)

        self.setWidget(self._scrollAreaWidgetContents)

        self.manga_thread_pool = QThreadPool()
        self.manga_thread_pool.setMaxThreadCount(self._column_count)
        self._set_images_thread = Thread(target=self.partial_image_addition)

    def _scroll_resize_event(self, event):
        if event.oldSize().width() != event.size().width():
            self.update_items()
        event.accept()

    def add_items(self, items: list[MangaItem]):
        i, j = 0, 0
        for item in items:
            self._manga_items.append(item)
            self._content_grid.addWidget(item, i, j, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            j += 1
            if j == self._column_count:
                j = 0
                i += 1
        self._set_images_thread.start()

    def partial_image_addition(self):
        for item in self._manga_items:
            if self.manga_thread_pool.activeThreadCount() == self.manga_thread_pool.maxThreadCount():
                self.manga_thread_pool.waitForDone()
            item.update_image()

    def delete_items(self):
        self._set_images_thread.terminate()
        self.verticalScrollBar().setValue(0)
        for item in self._manga_items:
            self._content_grid.removeWidget(item)
            item.deleteLater()
        self._manga_items.clear()

    def update_items(self):
        size = self.size().width() // (self._column_count + 1)
        [item.set_size(size) for item in self._manga_items]
