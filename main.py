import os
import sys
import time
from enum import Enum

import darkdetect
import platformdirs
from PySide6.QtCore import Qt, QTranslator, QLocale, QThreadPool
from PySide6.QtGui import QIcon, QPalette
from PySide6.QtWidgets import QApplication
from qfluentwidgets import StyleSheetBase, Theme, qconfig

from nlightreader import ParentWindow
from nlightreader.consts import APP_VERSION, APP_NAME, Icons
from nlightreader.utils import get_locale, get_ui_style, Thread


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationDisplayName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setWindowIcon(QIcon(Icons.App))

        self.translator = QTranslator()

        self.load_translator()
        # self.update_style()

    def load_translator(self):
        self.translator.load(get_locale(QLocale().language()))
        self.installTranslator(self.translator)

    def get_accent_color(self):
        return self.palette().color(QPalette.ColorRole.Highlight)

    def update_style(self):
        accent_color = self.get_accent_color()
        self.setStyleSheet(get_ui_style(darkdetect.theme(), accent_color.name()))


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    MAIN_WINDOW = "main_window"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"app/resource/qss/{theme.value.lower()}/{self.value}.qss"


class MainWindow(ParentWindow):
    def __init__(self):
        super().__init__()
        self.set_min_size_by_screen()
        self.setWindowTitle(APP_NAME)
        StyleSheet.MAIN_WINDOW.apply(self)
        self._theme_updater = Thread(target=self.theme_listener, callback=self.update_style)
        self._theme_updater.start()
        self.show()

    @staticmethod
    def theme_listener():
        theme = darkdetect.theme()
        accent_color = app.get_accent_color()
        while darkdetect.theme() == theme and accent_color == app.get_accent_color():
            time.sleep(1)

    def update_style(self):
        app.update_style()
        self._theme_updater.start()

    def closeEvent(self, event):
        self._theme_updater.terminate()
        self._theme_updater.wait()
        app.closeAllWindows()
        event.accept()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    # QApplication.setStyle('Fusion')
    QThreadPool.globalInstance().setMaxThreadCount(32)
    app = App(sys.argv)
    os.makedirs(f'{platformdirs.user_data_dir()}/{APP_NAME}', exist_ok=True)
    window = MainWindow()
    sys.exit(app.exec())
