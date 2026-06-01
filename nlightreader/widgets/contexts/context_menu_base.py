from enum import Enum

from qfluentwidgets import Action, RoundMenu


class AbstractContextMenu(RoundMenu):
    def __init__(self) -> None:
        super().__init__()
        self._actions_map: dict[Enum, list[Action]] = {}

    def set_mode(self, mode: Enum) -> None:
        if not issubclass(type(mode), Enum):
            msg = f"'{mode}' is not a subclass of Enum"
            raise TypeError(msg)
        self.clear()

        if mode not in self._actions_map:
            msg = (
                f"Invalid mode: '{mode}'. "
                f"Available modes are: {list(self._actions_map.keys())}"
            )
            raise ValueError(msg)

        current_actions = self._actions_map.get(mode, [])
        self.addActions(current_actions)


__all__ = [
    "AbstractContextMenu",
]
