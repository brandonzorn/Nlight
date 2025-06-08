from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QHBoxLayout
from qfluentwidgets import (
    BodyLabel,
    CardWidget,
    ComboBox,
    HorizontalSeparator,
    MessageBoxBase,
    PushButton,
    SpinBox,
    SubtitleLabel,
)

from nlightreader.consts.enums import LIB_LISTS, Nl
from nlightreader.models import Manga
from nlightreader.utils.catalog_manager import (
    get_catalog_by_id,
    get_lib_catalog,
)
from nlightreader.utils.translator import translate


class RateDialog(MessageBoxBase):
    def __init__(self, manga: Manga, parent):
        super().__init__(parent)
        self.title_label = SubtitleLabel(self.tr("Change rating"), parent=self)

        self.chapters_frame = CardWidget()
        self.chapters_frame_layout = QHBoxLayout(self.chapters_frame)
        self.chapters_frame_label = BodyLabel(
            self.tr("Chapters read"),
            parent=self.chapters_frame,
        )
        self.chapters_frame_separator = HorizontalSeparator(
            self.chapters_frame,
        )
        self.chapters_count_spin = SpinBox(parent=self.chapters_frame)
        self.chapters_count_spin.setMaximum(999)
        self.chapters_frame_layout.addWidget(self.chapters_frame_label)
        self.chapters_frame_layout.addWidget(self.chapters_frame_separator)
        self.chapters_frame_layout.addWidget(self.chapters_count_spin)

        self.score_frame = CardWidget()
        self.score_frame_layout = QHBoxLayout(self.score_frame)
        self.score_frame_label = BodyLabel(
            self.tr("Rating"),
            parent=self.score_frame,
        )
        self.score_frame_separator = HorizontalSeparator(self.score_frame)
        self.score_spin = SpinBox()
        self.score_spin.setMaximum(10)
        self.score_frame_layout.addWidget(self.score_frame_label)
        self.score_frame_layout.addWidget(self.score_frame_separator)
        self.score_frame_layout.addWidget(self.score_spin)

        self.lib_list_frame = CardWidget()
        self.lib_list_frame_layout = QHBoxLayout(self.lib_list_frame)
        self.lib_list_frame_label = BodyLabel(
            self.tr("List"),
            parent=self.lib_list_frame,
        )
        self.lib_list_frame_separator = HorizontalSeparator(
            self.lib_list_frame,
        )
        self.lib_list_combo = ComboBox()
        self.lib_list_combo.addItems(
            [translate("Form", i.capitalize()) for i in LIB_LISTS],
        )
        self.lib_list_frame_layout.addWidget(self.lib_list_frame_label)
        self.lib_list_frame_layout.addWidget(self.lib_list_frame_separator)
        self.lib_list_frame_layout.addWidget(self.lib_list_combo)

        self.delete_rate_button = PushButton()
        self.delete_rate_button.clicked.connect(self.delete_user_rate)
        self.delete_rate_button.setText(self.tr("Delete"))
        self.buttonLayout.addWidget(
            self.delete_rate_button,
            1,
            Qt.AlignmentFlag.AlignVCenter,
        )

        self.viewLayout.addWidget(self.title_label)
        self.viewLayout.addWidget(self.chapters_frame)
        self.viewLayout.addWidget(self.score_frame)
        self.viewLayout.addWidget(self.lib_list_frame)

        self.accepted.connect(self.send_user_rate)
        self.rejected.connect(self.close)

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
        self.score_spin.setValue(self.__user_rate.score)
        self.chapters_count_spin.setValue(self.__user_rate.chapters)
        if self.__manga.chapters:
            self.chapters_count_spin.setMaximum(self.__manga.chapters)
        self.lib_list_combo.setCurrentIndex(self.__user_rate.status.value)

    @Slot()
    def send_user_rate(self):
        self.__user_rate.score = self.score_spin.value()
        self.__user_rate.chapters = self.chapters_count_spin.value()
        self.__user_rate.status = Nl.LibList(
            self.lib_list_combo.currentIndex(),
        )
        self.__catalog.update_user_rate(self.__user_rate)
        self.close()

    @Slot()
    def delete_user_rate(self):
        self.__catalog.delete_user_rate(self.__user_rate)
        self.close()
