from PySide6.QtCore import QThreadPool, QObject, Signal, QMutex
from PySide6.QtWidgets import QWidget

from nlightreader.items import Manga, RequestForm
from nlightreader.widgets.MangaItem import MangaItem


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.get_content()

    def update_content(self):
        pass

    def get_content(self):
        pass


class Signals(QObject):
    manga_open = Signal(Manga)


class MangaItemBasedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.mangas: list[Manga] = []
        self.manga_items: list[MangaItem] = []
        self.manga_thread_pool = QThreadPool()
        self.manga_thread_pool.setMaxThreadCount(50)
        self.signals = Signals()
        self.mutex = QMutex()
        self.request_params = RequestForm()

    def setup(self):
        self.get_content()

    def scroll_resize_event(self, event):
        if event.oldSize().width() != event.size().width():
            self.update_manga_grid()
        event.accept()

    def update_content(self):
        self.delete_manga_items()
        for manga in self.mangas:
            item = self.setup_manga_item(manga)
            self.manga_items.append(item)
        self.update_manga_grid()

    def update_manga_grid(self):
        pass

    def get_content(self):
        pass

    def delete_manga_items(self):
        pass

    def setup_manga_item(self, manga: Manga) -> MangaItem:
        pass
