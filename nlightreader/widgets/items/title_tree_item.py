from typing import TypeVar

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidgetItem, QTreeWidgetItem

from nlightreader.models.base_model import NamedBaseModel

T = TypeVar("T", bound=NamedBaseModel)


class ModelListItem[T: NamedBaseModel](QListWidgetItem):
    def __init__(self, model: T, icon: QIcon | None = None) -> None:
        super().__init__(model.get_name())
        if icon is not None:
            self.setIcon(icon)
        self.model: T = model


class ModelTreeItem[T: NamedBaseModel](QTreeWidgetItem):
    def __init__(self, model: T, icon: QIcon | None = None) -> None:
        super().__init__([model.get_name()])
        if icon is not None:
            self.setIcon(0, icon)
        self.model: T = model


__all__ = [
    "ModelListItem",
    "ModelTreeItem",
]
