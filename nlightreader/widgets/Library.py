import webbrowser

from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QListWidgetItem

from const.lists import LibList
from data.ui.library import Ui_Form
from nlightreader.contexts.LibraryManga import LibraryMangaMenu
from nlightreader.items import Manga, RequestForm
from nlightreader.parsers import LocalLib
from nlightreader.utils import get_catalog
from nlightreader.widgets.BaseWidget import BaseWidget


class FormLibrary(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.request_params = RequestForm()
        self.catalog = LocalLib()
        self.ui.items_list.installEventFilter(self)
        self.ui.planned_btn.clicked.connect(lambda: self.change_list(LibList.planned))
        self.ui.reading_btn.clicked.connect(lambda: self.change_list(LibList.watching))
        self.ui.on_hold_btn.clicked.connect(lambda: self.change_list(LibList.on_hold))
        self.ui.completed_btn.clicked.connect(lambda: self.change_list(LibList.completed))
        self.ui.dropped_btn.clicked.connect(lambda: self.change_list(LibList.dropped))
        self.ui.re_reading_btn.clicked.connect(lambda: self.change_list(LibList.rewatching))

    def eventFilter(self, source, event):
        def remove_from_lib():
            self.catalog.db.rem_manga_library(selected_manga)
            self.get_content()

        def open_in_browser():
            webbrowser.open_new_tab(get_catalog(selected_manga.catalog_id)().get_manga_url(selected_manga))

        if event and event.type() == QEvent.ContextMenu and source is self.ui.items_list and source.itemAt(event.pos()):
            menu = LibraryMangaMenu()
            selected_item: QListWidgetItem = source.itemAt(event.pos())
            selected_manga = self.mangas[selected_item.listWidget().indexFromItem(selected_item).row()]
            menu.set_mode(1)
            selected_action = menu.exec(event.globalPos())
            match selected_action:
                case menu.remove_from_lib:
                    remove_from_lib()
                case menu.open_in_browser:
                    open_in_browser()
            return True
        return super().eventFilter(source, event)

    def setup(self):
        self.get_content()

    def get_current_manga(self) -> Manga:
        return self.mangas[self.ui.items_list.currentIndex().row()]

    def change_list(self, lst: LibList):
        self.request_params.lib_list = lst
        self.get_content()

    def get_content(self):
        self.ui.items_list.clear()
        self.mangas = self.catalog.search_manga(self.request_params)
        for manga in self.mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.items_list.addItem(item)
