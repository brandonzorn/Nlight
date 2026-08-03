from typing import override

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.shikimori import Ui_ExternalLibraryPage
from nlightreader.core.enums import LibList
from nlightreader.items import User
from nlightreader.models import Manga
from nlightreader.parsers import ShikimoriLib
from nlightreader.parsers.catalog import CatalogAuthType, LibParser
from nlightreader.utils.threads import NWorker
from nlightreader.widgets.dialogs import (
    TokenAuthMessageBox,
    UserDataAuthMessageBox,
)
from nlightreader.widgets.items.manga_item import MangaItem
from nlightreader.widgets.pages.base_page import BaseMangaLibraryPage


class ExternalLibraryPage(BaseMangaLibraryPage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_ExternalLibraryPage()
        self._setup_ui()
        self._setup_connections()

        self.catalog: LibParser = ShikimoriLib()
        NWorker(
            target=self._get_user_info,
            callback=self._set_user_info,
        ).start()

    @override
    def _setup_ui(self) -> None:
        self.ui.setupUi(self)

        self.ui.nextButton.setIcon(FluentIcon.RIGHT_ARROW)
        self.ui.previousButton.setIcon(FluentIcon.LEFT_ARROW)

        self.manga_area.install(self.ui.itemsLayout)

    @override
    def _setup_connections(self) -> None:
        self.ui.plannedButton.clicked.connect(
            lambda: self._change_list(LibList.PLANNED),
        )
        self.ui.readingButton.clicked.connect(
            lambda: self._change_list(LibList.READING),
        )
        self.ui.onHoldButton.clicked.connect(
            lambda: self._change_list(LibList.ON_HOLD),
        )
        self.ui.completedButton.clicked.connect(
            lambda: self._change_list(LibList.COMPLETED),
        )
        self.ui.droppedButton.clicked.connect(
            lambda: self._change_list(LibList.DROPPED),
        )
        self.ui.reReadingButton.clicked.connect(
            lambda: self._change_list(LibList.RE_READING),
        )
        self.ui.nextButton.clicked.connect(self.turn_page_next)
        self.ui.previousButton.clicked.connect(self.turn_page_prev)
        self.ui.searchLineEdit.searchSignal.connect(self.search)
        self.ui.signInButton.clicked.connect(self.authorize)

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(
            manga,
            parent=self,
            is_added_to_lib=False,
            pool=self.manga_area.manga_thread_pool,
        )
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def _get_user_info(self) -> User:
        self.ui.signInButton.setEnabled(False)
        return self.catalog.get_user()

    def _set_user_info(self, user: User) -> None:
        if user.nickname:
            self.ui.signInButton.setText(user.nickname)
        else:
            self.ui.signInButton.setText(self.tr("Sign in"))
        self.ui.signInButton.setEnabled(True)

    @override
    def _update_page(self) -> None:
        self.ui.pageLabel.setText(
            f"{self.tr('Page')} {self.request_params.page}",
        )

    def auth_success_callback(self, user: User) -> None:
        self._set_user_info(user)
        self._get_content()

    @Slot()
    def authorize(self) -> None:
        match self.catalog.AUTH_TYPE:
            case CatalogAuthType.TOKEN:
                w = TokenAuthMessageBox(self.catalog, self._parent)
            case CatalogAuthType.CREDENTIALS:
                w = UserDataAuthMessageBox(self.catalog, self._parent)
            case _:
                return

        if w.exec():
            self.catalog.session.authorize(w.auth_data)
            NWorker(
                target=self._get_user_info,
                callback=self.auth_success_callback,
            ).start()

    @Slot()
    def search(self) -> None:
        self.request_params.page = 1
        self.request_params.search = self.ui.searchLineEdit.text()
        self._get_content()


__all__ = ["ExternalLibraryPage"]
