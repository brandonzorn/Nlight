from PySide6.QtWidgets import QWidget


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.get_content()

    def update_content(self):
        pass

    def get_content(self):
        pass
