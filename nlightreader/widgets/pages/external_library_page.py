from functools import partial
from typing import override

from PySide6.QtCore import qtTrId, Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from core.enums import LibList
from items import User
from models import Manga
from parsers import ShikimoriLib
from parsers.catalog import CatalogAuthType, LibParser
from resources.ui.widgets.shikimori import Ui_ExternalLibraryPage
from utils.threads import NWorker
from widgets.dialogs import (
    TokenAuthMessageBox,
    UserDataAuthMessageBox,
)
from widgets.items.manga_item import MangaItem
from widgets.pages.base_page import BaseMangaLibraryPage


class ExternalLibraryPage(BaseMangaLibraryPage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_ExternalLibraryPage()
        self._setup_ui()
        self._setup_connections()

        self.catalog: LibParser = ShikimoriLib()
        NWorker(
            target=self._get_user_info,
            callback=self._set_user_info,
        ).start()

    @override
    def _setup_ui(self) -> None:
        self._ui.setupUi(self)

        self._ui.nextButton.setIcon(FluentIcon.RIGHT_ARROW)
        self._ui.previousButton.setIcon(FluentIcon.LEFT_ARROW)

        self.manga_area.install(self._ui.itemsLayout)

    @override
    def _setup_connections(self) -> None:
        button_mapping = {
            self._ui.plannedButton: LibList.PLANNED,
            self._ui.readingButton: LibList.READING,
            self._ui.onHoldButton: LibList.ON_HOLD,
            self._ui.completedButton: LibList.COMPLETED,
            self._ui.droppedButton: LibList.DROPPED,
            self._ui.reReadingButton: LibList.RE_READING,
        }

        for button, lib_list in button_mapping.items():
            button.clicked.connect(partial(self._change_list, lib_list))

        self._ui.nextButton.clicked.connect(self.turn_page_next)
        self._ui.previousButton.clicked.connect(self.turn_page_prev)
        self._ui.searchLineEdit.searchSignal.connect(self.search)
        self._ui.signInButton.clicked.connect(self.authorize)

    @override
    def _setup_manga_item(self, manga: Manga) -> MangaItem:
        item = MangaItem(manga, parent=self, is_added_to_lib=False)
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def _get_user_info(self) -> User:
        self._ui.signInButton.setEnabled(False)
        return self.catalog.get_user()

    def _set_user_info(self, user: User) -> None:
        if user.nickname:
            self._ui.signInButton.setText(user.nickname)
        else:
            self._ui.signInButton.setText(self.tr("Sign in"))
        self._ui.signInButton.setEnabled(True)

    @override
    def _update_page(self) -> None:
        self._ui.pageLabel.setText(
            f"{qtTrId('label.Page')} {self.request_params.page}",
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
        self.request_params.search = self._ui.searchLineEdit.text()
        self._get_content()


__all__ = ["ExternalLibraryPage"]
