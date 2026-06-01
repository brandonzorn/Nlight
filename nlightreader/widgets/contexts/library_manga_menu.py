from enum import IntEnum, unique

from qfluentwidgets import Action, FluentIcon

from nlightreader.widgets.contexts.context_menu_base import AbstractContextMenu


@unique
class LibraryMenuMode(IntEnum):
    NOT_IN_LIBRARY = 0
    IN_LIBRARY = 1
    LOCAL_ONLY = 2


class LibraryMangaMenu(AbstractContextMenu):
    def __init__(self) -> None:
        super().__init__()
        self.add_to_lib = Action(
            FluentIcon.ADD_TO,
            self.tr("Add to Library"),
        )
        self.remove_from_lib = Action(
            FluentIcon.REMOVE_FROM,
            self.tr("Remove from library"),
        )
        self.open_in_browser = Action(
            FluentIcon.LINK,
            self.tr("Open in browser"),
        )
        self.remove_files = Action(
            FluentIcon.DELETE,
            self.tr("Clear local files"),
        )
        self.open_local_files = Action(
            FluentIcon.FOLDER,
            self.tr("Open local files"),
        )

        self._actions_map = {
            LibraryMenuMode.NOT_IN_LIBRARY: [
                self.open_in_browser,
                self.add_to_lib,
                self.open_local_files,
                self.remove_files,
            ],
            LibraryMenuMode.IN_LIBRARY: [
                self.open_in_browser,
                self.remove_from_lib,
                self.open_local_files,
                self.remove_files,
            ],
            LibraryMenuMode.LOCAL_ONLY: [
                self.open_in_browser,
                self.open_local_files,
                self.remove_files,
            ],
        }

    def set_mode(self, mode: LibraryMenuMode) -> None:
        return super().set_mode(mode)


__all__ = [
    "LibraryMangaMenu",
    "LibraryMenuMode",
]
