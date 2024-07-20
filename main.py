import logging
import sys
import time
from http.server import HTTPServer
from pathlib import Path
from threading import Thread as PyThread

import darkdetect
import platformdirs
from PySide6.QtCore import QLocale, Qt, QThreadPool, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import InfoBar, setTheme, Theme

from data import resource
from nlightreader import ParentWindow
from nlightreader.consts.app import APP_BRANCH, APP_NAME, APP_VERSION
from nlightreader.consts.files import Icons
from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.consts.urls import GITHUB_REPO
from nlightreader.utils import get_html, get_locale, Thread, translate
from nlightreader.utils.kodik_server import KodikHTTPRequestHandler


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationDisplayName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setWindowIcon(QIcon(Icons.App))

        self.translator = QTranslator()

        self.load_translator()
        self.update_style()

    def load_translator(self):
        self.translator.load(get_locale(QLocale().language()))
        self.installTranslator(self.translator)

    def update_style(self):
        setTheme(Theme.DARK if darkdetect.isDark() else Theme.LIGHT)


class MainWindow(ParentWindow):
    def __init__(self):
        super().__init__()
        self.set_min_size_by_screen()
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(Icons.App))
        self._theme_updater = Thread(
            target=self.theme_listener,
            callback=self.update_style,
        )
        self._update_checker = Thread(
            target=self.check_for_updates,
            callback=self.show_update_info,
        )
        self._theme_updater.start()
        self._update_checker.start()

    def check_for_updates(self):
        response = get_html(
            f"{GITHUB_REPO}/releases",
            params={"per_page": 2},
            content_type="json",
        )
        if not response:
            return
        for release in response:
            version = release["tag_name"]
            if APP_BRANCH in version:
                return version

    def show_update_info(self, result):
        info_bar_title = translate(
            "Message",
            "Check for updates.",
        )
        info_bar_duration = 3500
        if result is None:
            InfoBar.error(
                title=info_bar_title,
                content=translate(
                    "Message",
                    "Error checking for updates.",
                ),
                duration=info_bar_duration,
                parent=self,
            )

        elif result != APP_VERSION:
            InfoBar.info(
                title=info_bar_title,
                content=translate(
                    "Message",
                    "New version {result} is available! "
                    "You are currently on version {APP_VERSION}.",
                ).format(result=result, APP_VERSION=APP_VERSION),
                duration=info_bar_duration,
                parent=self,
            )

    @staticmethod
    def theme_listener():
        theme = darkdetect.theme()
        while darkdetect.theme() == theme:
            time.sleep(1)

    def update_style(self):
        app.update_style()
        self._theme_updater.start()

    def closeEvent(self, event):
        super().closeEvent(event)
        self._theme_updater.terminate()
        self._theme_updater.wait()
        app.closeAllWindows()


if __name__ == "__main__":
    if "debug" in sys.argv:
        logging.basicConfig(
            level=logging.WARNING,
            filename="latest.log",
            filemode="w",
        )

    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor,
    )
    QApplication.setStyle("Fusion")
    QThreadPool.globalInstance().setMaxThreadCount(32)
    app = App(sys.argv)

    APP_DATA_PATH.mkdir(parents=True, exist_ok=True)

    httpd = HTTPServer(("localhost", 8000), KodikHTTPRequestHandler)
    PyThread(target=httpd.serve_forever, daemon=True).start()

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
