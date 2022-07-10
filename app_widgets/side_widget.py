from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from const.icons import main_icon_path, library_icon_path, shikimori_icon_path, history_icon_path, settings_icon_path
from forms.sideMenu import Ui_Form


class SideMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_mylist.setIcon(QIcon(library_icon_path))
        self.ui.btn_main.setIcon(QIcon(main_icon_path))
        self.ui.btn_shikimori.setIcon(QIcon(shikimori_icon_path))
        self.ui.btn_history.setIcon(QIcon(history_icon_path))
        self.ui.btn_settings.setIcon(QIcon(settings_icon_path))
