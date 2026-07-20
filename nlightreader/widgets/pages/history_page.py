from collections import defaultdict
from functools import partial
from typing import override

from PySide6.QtCore import QPoint, Slot
from PySide6.QtWidgets import QTreeWidgetItem, QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.history import Ui_HistoryPage
from nlightreader.database import Database
from nlightreader.items import HistoryNote
from nlightreader.models import Manga
from nlightreader.widgets.contexts import HistoryMenuMode, HistoryNoteMenu
from nlightreader.widgets.items import HistoryTreeItem, MangaTreeItem
from nlightreader.widgets.pages.base_page import BasePage


class HistoryPage(BasePage):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_HistoryPage()
        self._setup_ui()
        self._setup_connections()

        self._db = Database()
        self._grouped_notes: dict[Manga, list[HistoryNote]] = defaultdict(list)

    @override
    def _setup_ui(self) -> None:
        self._ui.setupUi(self)
        self._ui.delete_button.setIcon(FluentIcon.DELETE)

    @override
    def _setup_connections(self) -> None:
        self._ui.delete_button.clicked.connect(self._delete_note)

        self._ui.items_tree.itemDoubleClicked.connect(self._open_info)
        self._ui.items_tree.customContextMenuRequested.connect(
            self._on_context_menu,
        )

    @override
    def setup(self) -> None:
        self._ui.items_tree.verticalScrollBar().setValue(0)
        super().setup()

    @override
    def _get_content(self) -> None:
        self._grouped_notes.clear()
        notes = self._db.history.get_all()
        for note in notes:
            self._grouped_notes[note.manga].append(note)
        self._update_content()

    @Slot(QTreeWidgetItem, int)
    def _open_info(self, item: QTreeWidgetItem, _: int) -> None:
        if not isinstance(item, HistoryTreeItem):
            return
        self.manga_open.emit(item.note.manga)

    @Slot()
    def _delete_note(self) -> None:
        selected_item = self._ui.items_tree.currentItem()
        if not isinstance(selected_item, HistoryTreeItem):
            return
        self._db.history.delete_by_chapter(selected_item.note.chapter.id)
        parent = selected_item.parent()
        parent.removeChild(selected_item)
        if parent.childCount() == 0:
            i = self._ui.items_tree.indexOfTopLevelItem(parent)
            self._ui.items_tree.takeTopLevelItem(i)

    @override
    def _update_content(self) -> None:
        self._ui.items_tree.clear()

        for manga, manga_notes in self._grouped_notes.items():
            manga_item = MangaTreeItem(manga)
            children = [HistoryTreeItem(note) for note in manga_notes]
            manga_item.addChildren(children)
            self._ui.items_tree.addTopLevelItem(manga_item)

    def _mark_chapter_as_read(self, selected_item: HistoryTreeItem) -> None:
        if not selected_item.note.is_completed:
            selected_item.note.is_completed = True
            self._db.history.save(selected_item.note)
        selected_item.update_icon()

    def _remove_manga_history(self, selected_item: HistoryTreeItem) -> None:
        self._db.history.delete_by_manga(selected_item.note.manga.id)
        selected_item.delete_parent()

    def _on_context_menu(self, position: QPoint) -> None:
        selected_item = self._ui.items_tree.itemAt(position)
        if not isinstance(selected_item, HistoryTreeItem):
            return

        menu = HistoryNoteMenu()
        menu.set_as_read.triggered.connect(
            partial(self._mark_chapter_as_read, selected_item),
        )
        menu.remove_all.triggered.connect(
            partial(self._remove_manga_history, selected_item),
        )

        if selected_item.note.is_completed:
            menu.set_mode(HistoryMenuMode.READ)
        else:
            menu.set_mode(HistoryMenuMode.UNREAD)

        menu.exec(self._ui.items_tree.mapToGlobal(position))


__all__ = ["HistoryPage"]
