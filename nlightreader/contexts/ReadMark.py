from qfluentwidgets import Action, FluentIcon, RoundMenu

from nlightreader.utils import translate


class ReadMarkMenu(RoundMenu):
    def __init__(self):
        super().__init__()
        self.set_as_read = Action(
            FluentIcon.ACCEPT_MEDIUM,
            translate("Menu", "Mark as read"),
        )
        self.set_as_read_all = Action(
            FluentIcon.COMPLETED,
            translate("Menu", "Mark as read all previous"),
        )
        self.remove_read_state = Action(
            FluentIcon.REMOVE,
            translate("Menu", "Remove read mark"),
        )

    def set_mode(self, mode: int):
        """
        Sets the mode of this object and
        adds the appropriate actions based on the mode.

        Args:
            mode (int): The mode to set. Valid values are 0, 1, 2.

        Raises:
            ValueError: If an invalid mode is provided.
        """
        actions = {
            0: [self.set_as_read, self.set_as_read_all],
            1: [self.remove_read_state, self.set_as_read_all],
            2: [
                self.set_as_read,
                self.remove_read_state,
                self.set_as_read_all,
            ],
        }
        if mode not in actions:
            raise ValueError("Invalid mode: must be 0, 1 or 2")
        self.addActions(actions.get(mode, []))
