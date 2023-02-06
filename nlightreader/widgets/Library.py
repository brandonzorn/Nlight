from PySide6.QtCore import Qt

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
        self.add_manga_items()
        self.update_manga_items()

    def add_manga_items(self):
        i, j = 0, 0
        for manga_item in self.manga_items:
            self.ui.content_grid.addWidget(manga_item, i, j, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            j += 1
            if j == self.col_count - 1:
                j = 0
                i += 1

    def delete_manga_items(self):
        for manga_item in self.manga_items:
            self.ui.content_grid.removeWidget(manga_item)
            manga_item.deleteLater()
        self.manga_items.clear()

    def update_manga_items(self):
        [manga_item.set_size(self.ui.scrollArea.size().width() // self.col_count) for manga_item in self.manga_items]

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, pool=self.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        item.manga_changed.connect(self.get_content)
        return item

    def get_content(self):
        self.update_content()
