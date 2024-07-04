import time

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import IndeterminateProgressRing

from nlightreader.consts.enums import Nl
from nlightreader.items import Manga, RequestForm
from nlightreader.utils import Thread
from nlightreader.widgets.NlightContainers.manga_area import MangaArea
from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class MangaItemBasedWidget(QWidget):
    manga_open = Signal(Manga)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.manga_area = MangaArea()
        self.mangas: list[Manga] = []

        self.progressRing = IndeterminateProgressRing()
        self.progressRing.setVisible(False)

        self._get_content_thread = Thread(
            target=self._get_content_thread_func,
            callback=self.update_content,
        )

        self.catalog = None
        self.request_params = RequestForm()

    def setup(self):
        self.get_content()

    def update_content(self):
        self.manga_area.delete_items()
        items = [self.setup_manga_item(manga) for manga in self.mangas]
        self.progressRing.stop()
        self.progressRing.setVisible(False)
        self.manga_area.add_items(items)
        self.manga_area.update_items()

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
        self.manga_area.delete_items()
        self.progressRing.setVisible(True)
        self.progressRing.start()
        self._get_content_thread.start()

    def _get_content_thread_func(self):
        page = self.request_params.page
        lib_list = self.request_params.lib_list
        time.sleep(0.25)
        if (
                page != self.request_params.page
                or lib_list != self.request_params.lib_list
        ):
            return
        self.mangas = self.catalog.search_manga(self.request_params)

    def setup_manga_item(self, manga: Manga) -> MangaItem:
        pass

    def update_page(self):
        pass

    @Slot(Nl.LibList)
    def change_list(self, lst: Nl.LibList):
        self.request_params.lib_list = lst
        self.get_content()
