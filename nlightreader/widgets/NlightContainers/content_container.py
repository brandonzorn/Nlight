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
    empty = 0
    show_content = 1
    fetch_content = 2
    no_content = 3
    fetch_error = 4


class AbstractContentContainer:
    def __init__(self):
        self._progress_ring = IndeterminateProgressRing()
        self._progress_ring.setVisible(False)

        self._fetch_error_widget = TransparentPushButton(
            FluentIcon.CLOUD,
            translate("Message", "No connection")
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

        self._state = ContentContainerState.empty

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
        if state == ContentContainerState.empty:
            state_obj = None

        elif state == ContentContainerState.show_content:
            state_obj = self._content_widget

        elif state == ContentContainerState.fetch_content:
            state_obj = self._progress_ring

        elif state == ContentContainerState.no_content:
            state_obj = self._no_content_error_widget

        elif state == ContentContainerState.fetch_error:
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
