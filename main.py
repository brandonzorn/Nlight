import sys
import time
from pathlib import Path

import darkdetect
import platformdirs
from PySide6.QtCore import Qt, QTranslator, QLocale, QThreadPool
from PySide6.QtGui import QIcon, QPalette
from PySide6.QtWidgets import QApplication

from nlightreader import ParentWindow
from nlightreader.consts import APP_VERSION, APP_NAME, Icons
from nlightreader.utils import get_locale, Thread


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationDisplayName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setWindowIcon(QIcon(Icons.App))

        self.translator = QTranslator()

        self.load_translator()

    def load_translator(self):
        self.translator.load(get_locale(QLocale().language()))
        self.installTranslator(self.translator)

    def get_accent_color(self):
        return self.palette().color(QPalette.ColorRole.Highlight)


class MainWindow(ParentWindow):
    def __init__(self):
        super().__init__()
        self.set_min_size_by_screen()
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(Icons.App))
        self._theme_updater = Thread(target=self.theme_listener, callback=self.update_style)
        # self._theme_updater.start()
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


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QThreadPool.globalInstance().setMaxThreadCount(32)
    app = App(sys.argv)
    Path(f"{platformdirs.user_data_dir()}/{APP_NAME}").mkdir(parents=True, exist_ok=True)
    window = MainWindow()
    sys.exit(app.exec())
