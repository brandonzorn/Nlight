from collections import defaultdict
from typing import override

from PySide6.QtCore import QPoint, Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.history import Ui_HistoryPage
from nlightreader.database import Database
from nlightreader.widgets.contexts import HistoryMenuMode, HistoryNoteMenu
from nlightreader.widgets.items import HistoryTreeItem, MangaTreeItem
from nlightreader.widgets.pages.base_page import BasePage


class HistoryPage(BasePage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_HistoryPage()
        self.ui.setupUi(self)

        self.ui.delete_btn.setIcon(FluentIcon.DELETE)
        self.ui.delete_btn.clicked.connect(self.delete_note)

        self.ui.itemsTree.doubleClicked.connect(self.open_info)
        self.ui.itemsTree.customContextMenuRequested.connect(
            self._on_context_menu,
        )

        self._db = Database()

    @override
    def setup(self) -> None:
        self.ui.itemsTree.verticalScrollBar().setValue(0)
        super().setup()

    @override
    def _get_content(self) -> None:
        self._update_content()

    @Slot()
    def open_info(self) -> None:
        selected_item = self.ui.itemsTree.currentItem()
        if not isinstance(selected_item, HistoryTreeItem):
            return
        self.manga_open.emit(selected_item.note.manga)

    @Slot()
    def delete_note(self) -> None:
        selected_item = self.ui.itemsTree.currentItem()
        if not isinstance(selected_item, HistoryTreeItem):
            return
        self._db.history.delete_by_chapter(selected_item.note.chapter.id)
        selected_item.parent().removeChild(selected_item)
        self._update_content()

    @override
    def _update_content(self) -> None:
        self.ui.itemsTree.clear()
        notes = self._db.history.get_all()
        grouped_notes = defaultdict(list)
        for note in notes:
            grouped_notes[note.manga].append(note)

        for manga, manga_notes in grouped_notes.items():
            manga_item = MangaTreeItem(manga)
            self.ui.itemsTree.addTopLevelItem(manga_item)
            for note in manga_notes:
                chapter_item = HistoryTreeItem(note)
                manga_item.addChild(chapter_item)

    def _mark_chapter_as_read(self, selected_item: HistoryTreeItem) -> None:
        selected_item.note.is_completed = True
        self._db.history.save(selected_item.note)
        selected_item.update_icon()

    def _remove_manga_history(self, selected_item: HistoryTreeItem) -> None:
        self._db.history.delete_by_manga(selected_item.note.manga.id)
        selected_item.delete_parent()

    def _on_context_menu(self, position: QPoint) -> None:
        selected_item = self.ui.itemsTree.itemAt(position)
        if not isinstance(selected_item, HistoryTreeItem):
            return

        menu = HistoryNoteMenu()
        menu.set_as_read.triggered.connect(
            lambda: self._mark_chapter_as_read(selected_item),
        )
        menu.remove_all.triggered.connect(
            lambda: self._remove_manga_history(selected_item),
        )

        if self._db.history.is_completed(selected_item.note.chapter.id):
            menu.set_mode(HistoryMenuMode.READ)
        else:
            menu.set_mode(HistoryMenuMode.UNREAD)

        menu.exec(self.ui.itemsTree.mapToGlobal(position))


__all__ = ["HistoryPage"]
