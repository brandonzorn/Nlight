from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QTreeWidgetItem, QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.history import Ui_Form
from nlightreader.consts.colors import ItemsIcons
from nlightreader.items import HistoryNote
from nlightreader.models import Manga
from nlightreader.utils.database import Database
from nlightreader.widgets.contexts import HistoryNoteMenu


class HistoryPage(QWidget):
    manga_open = Signal(Manga)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.delete_btn.setIcon(FluentIcon.DELETE)

        self.setObjectName("FormHistory")

        self.ui.items_tree.customContextMenuRequested.connect(
            self.on_context_menu,
        )
        self.db: Database = Database()
        self.ui.delete_btn.clicked.connect(self.delete_note)
        self.ui.items_tree.doubleClicked.connect(self.open_info)
        self.notes: list[HistoryNote] = []
        self.sorted_notes = {}

    def on_context_menu(self, pos):
        def set_as_read():
            self.db.add_history_note(
                HistoryNote(
                    selected_note.chapter,
                    selected_note.manga,
                    True,
                ),
            )
            selected_item.setIcon(0, ItemsIcons.READ)

        def remove_all():
            self.db.del_history_notes(selected_manga)
            self.get_content()

        menu = HistoryNoteMenu()
        selected_item = self.ui.items_tree.itemAt(pos)
        if not selected_item:
            return

        selected_note = self._get_selected_note()
        selected_manga = self._get_selected_manga()

        if selected_item.parent() and not self.db.get_complete_status(
            selected_note.chapter,
        ):
            menu.set_mode(0)
        else:
            menu.set_mode(1)

        menu.set_as_read.triggered.connect(set_as_read)
        menu.remove_all.triggered.connect(remove_all)
        menu.exec(self.ui.items_tree.mapToGlobal(pos))

    def setup(self):
        self.get_content()

    @Slot()
    def open_info(self):
        selected_item = self.ui.items_tree.currentItem()
        if selected_item.parent():
            self.manga_open.emit(self._get_selected_manga())

    def sort_notes(self):
        self.sorted_notes.clear()
        for note in self.notes:
            if note.manga in self.sorted_notes:
                self.sorted_notes[note.manga].append(note)
            else:
                self.sorted_notes.update({note.manga: [note]})

    def update_content(self):
        self.ui.items_tree.clear()
        self.notes: list[HistoryNote] = self.db.get_history_notes()
        self.sort_notes()
        for manga in self.sorted_notes:
            top_item = QTreeWidgetItem([manga.get_name()])
            self.ui.items_tree.addTopLevelItem(top_item)
            for note in self.sorted_notes[manga]:
                ch_item = QTreeWidgetItem([note.chapter.get_name()])
                if note.is_completed:
                    ch_item.setIcon(0, ItemsIcons.READ.qicon())
                else:
                    ch_item.setIcon(0, ItemsIcons.UNREAD)
                top_item.addChild(ch_item)

    def _get_selected_note(self) -> HistoryNote | None:
        selected_item = self.ui.items_tree.currentItem()
        if not selected_item.parent():
            return None
        parent_index = self.ui.items_tree.indexFromItem(
            selected_item.parent(),
        ).row()
        note_index = self.ui.items_tree.indexFromItem(
            selected_item,
        ).row()
        return self.sorted_notes[
            list(self.sorted_notes.keys())[parent_index]][
            note_index
        ]

    def _get_selected_manga(self) -> Manga:
        selected_item = self.ui.items_tree.currentItem()
        if not selected_item.parent():
            index = self.ui.items_tree.indexFromItem(selected_item).row()
            return list(self.sorted_notes.keys())[index]
        return self._get_selected_note().manga

    @Slot()
    def delete_note(self):
        selected_item = self.ui.items_tree.currentItem()
        if not selected_item or not selected_item.parent():
            return
        self.db.del_history_note(self._get_selected_note().chapter)
        selected_item.parent().removeChild(selected_item)
        self.get_content()

    def get_content(self):
        self.update_content()


__all__ = [
    "HistoryPage",
]
