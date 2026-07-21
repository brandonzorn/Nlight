from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTreeWidgetItem

from nlightreader.consts.colors import ItemsIcons
from nlightreader.items import HistoryNote
from nlightreader.models import Manga


class GroupTreeItem(QTreeWidgetItem):
    def __init__(self, *args: str, icon: QIcon | None = None) -> None:
        super().__init__(args)
        if icon is not None:
            self.setIcon(0, icon)
        self.setFlags(self.flags() & ~Qt.ItemFlag.ItemIsSelectable)


class MangaTreeItem(GroupTreeItem):
    def __init__(self, manga: Manga) -> None:
        super().__init__(manga.get_name())
        self.manga = manga


class HistoryTreeItem(QTreeWidgetItem):
    def __init__(self, note: HistoryNote) -> None:
        tr = note.chapter.translator or ""
        super().__init__([f"{note.chapter.get_name()} {tr}"])
        self.note = note
        self.update_icon()

    def delete_parent(self) -> None:
        index = self.treeWidget().indexOfTopLevelItem(self.parent())
        self.treeWidget().takeTopLevelItem(index)

    def update_icon(self) -> None:
        if self.note.is_completed:
            self.setIcon(0, ItemsIcons.READ.qicon())
        else:
            self.setIcon(0, ItemsIcons.UNREAD)


__all__ = ["GroupTreeItem", "HistoryTreeItem", "MangaTreeItem"]
