import logging
import time
from typing import override

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from nlightreader.core.enums import LibList
from nlightreader.core.exceptions.parser_content_exc import (
    BaseContentError,
    FetchContentError,
    NoContentError,
    RequestsParamsError,
)
from nlightreader.items import RequestForm
from nlightreader.models import Manga
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.threads import NThread
from nlightreader.widgets.containers.content_container import (
    ContentContainerState,
)
from nlightreader.widgets.containers.manga_area import MangaArea
from nlightreader.widgets.items.manga_item import MangaItem

logger = logging.getLogger(__name__)


class BasePage(QWidget):
    manga_open = Signal(Manga)

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._parent: QWidget = parent

        self.catalog: AbstractCatalog | None = None
        self.request_params = RequestForm()

    def _setup_ui(self) -> None:
        pass

    def _setup_connections(self) -> None:
        pass

    def setup(self) -> None:
        self._get_content()

    def _update_content(self) -> None:
        pass

    def _get_content(self) -> None:
        self._update_content()

    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        raise NotImplementedError

    def _process_errors(self, e: BaseContentError) -> None:
        logger.error("Unhandled error:", e)


class BaseMangaPage(BasePage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._get_content_thread = NThread(
            target=self._get_content_thread_func,
            callback=self._update_content,
            error_callback=self._process_errors,
        )

        self.manga_area = MangaArea()
        self.mangas: list[Manga] = []

    @override
    def _get_content(self) -> None:
        self._update_page()
        self._get_content_thread.terminate()
        self._get_content_thread.wait()
        self.manga_area.delete_items()
        self.manga_area.set_state(ContentContainerState.FETCH_CONTENT)
        self._get_content_thread.start()

    @override
    def _update_content(self) -> None:
        self.manga_area.delete_items()
        items = [self._setup_manga_item(manga) for manga in self.mangas]
        self.manga_area.set_state(ContentContainerState.SHOW_CONTENT)
        self.manga_area.add_items(items)
        self.manga_area.update_items()

    def _update_page(self) -> None:
        pass

    @Slot()
    def turn_page_next(self) -> None:
        if self.request_params.page == 999:
            return
        self.request_params.page += 1
        self._get_content()

    @Slot()
    def turn_page_prev(self) -> None:
        if self.request_params.page == 1:
            return
        self.request_params.page -= 1
        self._get_content()

    def _get_content_thread_func(self) -> None:
        page = self.request_params.page
        lib_list = self.request_params.lib_list
        time.sleep(0.25)
        if (
            page != self.request_params.page
            or lib_list != self.request_params.lib_list
            or self.catalog is None
        ):
            return
        self.mangas = self.catalog.search_manga(self.request_params)
        if not self.mangas:
            msg = f"{self.catalog.CATALOG_NAME}: search returned no results."
            raise NoContentError(msg)

    @override
    def _process_errors(self, e: BaseContentError) -> None:
        if isinstance(e, FetchContentError):
            logger.error(e)
            self.manga_area.set_state(ContentContainerState.FETCH_ERROR)
        elif isinstance(e, (NoContentError, RequestsParamsError)):
            logger.warning(e)
            self.manga_area.set_state(ContentContainerState.NO_CONTENT)
        else:
            logger.error("Unhandled error: %s", e)


class BaseMangaLibraryPage(BaseMangaPage):
    @Slot(LibList)
    def _change_list(self, lst: LibList) -> None:
        self.request_params.lib_list = lst
        self._get_content()


__all__ = ["BasePage", "BaseMangaPage", "BaseMangaLibraryPage"]
