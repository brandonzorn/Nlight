import time

from PySide6.QtCore import Slot, Qt

from data.ui.shikimori import Ui_Form
from nlightreader.consts import LibList
from nlightreader.dialogs import FormAuth
from nlightreader.items import Manga, User
from nlightreader.parsers import ShikimoriLib
from nlightreader.utils import translate, Worker
from nlightreader.widgets.BaseWidget import MangaItemBasedWidget
from nlightreader.widgets.MangaItem import MangaItem


class FormShikimori(MangaItemBasedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.planned_btn.clicked.connect(lambda: self.change_list(LibList.planned))
        self.ui.reading_btn.clicked.connect(lambda: self.change_list(LibList.reading))
        self.ui.on_hold_btn.clicked.connect(lambda: self.change_list(LibList.on_hold))
        self.ui.completed_btn.clicked.connect(lambda: self.change_list(LibList.completed))
        self.ui.dropped_btn.clicked.connect(lambda: self.change_list(LibList.dropped))
        self.ui.re_reading_btn.clicked.connect(lambda: self.change_list(LibList.re_reading))
        self.ui.next_btn.clicked.connect(self.turn_page_next)
        self.ui.prev_btn.clicked.connect(self.turn_page_prev)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.auth_btn.clicked.connect(self.authorize)
        self.ui.scrollAreaWidgetContents.resizeEvent = self.scroll_resize_event
        self.catalog = ShikimoriLib()
        self.Form_auth = FormAuth(self.catalog)
        self.Form_auth.accepted.connect(self.auth_accept)
        self.update_user_info()

    def delete_manga_items(self):
        for manga_item in self.manga_items:
            if manga_item.parent() == self.ui.scrollAreaWidgetContents:
                self.ui.content_grid.removeWidget(manga_item)
            manga_item.deleteLater()
        self.manga_items.clear()

    def update_manga_grid(self):
        col_count = 6
        i, j = 0, 0
        for manga_item in self.manga_items:
            manga_item.set_size(self.ui.scrollArea.size().width() // col_count)
            if manga_item.parent() == self.ui.scrollAreaWidgetContents:
                self.ui.content_grid.removeWidget(manga_item)
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            j += 1
            if j == col_count - 1:
                j = 0
                i += 1

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, is_added_to_lib=False, pool=self.manga_thread_pool)
        item.signals.manga_clicked.connect(lambda x: self.signals.manga_open.emit(x))
        return item

    def update_user_info(self):
        whoami = self.get_whoami()
        if whoami.nickname:
            self.ui.auth_btn.setText(whoami.nickname)
        else:
            self.ui.auth_btn.setText(translate("Other", "Sign in"))

    def update_page(self):
        self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.request_params.page}")

    @Slot()
    def auth_accept(self):
        self.catalog.session.auth_login(self.Form_auth.get_user_data())
        whoami = self.get_whoami()
        if whoami.nickname:
            self.ui.auth_btn.setText(whoami.nickname)
        else:
            self.ui.auth_btn.setText(translate("Other", "Sign in"))

    @Slot()
    def authorize(self):
        self.Form_auth.hide()
        self.Form_auth.show()

    def get_whoami(self) -> User:
        return self.catalog.get_user()

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

    @Slot()
    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.title_line.text()
        self.get_content()

    def change_list(self, lib_list: LibList):
        self.request_params.lib_list = lib_list
        self.get_content()

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
