from PySide6.QtCore import Slot, Qt, QObject, Signal
from PySide6.QtWidgets import QGridLayout

from data.ui.library import Ui_Form
from nlightreader.consts import LibList
from nlightreader.items import Manga, RequestForm
from nlightreader.parsers import LocalLib
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
        self.manga_items: list[MangaItem] = []
        self.signals = Signals()
        self.request_params = RequestForm()
        self.catalog = LocalLib()
        self.ui.planned_btn.clicked.connect(lambda: self.change_list(LibList.planned))
        self.ui.reading_btn.clicked.connect(lambda: self.change_list(LibList.reading))
        self.ui.on_hold_btn.clicked.connect(lambda: self.change_list(LibList.on_hold))
        self.ui.completed_btn.clicked.connect(lambda: self.change_list(LibList.completed))
        self.ui.dropped_btn.clicked.connect(lambda: self.change_list(LibList.dropped))
        self.ui.re_reading_btn.clicked.connect(lambda: self.change_list(LibList.re_reading))

    def resizeEvent(self, event):
        cols = self.ui.content_grid.columnCount()
        cols_available = (self.ui.scrollArea.size().width() // 200) - 1
        state_1 = cols < cols_available
        state_2 = cols > cols_available
        if (state_1 or state_2) and len(self.manga_items) > cols_available:
            self.reset_manga_grid()
            self.update_manga_grid()
        for item in self.manga_items:
            item.setMaximumWidth(self.ui.scrollArea.size().width() // (self.ui.scrollArea.size().width() // 200))

    def setup(self):
        self.get_content()

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
            manga_item.setMaximumWidth(self.ui.scrollArea.size().width() // (self.ui.scrollArea.size().width() // 200))
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft)
            j += 1
            if j == (self.ui.scrollArea.size().width() // 200) - 1:
                j = 0
                i += 1

    def delete_manga_item(self, manga_item: MangaItem):
        self.catalog.db.rem_manga_library(manga_item.manga)
        self.get_content()

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga)
        item.signals.manga_clicked.connect(lambda x: self.signals.manga_open.emit(x))
        item.signals.remove_from_lib.connect(lambda x: self.delete_manga_item(x))
        return item

    @Slot(LibList)
    def change_list(self, lst: LibList):
        self.request_params.lib_list = lst
        self.get_content()

    def get_content(self):
        self.update_content()
