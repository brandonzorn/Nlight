from qfluentwidgets import Action, FluentIcon, RoundMenu


class HistoryNoteMenu(RoundMenu):
    def __init__(self) -> None:
        super().__init__()
        self.set_as_read = Action(
            FluentIcon.ACCEPT_MEDIUM,
            self.tr("Mark as read"),
        )
        self.remove_all = Action(
            FluentIcon.REMOVE,
            self.tr("Remove all"),
        )

    def set_mode(self, mode: int) -> None:
        """
        Sets the mode of this object and
        adds the appropriate actions based on the mode.

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
            msg = "Invalid mode: must be 0 or 1"
            raise ValueError(msg)
        self.addActions(actions[mode])


__all__ = [
    "HistoryNoteMenu",
]
