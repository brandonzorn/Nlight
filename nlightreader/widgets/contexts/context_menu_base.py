from collections.abc import Sequence
from enum import IntEnum

from qfluentwidgets import Action, RoundMenu


class AbstractContextMenu[TMode: IntEnum](RoundMenu):
    def __init__(self) -> None:
        super().__init__()
        self._actions_map: dict[TMode, Sequence[Action]] = {}

    def set_mode(self, mode: TMode) -> None:
        self.clear()

        if mode not in self._actions_map:
            msg = (
                f"Available values: "
                f"{list(self._actions_map.keys())}, got {mode}"
            )
            raise ValueError(msg)

        current_actions = self._actions_map[mode]
        self.addActions(current_actions)


__all__ = ["AbstractContextMenu"]
