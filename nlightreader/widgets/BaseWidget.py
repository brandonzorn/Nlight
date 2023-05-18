import time

from PySide6.QtCore import QThreadPool, Signal, QMutex, Slot
from PySide6.QtWidgets import QWidget

from nlightreader.consts import LibList
from nlightreader.items import Manga, RequestForm
from nlightreader.utils import Thread
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

        self._get_content_thread = Thread(target=self._get_content_thread_func, callback=self.update_content)

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

    @Slot()
    def turn_page_next(self):
        if self.request_params.page == 999:
            return
        self.request_params.page += 1
        self.get_content()

    @Slot()
    def turn_page_prev(self):
        if self.request_params.page == 1:
            return
        self.request_params.page -= 1
        self.get_content()

    def get_content(self):
        self.update_page()
        self._get_content_thread.terminate()
        self._get_content_thread.wait()
        self.delete_manga_items()
        self._get_content_thread.start()

    def _get_content_thread_func(self):
        page = self.request_params.page
        lib_list = self.request_params.lib_list
        time.sleep(0.25)
        if page != self.request_params.page or lib_list != self.request_params.lib_list:
            return
        self.mangas = self.catalog.search_manga(self.request_params)
        self.manga_thread_pool.setMaxThreadCount(len(self.mangas))

    def delete_manga_items(self):
        pass

    def setup_manga_item(self, manga: Manga) -> MangaItem:
        pass

    def update_page(self):
        pass

    @Slot(LibList)
    def change_list(self, lst: LibList):
        self.request_params.lib_list = lst
        self.get_content()
