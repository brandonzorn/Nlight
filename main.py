import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from app_windows.main_window import MainWindow
from const.icons import app_icon_path
from file_manager import init_app_paths


class App(MainWindow):
    def __init__(self):
        super().__init__(None)
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        self.setWindowTitle('Desu')
        self.setWindowIcon(QIcon(app_icon_path))
        self.show()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    app = QApplication(sys.argv)
    app_paths = ['Desu']
    init_app_paths(app_paths)
    a = App()
    sys.exit(app.exec())
