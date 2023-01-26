import webbrowser

from PySide6.QtCore import Slot, Qt, QObject, Signal
from PySide6.QtWidgets import QGridLayout

from data.ui.library import Ui_Form
from nlightreader.consts import LibList
from nlightreader.contexts import LibraryMangaMenu
from nlightreader.items import Manga, RequestForm
from nlightreader.parsers import LocalLib
from nlightreader.utils import get_catalog
from nlightreader.widgets.BaseWidget import BaseWidget
from nlightreader.widgets.MangaItem import MangaItem


class Signals(QObject):
    manga_open = Signal(Manga)


class FormLibrary(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.manga_items = []
        self.signals = Signals()
        self.request_params = RequestForm()
        self.catalog = LocalLib()
        # self.ui.items_list.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.planned_btn.clicked.connect(lambda: self.change_list(LibList.planned))
        self.ui.reading_btn.clicked.connect(lambda: self.change_list(LibList.reading))
        self.ui.on_hold_btn.clicked.connect(lambda: self.change_list(LibList.on_hold))
        self.ui.completed_btn.clicked.connect(lambda: self.change_list(LibList.completed))
        self.ui.dropped_btn.clicked.connect(lambda: self.change_list(LibList.dropped))
        self.ui.re_reading_btn.clicked.connect(lambda: self.change_list(LibList.re_reading))

    def on_context_menu(self, pos):
        def remove_from_lib():
            self.catalog.db.rem_manga_library(selected_manga)
            self.get_content()

        def open_in_browser():
            webbrowser.open_new_tab(get_catalog(selected_manga.catalog_id)().get_manga_url(selected_manga))

        menu = LibraryMangaMenu()
        selected_item = self.ui.items_list.itemAt(pos)
        selected_manga = self.mangas[selected_item.listWidget().indexFromItem(selected_item).row()]
        menu.set_mode(1)
        menu.remove_from_lib.triggered.connect(remove_from_lib)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.exec(self.ui.items_list.mapToGlobal(pos))

    def resizeEvent(self, event) -> None:
        cols = self.ui.content_grid.columnCount()
        cols_available = (self.ui.scrollArea.size().width() // 200) - 1
        state_1 = cols < cols_available
        state_2 = cols > cols_available
        if (state_1 or state_2) and len(self.manga_items) > cols_available:
            self.update_content()
        for item in self.manga_items:
            item.setMaximumWidth(self.ui.scrollArea.size().width() // (self.ui.scrollArea.size().width() // 200))

    def setup(self):
        self.get_content()

    def update_content(self):
        for item in self.manga_items:
            item.setParent(None)
        self.ui.content_grid.deleteLater()
        self.ui.content_grid = QGridLayout()
        self.ui.verticalLayout_2.addLayout(self.ui.content_grid)
        i, j = 0, 0
        for manga_item in self.manga_items:
            manga_item.setMaximumWidth(self.ui.scrollArea.size().width() // (self.ui.scrollArea.size().width() // 200))
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft)
            j += 1
            if j == (self.ui.scrollArea.size().width() // 200) - 1:
                j = 0
                i += 1

    @Slot(LibList)
    def change_list(self, lst: LibList):
        self.request_params.lib_list = lst
        self.get_content()

    def get_content(self):
        self.mangas = self.catalog.search_manga(self.request_params)
        for item in self.manga_items:
            item.deleteLater()
        self.manga_items.clear()
        for manga in self.mangas:
            item = MangaItem(manga)
            item.signals.manga_clicked.connect(lambda x: self.signals.manga_open.emit(x))
            self.manga_items.append(item)
        self.update_content()
