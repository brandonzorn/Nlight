from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QListWidgetItem

from const.colors import ItemsColors
from data.ui.history import Ui_Form
from nlightreader.contexts import HistoryNoteMenu
from nlightreader.items import HistoryNote
from nlightreader.utils import Database
from nlightreader.widgets.BaseWidget import BaseWidget


class FormHistory(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.items_list.installEventFilter(self)
        self.db: Database = Database()
        self.ui.delete_btn.clicked.connect(self.delete_note)
        self.notes: list[HistoryNote] = []

    def eventFilter(self, source, event):
        def set_as_read():
            self.db.add_history_note(selected_note.manga, selected_note.chapter, True)
            selected_item.setBackground("GREEN")

        def remove_all():
            self.db.del_history_notes(self.notes[selected_item.listWidget().indexFromItem(selected_item).row()].manga)
            self.get_content()

        if event.type() == QEvent.ContextMenu and source is self.ui.items_list:
            menu = HistoryNoteMenu()
            selected_item: QListWidgetItem = source.itemAt(event.pos())
            selected_note = self.notes[selected_item.listWidget().indexFromItem(selected_item).row()]
            if not selected_note.is_completed:
                menu.set_mode(0)
            else:
                menu.set_mode(1)
            selected_action = menu.exec(event.globalPos())
            match selected_action:
                case menu.set_as_read:
                    set_as_read()
                case menu.remove_all:
                    remove_all()
            return True
        return super().eventFilter(source, event)

    def setup(self):
        self.get_content()

    def get_current_manga(self):
        return self.notes[self.ui.items_list.currentIndex().row()].manga

    def delete_note(self):
        if self.ui.items_list.currentIndex().row() >= 0:
            self.db.del_history_note(self.notes[self.ui.items_list.currentIndex().row()].chapter)
            self.setup()

    def get_content(self):
        self.ui.items_list.clear()
        self.notes: list[HistoryNote] = self.db.get_history_notes()
        for note in self.notes:
            item = QListWidgetItem(note.get_name())
            if note.is_completed:
                item.setBackground(ItemsColors.READ)
            else:
                item.setBackground(ItemsColors.UNREAD)
            self.ui.items_list.addItem(item)
