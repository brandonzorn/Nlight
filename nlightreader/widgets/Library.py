from PySide6.QtCore import Slot, Qt

from data.ui.library import Ui_Form
from nlightreader.consts import LibList
from nlightreader.items import Manga
from nlightreader.parsers import LocalLib
from nlightreader.widgets.BaseWidget import MangaItemBasedWidget
from nlightreader.widgets.MangaItem import MangaItem


class FormLibrary(MangaItemBasedWidget):
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
        self.ui.scrollAreaWidgetContents.resizeEvent = self.scroll_resize_event
        self.catalog = LocalLib()

    def update_content(self):
        self.mangas = self.catalog.search_manga(self.request_params)
        self.manga_thread_pool.setMaxThreadCount(len(self.mangas))
        self.delete_manga_items()
        for manga in self.mangas:
            item = self.setup_manga_item(manga)
            self.manga_items.append(item)
        self.update_manga_grid()

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
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft)
            j += 1
            if j == col_count - 1:
                j = 0
                i += 1

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, pool=self.manga_thread_pool)
        item.signals.manga_clicked.connect(lambda x: self.signals.manga_open.emit(x))
        item.signals.manga_changed.connect(self.get_content)
        return item

    @Slot(LibList)
    def change_list(self, lst: LibList):
        self.request_params.lib_list = lst
        self.get_content()

    def get_content(self):
        self.update_content()
