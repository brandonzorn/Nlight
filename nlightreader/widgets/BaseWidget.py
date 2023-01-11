from PySide6.QtWidgets import QWidget

from nlightreader.items import Manga


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def get_current_manga(self):
        return Manga.get_empty_instance()

    def update_content(self):
        pass
