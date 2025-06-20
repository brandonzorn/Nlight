import time

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from nlightreader.consts.enums import Nl
from nlightreader.exceptions.parser_content_exc import (
    FetchContentError,
    NoContentError,
    RequestsParamsError,
)
from nlightreader.items import RequestForm
from nlightreader.models import Manga
from nlightreader.utils.threads import Thread
from nlightreader.widgets.containers.content_container import (
    ContentContainerState,
)
from nlightreader.widgets.containers.manga_area import MangaArea
from nlightreader.widgets.items.manga_item import MangaItem


class BasePage(QWidget):
    manga_open = Signal(Manga)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.manga_area = MangaArea()
        self.mangas: list[Manga] = []

        self._get_content_thread = Thread(
            target=self._get_content_thread_func,
            callback=self.update_content,
            error_callback=self.__process_errors,
        )

        self.catalog = None
        self.request_params = RequestForm()

    def setup(self):
        self.get_content()

    def update_content(self):
        self.manga_area.delete_items()
        items = [self._setup_manga_item(manga) for manga in self.mangas]
        self.manga_area.set_state(ContentContainerState.show_content)
        self.manga_area.add_items(items)
        self.manga_area.update_items()

    def __process_errors(self, exception: Exception):
        try:
            raise exception
        except FetchContentError:
            self.manga_area.set_state(ContentContainerState.fetch_error)
        except (NoContentError, RequestsParamsError):
            self.manga_area.set_state(ContentContainerState.no_content)

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
        self.manga_area.set_state(ContentContainerState.fetch_content)
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
        if not self.mangas:
            raise NoContentError

    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        raise NotImplementedError

    def update_page(self):
        pass

    @Slot(Nl.LibList)
    def change_list(self, lst: Nl.LibList):
        self.request_params.lib_list = lst
        self.get_content()


__all__ = [
    "BasePage",
]
