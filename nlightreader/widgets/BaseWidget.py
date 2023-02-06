import time

from PySide6.QtCore import QThreadPool, Signal, QMutex
from PySide6.QtWidgets import QWidget

from nlightreader.items import Manga, RequestForm
from nlightreader.utils import Worker
from nlightreader.widgets.MangaItem import MangaItem


class MangaItemBasedWidget(QWidget):
    manga_open = Signal(Manga)

    def __init__(self):
        super().__init__()
        self.mangas: list[Manga] = []
        self.manga_items: list[MangaItem] = []
        self.manga_thread_pool = QThreadPool()
        self.manga_thread_pool.setMaxThreadCount(50)
        self.col_count = 6
        self.mutex = QMutex()
        self.catalog = None
        self.request_params = RequestForm()

    def setup(self):
        self.get_content()

    def scroll_resize_event(self, event):
        if event.oldSize().width() != event.size().width():
            self.update_manga_items()
        event.accept()

    def update_content(self):
        self.delete_manga_items()
        for manga in self.mangas:
            item = self.setup_manga_item(manga)
            self.manga_items.append(item)
        self.add_manga_items()
        self.update_manga_items()

    def add_manga_items(self):
        pass

    def update_manga_items(self):
        pass

    def get_content(self):
        def get_content():
            page = self.request_params.page
            lib_list = self.request_params.lib_list
            time.sleep(0.25)
            if page != self.request_params.page or lib_list != self.request_params.lib_list:
                return
            self.mangas = self.catalog.search_manga(self.request_params)
            self.manga_thread_pool.setMaxThreadCount(len(self.mangas))

        self.update_page()
        Worker(target=get_content, callback=self.update_content, locker=self.mutex).start()

    def delete_manga_items(self):
        pass

    def setup_manga_item(self, manga: Manga) -> MangaItem:
        pass

    def update_page(self):
        pass
