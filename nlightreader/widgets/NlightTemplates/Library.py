from data.ui.widgets.library import Ui_Form

from nlightreader.consts.enums import Nl
from nlightreader.items import Manga
from nlightreader.parsers import LocalLib
from nlightreader.widgets.NlightContainers.manga_area import MangaArea
from nlightreader.widgets.NlightTemplates.BaseWidget import (
    MangaItemBasedWidget,
)
from nlightreader.widgets.NlightWidgets.manga_item import MangaItem


class FormLibrary(MangaItemBasedWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setObjectName("FormLibrary")

        self.manga_area = MangaArea(self.ui.items_layout)

        self.ui.planned_btn.clicked.connect(lambda: self.change_list(Nl.LibList.planned))
        self.ui.reading_btn.clicked.connect(lambda: self.change_list(Nl.LibList.reading))
        self.ui.on_hold_btn.clicked.connect(lambda: self.change_list(Nl.LibList.on_hold))
        self.ui.completed_btn.clicked.connect(lambda: self.change_list(Nl.LibList.completed))
        self.ui.dropped_btn.clicked.connect(lambda: self.change_list(Nl.LibList.dropped))
        self.ui.re_reading_btn.clicked.connect(lambda: self.change_list(Nl.LibList.re_reading))
        self.catalog = LocalLib()

    def update_content(self):
        self.mangas = self.catalog.search_manga(self.request_params)
        super().update_content()

    def setup_manga_item(self, manga: Manga):
        item = MangaItem(manga, pool=self.manga_area.manga_thread_pool)
        item.manga_clicked.connect(self.manga_open.emit)
        item.manga_changed.connect(self.get_content)
        return item

    def get_content(self):
        self.update_content()
