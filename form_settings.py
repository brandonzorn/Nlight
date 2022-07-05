from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QStyleFactory, QApplication

from const import app_icon_path
from forms.ui_settings import Ui_Dialog


class FormSettings(QDialog):
    def __init__(self):
        super().__init__(None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.setWindowTitle('Options')
        self.setWindowIcon(QIcon(app_icon_path))
        self.ui.scale_box_2.addItems(QStyleFactory.keys())
        self.ui.scale_box_2.currentIndexChanged.connect(self.set_style)

    def set_style(self):
        QApplication.setStyle(QStyleFactory.keys()[self.ui.scale_box_2.currentIndex()])
