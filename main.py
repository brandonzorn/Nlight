import os
import sys
import time

import darkdetect
import platformdirs
from PySide6.QtCore import Qt, QTranslator, QLocale, QThreadPool
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication

from nlightreader import ParentWindow
from nlightreader.consts import APP_VERSION, APP_NAME, Icons, Fonts
from nlightreader.utils import get_locale, get_ui_style, Thread


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationDisplayName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setWindowIcon(QIcon(Icons.App))

        self.translator = QTranslator()

        self.load_font()
        self.load_translator()
        self.update_style()

    def load_translator(self):
        self.translator.load(get_locale(QLocale().language()))
        self.installTranslator(self.translator)

    def load_font(self):
        font = QFont(Fonts.SegoeUI, 9)
        self.setFont(font)

    def update_style(self):
        self.setStyleSheet(get_ui_style(darkdetect.theme()))


class MainWindow(ParentWindow):
    def __init__(self):
        super().__init__()
        self.set_min_size_by_screen()
        self.setWindowTitle(APP_NAME)
        self._theme_updater = Thread(target=self.theme_listener, callback=self.update_style)
        self._theme_updater.start()
        self.show()

    @staticmethod
    def theme_listener():
        theme = darkdetect.theme()
        while True:
            if darkdetect.theme() != theme:
                return
            time.sleep(1)

    def update_style(self):
        app.update_style()
        self._theme_updater.start()

    def closeEvent(self, event):
        self._theme_updater.terminate()
        self._theme_updater.wait()
        event.accept()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle('Fusion')
    QThreadPool.globalInstance().setMaxThreadCount(32)
    app = App(sys.argv)
    os.makedirs(f'{platformdirs.user_data_dir()}/{APP_NAME}', exist_ok=True)
    window = MainWindow()
    sys.exit(app.exec())
