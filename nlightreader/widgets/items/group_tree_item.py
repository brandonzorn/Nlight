from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTreeWidgetItem


class GroupTreeItem(QTreeWidgetItem):
    def __init__(self, *args: str, icon: QIcon | None = None) -> None:
        super().__init__(args)
        if icon is not None:
            self.setIcon(0, icon)
        self.setFlags(self.flags() & ~Qt.ItemFlag.ItemIsSelectable)


__all__ = ["GroupTreeItem"]
