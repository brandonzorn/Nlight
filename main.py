import logging
import os
import sys
import time
from http.server import HTTPServer
from threading import Thread as PyThread

import darkdetect
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import InfoBar, setTheme, Theme

from data import resource
from nlightreader import ParentWindow
from nlightreader.consts.app import APP_BRANCH, APP_NAME, APP_VERSION
from nlightreader.consts.files import Icons
from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.consts.urls import GITHUB_REPO_API
from nlightreader.utils.config import cfg
from nlightreader.utils.kodik_server import KodikHTTPRequestHandler
from nlightreader.utils.threads import Thread
from nlightreader.utils.translator import NlightTranslator, translate
from nlightreader.utils.utils import get_html


__all__ = []


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationDisplayName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setWindowIcon(QIcon(Icons.App))

        self.translator = NlightTranslator()

        self.load_translator()
        self.update_theme_mode()

    def load_translator(self):
        locale = cfg.get(cfg.language).value
        self.translator.load(locale)
        self.installTranslator(self.translator)

    @staticmethod
    def update_theme_mode():
        if (theme_mode := cfg.get(cfg.theme_mode)) == "Auto":
            setTheme(Theme.DARK if darkdetect.isDark() else Theme.LIGHT)
        else:
            setTheme(Theme.DARK if theme_mode == "Dark" else Theme.LIGHT)


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
            error_callback=lambda: self.show_update_info(None),
        )

        self.settings_interface.check_for_updates_signal.connect(
            self.start_check_for_updates_thread,
        )
        self.settings_interface.theme_changed.connect(
            app.update_theme_mode,
        )

        self._theme_updater.start()
        if cfg.get(cfg.check_updates_at_startup):
            self.start_check_for_updates_thread()

    def closeEvent(self, event, /):
        self._theme_updater.terminate()
        self._theme_updater.deleteLater()
        app.closeAllWindows()
        super().closeEvent(event)

    def start_check_for_updates_thread(self):
        self._update_checker.terminate()
        self._update_checker.wait()
        self._update_checker.start()

    def check_for_updates(self) -> str | None:
        response = get_html(
            f"{GITHUB_REPO_API}/releases",
            params={"per_page": 2},
            content_type="json",
        )
        if not response:
            return None
        latest_version = None
        for release in reversed(response):
            version = release["tag_name"]
            if APP_BRANCH in version:
                latest_version = version
        return latest_version

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
        else:
            InfoBar.success(
                title=info_bar_title,
                content=translate(
                    "Message",
                    "No updates available. You are using the latest version.",
                ),
                duration=info_bar_duration,
                parent=self,
            )

    @staticmethod
    def theme_listener():
        theme = darkdetect.theme()
        while darkdetect.theme() == theme or cfg.get(cfg.theme_mode) != "Auto":
            time.sleep(1)

    def update_style(self):
        app.update_theme_mode()
        self._theme_updater.start()


if __name__ == "__main__":
    if "debug" in sys.argv:
        logging.basicConfig(
            level=logging.WARNING,
            filename="latest.log",
            filemode="w",
        )
    QThreadPool.globalInstance().setMaxThreadCount(32)

    if cfg.get(cfg.dpi_scale) != "Auto":
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
        os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpi_scale))

    app = App(sys.argv)

    APP_DATA_PATH.mkdir(parents=True, exist_ok=True)

    if cfg.get(cfg.enable_kodik_server):
        httpd = HTTPServer(("localhost", 8000), KodikHTTPRequestHandler)
        PyThread(target=httpd.serve_forever, daemon=True).start()

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
