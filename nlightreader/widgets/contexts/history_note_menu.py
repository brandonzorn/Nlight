from enum import IntEnum, unique

from qfluentwidgets import Action, FluentIcon

from nlightreader.widgets.contexts.context_menu_base import AbstractContextMenu


@unique
class HistoryMenuMode(IntEnum):
    UNREAD = 0
    READ = 1


class HistoryNoteMenu(AbstractContextMenu[HistoryMenuMode]):
    def __init__(self) -> None:
        super().__init__()
        self.set_as_read = Action(
            FluentIcon.ACCEPT_MEDIUM,
            self.tr("Mark as read"),
        )
        self.remove = Action(
            FluentIcon.REMOVE,
            self.tr("Remove"),
        )
        self.remove_all = Action(
            FluentIcon.DELETE,
            self.tr("Remove all"),
        )

        self._actions_map = {
            HistoryMenuMode.UNREAD: [
                self.remove,
                self.remove_all,
                self.set_as_read,
            ],
            HistoryMenuMode.READ: [self.remove, self.remove_all],
        }


__all__ = [
    "HistoryMenuMode",
    "HistoryNoteMenu",
]
