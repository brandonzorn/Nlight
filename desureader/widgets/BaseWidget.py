from PySide6.QtWidgets import QWidget


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.get_content()

    def get_content(self):
        pass

    def get_current_manga(self):
        print("// Method called from BaseClass")
