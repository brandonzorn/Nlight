from typing import override

from data.ui.widgets.library import Ui_Form

from nlightreader.consts.enums import Nl
from nlightreader.models import Manga
from nlightreader.parsers import LocalLibrary
from nlightreader.widgets.pages.base_page import BasePage
from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class LibraryPage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setObjectName("FormLibrary")

        self.manga_area.install(self.ui.items_layout)

        self.ui.planned_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.planned),
        )
        self.ui.reading_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.reading),
        )
        self.ui.on_hold_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.on_hold),
        )
        self.ui.completed_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.completed),
        )
        self.ui.dropped_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.dropped),
        )
        self.ui.re_reading_btn.clicked.connect(
            lambda: self.change_list(Nl.LibList.re_reading),
        )
        self.catalog = LocalLibrary()

    @override
    def _setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, pool=self.manga_area.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        item.manga_changed.connect(self.get_content)
        return item
