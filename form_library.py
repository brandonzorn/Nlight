from PySide6.QtWidgets import QWidget, QListWidgetItem
from forms.desu_library import Ui_Dialog
from items import Manga, RequestForm
from parser.LocalLib import LocalLib


class FormLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.request_params = RequestForm()
        self.catalog = LocalLib()
        self.ui.b_planned.clicked.connect(lambda: self.change_list('planned'))
        self.ui.b_watching.clicked.connect(lambda: self.change_list('watching'))
        self.ui.b_on_hold.clicked.connect(lambda: self.change_list('on_hold'))
        self.ui.b_completed.clicked.connect(lambda: self.change_list('completed'))
        self.ui.b_dropped.clicked.connect(lambda: self.change_list('dropped'))
        self.ui.b_rewatching.clicked.connect(lambda: self.change_list('rewatching'))

    def get_current_manga(self) -> Manga:
        return self.mangas[self.ui.list_manga.currentIndex().row()]

    def change_list(self, list_name: str):
        self.request_params.mylist = list_name
        self.update_list()

    def update_list(self):
        self.ui.list_manga.clear()
        self.mangas = self.catalog.search_manga(self.request_params)
        for manga in self.mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.list_manga.addItem(item)
