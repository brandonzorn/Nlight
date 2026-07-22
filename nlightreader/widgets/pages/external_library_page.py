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
from nlightreader.utils.threads import Worker
from nlightreader.widgets.dialogs import (
    TokenAuthMessageBox,
    UserDataAuthMessageBox,
)
from nlightreader.widgets.items.manga_item import MangaItem
from nlightreader.widgets.pages.base_page import BasePage


class ExternalLibraryPage(BasePage):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_ExternalLibraryPage()
        self.ui.setupUi(self)

        self.ui.nextButton.setIcon(FluentIcon.RIGHT_ARROW)
        self.ui.previousButton.setIcon(FluentIcon.LEFT_ARROW)

        self.manga_area.install(self.ui.itemsLayout)

        self.ui.plannedButton.clicked.connect(
            lambda: self.change_list(LibList.planned),
        )
        self.ui.readingButton.clicked.connect(
            lambda: self.change_list(LibList.reading),
        )
        self.ui.onHoldButton.clicked.connect(
            lambda: self.change_list(LibList.on_hold),
        )
        self.ui.completedButton.clicked.connect(
            lambda: self.change_list(LibList.completed),
        )
        self.ui.droppedButton.clicked.connect(
            lambda: self.change_list(LibList.dropped),
        )
        self.ui.reReadingButton.clicked.connect(
            lambda: self.change_list(LibList.re_reading),
        )
        self.ui.nextButton.clicked.connect(self.turn_page_next)
        self.ui.previousButton.clicked.connect(self.turn_page_prev)
        self.ui.searchLineEdit.searchSignal.connect(self.search)
        self.ui.signInButton.clicked.connect(self.authorize)
        self.catalog: LibParser = ShikimoriLib()
        Worker(
            target=self._get_user_info,
            callback=self._set_user_info,
        ).start()

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(
            manga,
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
    def update_page(self) -> None:
        self.ui.pageLabel.setText(
            f"{self.tr('Page')} {self.request_params.page}",
        )

    def auth_success_callback(self, user: User) -> None:
        self._set_user_info(user)
        self.get_content()

    @Slot()
    def authorize(self) -> None:
        match self.catalog.AUTH_TYPE:
            case CatalogAuthType.TOKEN:
                w = TokenAuthMessageBox(self.catalog, parent=self)
            case CatalogAuthType.CREDENTIALS:
                w = UserDataAuthMessageBox(self.catalog, parent=self)
            case _:
                return

        if w.exec():
            self.catalog.session.auth_login(w.get_user_data())
            Worker(
                target=self._get_user_info,
                callback=self.auth_success_callback,
            ).start()

    @Slot()
    def search(self) -> None:
        self.request_params.page = 1
        self.request_params.search = self.ui.searchLineEdit.text()
        self.get_content()


__all__ = ["ExternalLibraryPage"]
