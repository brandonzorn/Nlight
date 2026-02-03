from enum import IntEnum, unique

from qfluentwidgets import Action, FluentIcon, RoundMenu


@unique
class ReadMarkMode(IntEnum):
    SET_AS_READ = 0
    REMOVE_ONLY = 1
    ALL = 2


class ReadMarkMenu(RoundMenu):
    def __init__(self):
        super().__init__()
        self.set_as_read = Action(
            FluentIcon.ACCEPT_MEDIUM,
            self.tr("Mark as read"),
        )
        self.set_as_read_all = Action(
            FluentIcon.COMPLETED,
            self.tr("Mark as read all previous"),
        )
        self.remove_read_state = Action(
            FluentIcon.REMOVE,
            self.tr("Remove read mark"),
        )

    def set_mode(self, mode: ReadMarkMode):
        """
        Sets the mode of this object and
        adds the appropriate actions based on the mode.

        Args:
            mode (ReadMarkMode): The mode to set.

        Raises:
            ValueError: If an invalid mode is provided.
        """
        actions = {
            ReadMarkMode.SET_AS_READ: [
                self.set_as_read,
                self.set_as_read_all,
            ],
            ReadMarkMode.REMOVE_ONLY: [
                self.remove_read_state,
                self.set_as_read_all,
            ],
            ReadMarkMode.ALL: [
                self.set_as_read,
                self.remove_read_state,
                self.set_as_read_all,
            ],
        }
        if mode not in actions:
            raise ValueError("Invalid mode: must be a ReadMarkMode")
        self.addActions(actions.get(mode, []))


__all__ = [
    "ReadMarkMenu",
    "ReadMarkMode",
]
