from typing import override

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QFormLayout, QWidget
from qfluentwidgets import (
    BodyLabel,
    ComboBox,
    MessageBoxBase,
    PushButton,
    SpinBox,
    SubtitleLabel,
)

from nlightreader.core.enums import LIB_LISTS, LibList
from nlightreader.items import UserRate
from nlightreader.models import Manga
from nlightreader.utils.catalog_manager import (
    get_catalog_by_id,
    get_lib_catalog,
)
from nlightreader.utils.translator import translate


class RateDialog(MessageBoxBase):
    def __init__(self, manga: Manga, parent: QWidget) -> None:
        super().__init__(parent)
        self._parent = parent

        self._manga = manga
        self._catalog = get_lib_catalog(
            type(get_catalog_by_id(self._manga.catalog_id)),
        )
        self._user_rate = self._fetch_user_rate()

        self._setup_ui()
        self._setup_connections()
        self._display_user_rate()

    def _setup_ui(self) -> None:
        self.title_label = SubtitleLabel(self.tr("Change rating"), parent=self)

        self.form_frame = QWidget()
        self.form_layout = QFormLayout(self.form_frame)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(12)

        self.chapters_label = BodyLabel(
            self.tr("Chapters read"),
            parent=self.form_frame,
        )
        self.chapters_count_spin = SpinBox(parent=self.form_frame)
        self.chapters_count_spin.setMaximum(999)
        self.form_layout.addRow(self.chapters_label, self.chapters_count_spin)

        self.score_label = BodyLabel(
            self.tr("Rating"),
            parent=self.form_frame,
        )
        self.score_spin = SpinBox(parent=self.form_frame)
        self.score_spin.setMaximum(10)
        self.form_layout.addRow(self.score_label, self.score_spin)

        self.lib_list_label = BodyLabel(
            self.tr("List"),
            parent=self.form_frame,
        )
        self.lib_list_combo = ComboBox(parent=self.form_frame)
        self.lib_list_combo.addItems(
            [translate("Form", i.capitalize()) for i in LIB_LISTS],
        )
        self.form_layout.addRow(self.lib_list_label, self.lib_list_combo)

        self.delete_rate_button = PushButton()
        self.delete_rate_button.setText(self.tr("Delete"))
        self.buttonLayout.addWidget(
            self.delete_rate_button,
            1,
            Qt.AlignmentFlag.AlignVCenter,
        )

        self.viewLayout.addWidget(self.title_label)
        self.viewLayout.addWidget(self.form_frame)

    def _setup_connections(self) -> None:
        self.delete_rate_button.clicked.connect(self._delete_user_rate)
        self.accepted.connect(self._send_user_rate)
        self.rejected.connect(self.close)

    @override
    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.deleteLater()

    def _fetch_user_rate(self) -> UserRate | None:
        if not self._catalog.check_user_rate(self._manga):
            self._catalog.create_user_rate(self._manga)
        return self._catalog.get_user_rate(self._manga)

    def _display_user_rate(self) -> None:
        if self._user_rate is None:
            return
        self.score_spin.setValue(self._user_rate.score)
        self.chapters_count_spin.setValue(self._user_rate.chapters)
        if self._manga.chapters_number:
            self.chapters_count_spin.setMaximum(self._manga.chapters_number)
        self.lib_list_combo.setCurrentIndex(self._user_rate.status.value)

    @Slot()
    def _send_user_rate(self) -> None:
        if self._user_rate is None:
            return
        self._user_rate.score = self.score_spin.value()
        self._user_rate.chapters = self.chapters_count_spin.value()
        self._user_rate.status = LibList(
            self.lib_list_combo.currentIndex(),
        )
        self._catalog.update_user_rate(self._user_rate)
        self.close()

    @Slot()
    def _delete_user_rate(self) -> None:
        if self._user_rate is None:
            return
        self._catalog.delete_user_rate(self._user_rate)
        self.close()


__all__ = ["RateDialog"]
