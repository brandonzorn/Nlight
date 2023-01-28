import time

from PySide6.QtCore import Slot, QMutex, QObject, Signal, Qt
from PySide6.QtWidgets import QGridLayout

from data.ui.shikimori import Ui_Form
from nlightreader.consts import LibList
from nlightreader.dialogs import FormAuth
from nlightreader.items import Manga, RequestForm, User
from nlightreader.parsers import ShikimoriLib
from nlightreader.utils import Database, translate, Worker
from nlightreader.widgets.BaseWidget import BaseWidget
from nlightreader.widgets.MangaItem import MangaItem


class Signals(QObject):
    manga_open = Signal(Manga)


class FormShikimori(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.manga_items = []
        self.catalog = ShikimoriLib()
        self.signals = Signals()
        self.Form_auth = FormAuth(self.catalog)
        self.request_params = RequestForm()
        self.db: Database = Database()
        self.mutex = QMutex()
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
        self.Form_auth.accepted.connect(self.auth_accept)
        self.update_user_info()

    def setup(self):
        self.update_content()

    def resizeEvent(self, event):
        cols = self.ui.content_grid.columnCount()
        cols_available = (self.ui.scrollArea.size().width() // 200) - 1
        state_1 = cols < cols_available
        state_2 = cols > cols_available
        if (state_1 or state_2) and len(self.manga_items) > cols_available:
            self.reset_manga_grid()
            self.update_manga_grid()
        event.accept()

    def update_content(self):
        self.mangas = self.catalog.search_manga(self.request_params)
        for item in self.manga_items:
            item.deleteLater()
        self.manga_items.clear()
        for manga in self.mangas:
            item = self.setup_manga_item(manga)
            self.manga_items.append(item)
        self.reset_manga_grid()
        self.update_manga_grid()

    def reset_manga_grid(self):
        for manga_item in self.manga_items:
            self.ui.content_grid.removeWidget(manga_item)
        self.ui.content_grid.deleteLater()
        self.ui.content_grid = QGridLayout()
        self.ui.content_grid.setVerticalSpacing(12)
        self.ui.scroll_layout.addLayout(self.ui.content_grid)

    def update_manga_grid(self):
        i, j = 0, 0
        for manga_item in self.manga_items:
            manga_item.set_size(self.ui.scrollArea.size().width())
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft)
            j += 1
            if j == (self.ui.scrollArea.size().width() // 200) - 1:
                j = 0
                i += 1

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga)
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
            self.mutex.tryLock()
            if page != self.request_params.page or lib_list != self.request_params.lib_list:
                return
            self.mangas = self.catalog.search_manga(self.request_params)
            self.mutex.unlock()
        self.update_page()
        Worker(target=get_content, callback=self.update_content).start()
