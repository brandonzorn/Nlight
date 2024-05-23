from qfluentwidgets import RoundMenu, FluentIcon, Action

from nlightreader.utils import translate


class LibraryMangaMenu(RoundMenu):
    def __init__(self):
        super().__init__()
        self.add_to_lib = Action(
            FluentIcon.ADD_TO,
            translate("Menu", "Add to Library"),
        )
        self.remove_from_lib = Action(
            FluentIcon.REMOVE_FROM,
            translate("Menu", "Remove from library"),
        )
        self.open_in_browser = Action(
            FluentIcon.LINK,
            translate("Menu", "Open in browser"),
        )
        self.remove_files = Action(
            FluentIcon.DELETE,
            translate("Menu", "Clear local files"),
        )
        self.open_local_files = Action(
            FluentIcon.FOLDER,
            translate("Menu", "Open local files"),
        )

    def set_mode(self, mode: int):
        """
        Sets the mode of this object and adds the appropriate actions based on the mode.

        Args:
            mode: The mode to set. Valid values are 0, 1, 2.

        Raises:
            ValueError: If an invalid mode is provided.
        """
        actions = {
            0: [
                self.open_in_browser,
                self.add_to_lib,
                self.open_local_files,
                self.remove_files,
            ],
            1: [
                self.open_in_browser,
                self.remove_from_lib,
                self.open_local_files,
                self.remove_files,
            ],
            2: [
                self.open_in_browser,
                self.open_local_files,
                self.remove_files,
            ],
        }
        if mode not in actions:
            raise ValueError("Invalid mode: must be 0, 1 or 2")
        self.addActions(actions.get(mode, []))
