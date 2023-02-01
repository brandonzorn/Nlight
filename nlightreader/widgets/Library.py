from PySide6.QtCore import Slot, Qt, QObject, Signal

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
        self.ui.scrollAreaWidgetContents.resizeEvent = self.scroll_resize_event

    def scroll_resize_event(self, event):
        if event.oldSize().width() != event.size().width():
            self.update_manga_grid()
        event.accept()

    def update_content(self):
        for manga_item in self.manga_items:
            if manga_item.parent() == self.ui.scrollAreaWidgetContents:
                self.ui.content_grid.removeWidget(manga_item)
            manga_item.deleteLater()
        self.manga_items.clear()
        self.mangas = self.catalog.search_manga(self.request_params)
        for manga in self.mangas:
            item = self.setup_manga_item(manga)
            self.manga_items.append(item)
        self.update_manga_grid()

    def update_manga_grid(self):
        col_count = 6
        i, j = 0, 0
        for manga_item in self.manga_items:
            if manga_item.parent() == self.ui.scrollAreaWidgetContents:
                self.ui.content_grid.removeWidget(manga_item)
            manga_item.set_size(self.ui.scrollArea.size().width() // col_count)
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft)
            j += 1
            if j == col_count - 1:
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
