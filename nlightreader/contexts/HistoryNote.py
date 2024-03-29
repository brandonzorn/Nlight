from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu

from nlightreader.utils import translate


class HistoryNoteMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.set_as_read = QAction(translate("Menu", "Mark as read"))
        self.remove_all = QAction(translate("Menu", "Remove all"))

    def set_mode(self, mode: int):
        """
        Sets the mode of this object and adds the appropriate actions based on the mode.

        Args:
            mode (int): The mode to set. Valid values are 0, 1.

        Raises:
            ValueError: If an invalid mode is provided.
        """
        actions = {
            0: [self.remove_all, self.set_as_read],
            1: [self.remove_all],
        }
        if mode not in actions:
            raise ValueError("Invalid mode: must be 0 or 1")
        self.addActions(actions[mode])
