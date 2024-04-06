from PySide6.QtWidgets import QWidget


class AbstractContentContainer:
    def install(self, parent):
        parent.addWidget(self)

    def get_content_widget(self) -> QWidget:
        raise NotImplementedError

    def set_content(self, content):
        raise NotImplementedError
