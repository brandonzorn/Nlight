from PySide6.QtCore import Slot
from qfluentwidgets import FluentIcon

from data.ui.widgets.shikimori import Ui_Form
from nlightreader.consts.enums import Nl
from nlightreader.dialogs import TokenAuthMessageBox, UserDataAuthMessageBox
from nlightreader.items import User
from nlightreader.models import Manga
from nlightreader.parsers import ShikimoriLib
from nlightreader.utils import translate, Worker
from nlightreader.widgets.NlightTemplates.BaseWidget import (
    MangaItemBasedWidget,
)
from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class FormShikimori(MangaItemBasedWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.next_btn.setIcon(FluentIcon.RIGHT_ARROW)
        self.ui.prev_btn.setIcon(FluentIcon.LEFT_ARROW)

        self.setObjectName("FormShikimori")

        self.manga_area.install(self.ui.items_layout)
        self.manga_area.get_content_widget().layout().addWidget(
            self.progressRing,
        )

        self.ui.planned_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.planned),
        )
        self.ui.reading_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.reading),
        )
        self.ui.on_hold_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.on_hold),
        )
        self.ui.completed_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.completed),
        )
        self.ui.dropped_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.dropped),
        )
        self.ui.re_reading_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.re_reading),
        )
        self.ui.next_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_btn.clicked.connect(self.turn_page_prev)
        self.ui.title_line.searchSignal.connect(self.search)
        self.ui.auth_btn.clicked.connect(self.authorize)
        self.catalog = ShikimoriLib()
        Worker(target=self.get_user_info, callback=self.set_user_info).start()

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(
            manga,
            is_added_to_lib=False,
            pool=self.manga_area.manga_thread_pool,
        )
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def get_user_info(self):
        self.ui.auth_btn.setEnabled(False)
        return self.catalog.get_user()

    def set_user_info(self, user: User):
        if user.nickname:
            self.ui.auth_btn.setText(user.nickname)
            self.get_content()
        else:
            self.ui.auth_btn.setText(
                translate("Other", "Sign in"),
            )
        self.ui.auth_btn.setEnabled(True)

    def update_page(self):
        self.ui.page_label.setText(
            f"{translate('Other', 'Page')} {self.request_params.page}",
        )

    @Slot()
    def authorize(self):
        if self.catalog.fields == 1:
            w = TokenAuthMessageBox(self.catalog, parent=self)
        else:
            w = UserDataAuthMessageBox(self.catalog, parent=self)
        if w.exec():
            self.catalog.session.auth_login(w.get_user_data())
            Worker(
                target=self.get_user_info,
                callback=self.set_user_info,
            ).start()

    @Slot()
    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.title_line.text()
        self.get_content()
