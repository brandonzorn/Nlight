from PySide6.QtWidgets import QWidget


class AbstractContentContainer:
    def install(self, parent):
        parent.addWidget(self)

    def _reset_area(self) -> None:
        raise NotImplementedError

    def set_content(self, content) -> None:
        raise NotImplementedError

    def get_content_widget(self) -> QWidget:
        raise NotImplementedError
