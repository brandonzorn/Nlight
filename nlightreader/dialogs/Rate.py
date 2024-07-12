from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QLayout
from qfluentwidgets import FluentIcon

from data.ui.dialogs.rate import Ui_Dialog
from nlightreader.consts.enums import LIB_LISTS, Nl
from nlightreader.items import Manga
from nlightreader.utils import translate
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
        self.ui.update_btn.clicked.connect(self.send_rate)
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.delete_btn.clicked.connect(self.delete_rate)

        self.__manga = manga
        self.__catalog = get_lib_catalog(
            get_catalog_by_id(
                self.__manga.catalog_id,
            ).__class__,
        )
        self.user_rate = None

        self.setWindowTitle(self.__manga.get_name())

        self.setup()

    def setup(self):
        if not self.__catalog.check_user_rate(self.__manga):
            self.__catalog.create_user_rate(self.__manga)
        self.user_rate = self.__catalog.get_user_rate(self.__manga)
        self.ui.score_box.setValue(self.user_rate.score)
        self.ui.chapters_box.setValue(self.user_rate.chapters)
        if self.__manga.chapters:
            self.ui.chapters_box.setMaximum(self.__manga.chapters)
        self.ui.lib_list_box.setCurrentIndex(self.user_rate.status.value)

    def closeEvent(self, arg__1):
        self.deleteLater()

    @Slot()
    def send_rate(self):
        self.user_rate.score = self.ui.score_box.value()
        self.user_rate.chapters = self.ui.chapters_box.value()
        self.user_rate.status = Nl.LibList(self.ui.lib_list_box.currentIndex())
        self.__catalog.update_user_rate(self.user_rate)
        self.close()

    @Slot()
    def delete_rate(self):
        self.__catalog.delete_user_rate(self.user_rate)
        self.close()
