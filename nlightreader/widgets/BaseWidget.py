from PySide6.QtWidgets import QWidget


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def get_current_manga(self):
        pass
