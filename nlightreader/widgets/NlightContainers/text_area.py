from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from data.ui.containers.text_area import Ui_Form


class TextArea(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.size_slider.valueChanged.connect(self.update_text_size)

    def install(self, parent):
        parent.addWidget(self)

    @Slot()
    def update_text_size(self):
        font = self.ui.text_browser.font()
        font.setPointSize(self.ui.size_slider.value())
        self.ui.text_browser.setFont(font)

    def reset_reader_area(self):
        self.ui.text_browser.clear()

    def set_html(self, html_text: str):
        self.reset_reader_area()
        self.ui.text_browser.setHtml(html_text)
