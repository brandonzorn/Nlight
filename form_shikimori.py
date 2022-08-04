from threading import Thread, Lock

from PySide6.QtWidgets import QWidget, QListWidgetItem

from form_auth import FormAuth
from forms.shikimoriUI import Ui_Form
from items import Manga, RequestForm, User
from parser.Shikimori import ShikimoriLib
from utils import with_lock_thread, lock_ui


class FormShikimori(QWidget):

    lock = Lock()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.catalog = ShikimoriLib()
        self.Form_auth = FormAuth(self.catalog)
        self.request_params = RequestForm()
        self.ui.b_planned.clicked.connect(lambda: self.change_list('planned'))
        self.ui.b_watching.clicked.connect(lambda: self.change_list('watching'))
        self.ui.b_on_hold.clicked.connect(lambda: self.change_list('on_hold'))
        self.ui.b_completed.clicked.connect(lambda: self.change_list('completed'))
        self.ui.b_dropped.clicked.connect(lambda: self.change_list('dropped'))
        self.ui.b_rewatching.clicked.connect(lambda: self.change_list('rewatching'))
        self.ui.prev_page.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_page.clicked.connect(lambda: self.change_page('+'))
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.btn_auth.clicked.connect(self.authorize)
        self.Form_auth.accepted.connect(self.auth_accept)

    def setup(self):
        try:
            self.ui.btn_auth.setText(self.get_whoami().nickname)
        except AttributeError:
            self.ui.btn_auth.setText("Войти")

    def get_current_manga(self):
        return self.catalog.get_manga(self.mangas[self.ui.list_manga.currentIndex().row()])

    def auth_accept(self):
        self.catalog.session.auth_login(self.Form_auth.get_user_data())
        self.ui.btn_auth.setText(self.get_whoami().nickname)

    def authorize(self):
        self.Form_auth.hide()
        self.Form_auth.show()

    def get_whoami(self) -> User:
        return self.catalog.get_user()

    def change_page(self, page):
        match page:
            case '+':
                self.request_params.page += 1
            case '-':
                if self.request_params.page == 1:
                    return
                self.request_params.page -= 1
        self.ui.label_page.setText(f"Страница {self.request_params.page}")
        Thread(target=self.update_list, daemon=True).start()

    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.line_search.text()
        self.update_list()

    def change_list(self, list_name: str):
        self.request_params.mylist = list_name
        self.update_list()

    @with_lock_thread(lock)
    def update_list(self):
        ui_to_lock = [self.ui.search_frame, self.ui.lists_frame]
        with lock_ui(ui_to_lock):
            self.ui.list_manga.clear()
            self.mangas = self.catalog.search_manga(self.request_params)
            self.ui.label_page.setText(f'Страница {self.request_params.page}')
            for manga in self.mangas:
                item = QListWidgetItem(manga.get_name())
                self.ui.list_manga.addItem(item)
