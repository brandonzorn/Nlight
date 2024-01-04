from PySide6.QtCore import Slot

from data.ui.widgets.shikimori import Ui_Form
from nlightreader.consts import LibList
from nlightreader.dialogs import FormAuth
from nlightreader.items import Manga
from nlightreader.parsers import ShikimoriLib
from nlightreader.utils import translate, Worker
from nlightreader.widgets.NlightContainers.manga_area import MangaArea
from nlightreader.widgets.NlightTemplates.BaseWidget import MangaItemBasedWidget
from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class FormShikimori(MangaItemBasedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.manga_area = MangaArea(self.ui.items_layout)

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
        self.catalog = ShikimoriLib()
        self.Form_auth = FormAuth(self.catalog, parent=self)
        self.Form_auth.accepted.connect(self.auth_accept)
        self.update_user_info()

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, is_added_to_lib=False, pool=self.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        return item

    def update_user_info(self):
        def get_user_info():
            self.whoami = self.catalog.get_user()

        def set_user_info():
            if self.whoami.nickname:
                self.ui.auth_btn.setText(self.whoami.nickname)
            else:
                self.ui.auth_btn.setText(translate("Other", "Sign in"))
            self.ui.auth_btn.setEnabled(True)

        self.ui.auth_btn.setEnabled(False)
        Worker(target=get_user_info, callback=set_user_info).start()

    def update_page(self):
        self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.request_params.page}")

    @Slot()
    def auth_accept(self):
        self.catalog.session.auth_login(self.Form_auth.get_user_data())
        self.update_user_info()

    @Slot()
    def authorize(self):
        self.Form_auth.exec()

    @Slot()
    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.title_line.text()
        self.get_content()
