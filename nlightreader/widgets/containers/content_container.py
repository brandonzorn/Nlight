from enum import Enum, unique

from PySide6.QtWidgets import QWidget
from qfluentwidgets import (
    FluentIcon,
    IndeterminateProgressRing,
    TransparentPushButton,
)

from nlightreader.utils.translator import translate


@unique
class ContentContainerState(Enum):
    EMPTY = 0
    SHOW_CONTENT = 1
    FETCH_CONTENT = 2
    NO_CONTENT = 3
    FETCH_ERROR = 4


class AbstractContentContainer:
    def __init__(self):
        self._progress_ring = IndeterminateProgressRing()
        self._progress_ring.setVisible(False)

        self._fetch_error_widget = TransparentPushButton(
            FluentIcon.CLOUD,
            translate("Message", "No connection"),
        )
        self._fetch_error_widget.setEnabled(False)
        self._fetch_error_widget.setVisible(False)

        self._no_content_error_widget = TransparentPushButton(
            FluentIcon.CLOUD,
            translate("Message", "Nothing found"),
        )
        self._no_content_error_widget.setEnabled(False)
        self._no_content_error_widget.setVisible(False)

        self._content_widget = None

        self._state = ContentContainerState.EMPTY

    def install(self, parent):
        self.get_content_widget().layout().addWidget(
            self._no_content_error_widget,
        )
        self.get_content_widget().layout().addWidget(
            self._fetch_error_widget,
        )
        self.get_content_widget().layout().addWidget(
            self._progress_ring,
        )
        parent.addWidget(self)

    def _reset_area(self) -> None:
        raise NotImplementedError

    def set_state(self, state: ContentContainerState):
        state_objects = (
            self._progress_ring,
            self._no_content_error_widget,
            self._fetch_error_widget,
            self._content_widget,
        )
        if not isinstance(state, ContentContainerState):
            raise TypeError(
                f"state must be ContentContainerState got {type(state)}",
            )

        self._state = state

        state_obj = None
        if state == ContentContainerState.EMPTY:
            state_obj = None

        elif state == ContentContainerState.SHOW_CONTENT:
            state_obj = self._content_widget

        elif state == ContentContainerState.FETCH_CONTENT:
            state_obj = self._progress_ring

        elif state == ContentContainerState.NO_CONTENT:
            state_obj = self._no_content_error_widget

        elif state == ContentContainerState.FETCH_ERROR:
            state_obj = self._fetch_error_widget

        [
            obj.setVisible(
                obj == state_obj,
            )
            for obj in state_objects
            if obj is not None
        ]

    def set_content(self, content) -> None:
        raise NotImplementedError

    def get_content_widget(self) -> QWidget:
        raise NotImplementedError


__all__ = [
    "AbstractContentContainer",
    "ContentContainerState",
]
