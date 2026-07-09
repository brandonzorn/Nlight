from collections import defaultdict

from PySide6.QtCore import QPoint, Signal, Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.history import Ui_HistoryPage
from nlightreader.items import HistoryNote
from nlightreader.models import Manga
from nlightreader.utils.database import Database
from nlightreader.widgets.contexts import HistoryMenuMode, HistoryNoteMenu
from nlightreader.widgets.items import (
    HistoryNoteTreeItem,
    MangaTreeItem,
)


class HistoryPage(QWidget):
    manga_open = Signal(Manga)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_HistoryPage()
        self.ui.setupUi(self)

        self.ui.delete_btn.setIcon(FluentIcon.DELETE)
        self.ui.delete_btn.clicked.connect(self.delete_note)

        self.ui.itemsTree.doubleClicked.connect(self.open_info)
        self.ui.itemsTree.customContextMenuRequested.connect(
            self.on_context_menu,
        )

        self._db: Database = Database()

        self._notes: list[HistoryNote] = []
        self._sorted_notes: dict[Manga, list[HistoryNote]] = {}

    def on_context_menu(self, pos: QPoint) -> None:
        selected_item = self.ui.itemsTree.itemAt(pos)
        if not isinstance(selected_item, HistoryNoteTreeItem):
            return

        menu = HistoryNoteMenu()
        menu.set_as_read.triggered.connect(
            lambda: self._mark_chapter_as_read(selected_item),
        )
        menu.remove_all.triggered.connect(
            lambda: self._remove_manga_history(selected_item),
        )

        if not self._db.get_complete_status(selected_item.note.chapter):
            menu.set_mode(HistoryMenuMode.UNREAD)
        else:
            menu.set_mode(HistoryMenuMode.READ)

        menu.exec(self.ui.itemsTree.mapToGlobal(pos))

    def setup(self) -> None:
        self.ui.itemsTree.verticalScrollBar().setValue(0)
        self.get_content()

    @Slot()
    def open_info(self) -> None:
        selected_item = self.ui.itemsTree.currentItem()
        if not isinstance(selected_item, HistoryNoteTreeItem):
            return
        self.manga_open.emit(selected_item.note.manga)

    @Slot()
    def delete_note(self) -> None:
        selected_item = self.ui.itemsTree.currentItem()
        if not isinstance(selected_item, HistoryNoteTreeItem):
            return
        self._db.del_history_note(selected_item.note.chapter)
        selected_item.parent().removeChild(selected_item)
        self.update_content()

    def update_content(self) -> None:
        self.ui.itemsTree.clear()
        notes = self._db.get_history_notes()
        grouped_notes = defaultdict(list)
        for note in notes:
            grouped_notes[note.manga].append(note)

        for manga, manga_notes in grouped_notes.items():
            manga_item = MangaTreeItem(manga)
            self.ui.itemsTree.addTopLevelItem(manga_item)
            for note in manga_notes:
                chapter_item = HistoryNoteTreeItem(note)
                manga_item.addChild(chapter_item)

    def get_content(self) -> None:
        self.update_content()

    def _mark_chapter_as_read(
        self,
        selected_item: HistoryNoteTreeItem,
    ) -> None:
        selected_item.note.is_completed = True
        self._db.add_history_note(selected_item.note)
        selected_item.update_icon()

    def _remove_manga_history(
        self,
        selected_item: HistoryNoteTreeItem,
    ) -> None:
        self._db.del_history_notes(selected_item.note.manga)
        selected_item.delete_parent()


__all__ = ["HistoryPage"]
