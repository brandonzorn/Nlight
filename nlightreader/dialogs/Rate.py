from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QLayout

from data.ui.dialogs.rate import Ui_Dialog
from nlightreader.consts import lib_lists_en, parse_lib_list
from nlightreader.items import Manga
from nlightreader.utils import translate
from nlightreader.utils.catalog_manager import get_catalog, get_lib_catalog


class FormRate(QDialog):
    def __init__(self, manga: Manga, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.layout().setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ui.lib_list_box.addItems([translate("Form", i.capitalize()) for i in lib_lists_en])
        self.ui.update_btn.clicked.connect(self.send_rate)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.delete_btn.clicked.connect(self.delete_rate)
        self.manga = manga
        self.catalog = get_lib_catalog(get_catalog(self.manga.catalog_id))()

        self.user_rate = None

        self.setWindowTitle(f"{self.manga.get_name()}")

        self.setup()

    def setup(self):
        if not self.catalog.check_user_rate(self.manga):
            self.catalog.create_user_rate(self.manga)
        self.user_rate = self.catalog.get_user_rate(self.manga)
        self.ui.score_box.setValue(self.user_rate.score)
        self.ui.chapters_box.setValue(self.user_rate.chapters)
        if self.manga.chapters:
            self.ui.chapters_box.setMaximum(self.manga.chapters)
        self.ui.lib_list_box.setCurrentIndex(lib_lists_en.index(parse_lib_list(self.user_rate.status)))

    def closeEvent(self, arg__1):
        self.deleteLater()

    @Slot()
    def send_rate(self):
        self.user_rate.score = self.ui.score_box.value()
        self.user_rate.chapters = self.ui.chapters_box.value()
        self.user_rate.status = lib_lists_en[self.ui.lib_list_box.currentIndex()]
        self.catalog.update_user_rate(self.user_rate)
        self.close()

    @Slot()
    def delete_rate(self):
        self.catalog.delete_user_rate(self.user_rate)
        self.close()
