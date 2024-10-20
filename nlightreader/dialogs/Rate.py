from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QLayout
from qfluentwidgets import FluentIcon

from data.ui.dialogs.rate import Ui_Dialog
from nlightreader.consts.enums import LIB_LISTS, Nl
from nlightreader.models import Manga
from nlightreader.utils.translator import translate
from nlightreader.utils.catalog_manager import (
    get_catalog_by_id,
    get_lib_catalog,
)


class FormRate(QDialog):
    def __init__(self, manga: Manga, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.layout().setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ui.cancel_btn.setIcon(FluentIcon.CANCEL)
        self.ui.update_btn.setIcon(FluentIcon.UPDATE)
        self.ui.delete_btn.setIcon(FluentIcon.DELETE)
        self.ui.lib_list_box.addItems(
            [translate("Form", i.capitalize()) for i in LIB_LISTS],
        )
        self.ui.update_btn.clicked.connect(self.send_user_rate)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.delete_btn.clicked.connect(self.delete_user_rate)

        self.__manga = manga
        self.__catalog = get_lib_catalog(
            get_catalog_by_id(
                self.__manga.catalog_id,
            ).__class__,
        )
        self.__user_rate = None

        self.setWindowTitle(self.__manga.get_name())

        self.setup()

    def setup(self):
        self.fetch_user_rate()
        self.display_user_rate()

    def closeEvent(self, arg__1):
        self.deleteLater()

    def fetch_user_rate(self):
        if not self.__catalog.check_user_rate(self.__manga):
            self.__catalog.create_user_rate(self.__manga)
        self.__user_rate = self.__catalog.get_user_rate(self.__manga)

    def display_user_rate(self):
        self.ui.score_box.setValue(self.__user_rate.score)
        self.ui.chapters_box.setValue(self.__user_rate.chapters)
        if self.__manga.chapters:
            self.ui.chapters_box.setMaximum(self.__manga.chapters)
        self.ui.lib_list_box.setCurrentIndex(self.__user_rate.status.value)

    @Slot()
    def send_user_rate(self):
        self.__user_rate.score = self.ui.score_box.value()
        self.__user_rate.chapters = self.ui.chapters_box.value()
        self.__user_rate.status = Nl.LibList(
            self.ui.lib_list_box.currentIndex(),
        )
        self.__catalog.update_user_rate(self.__user_rate)
        self.close()

    @Slot()
    def delete_user_rate(self):
        self.__catalog.delete_user_rate(self.__user_rate)
        self.close()
