import logging
import sys
import time
from pathlib import Path

import darkdetect
import platformdirs
from PySide6.QtCore import Qt, QTranslator, QLocale, QThreadPool
from PySide6.QtGui import QIcon, QPalette
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setTheme, Theme, InfoBar

from nlightreader import ParentWindow
from nlightreader.consts.app import APP_VERSION, APP_NAME
from nlightreader.consts.files import Icons
from nlightreader.consts.urls import GITHUB_REPO
from nlightreader.utils import get_locale, Thread, get_html, translate


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

    def get_accent_color(self):
        return self.palette().color(QPalette.ColorRole.Highlight)

    def update_style(self):
        setTheme(Theme.DARK if darkdetect.isDark() else Theme.LIGHT)


class MainWindow(ParentWindow):
    def __init__(self):
        super().__init__()
        self.set_min_size_by_screen()
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(Icons.App))
        self._theme_updater = Thread(target=self.theme_listener, callback=self.update_style)
        self._update_checker = Thread(target=self.check_for_updates, callback=self.show_update_info)
        self._theme_updater.start()
        self._update_checker.start()

    def check_for_updates(self):
        response = get_html(f"{GITHUB_REPO}/releases/latest", content_type="json")
        if response:
            latest_version: str = response["tag_name"]
            return latest_version

    def show_update_info(self, result):
        info_bar_title = translate("Message", "Check for updates.")
        info_bar_duration = 3500
        if result is None:
            InfoBar.error(
                title=info_bar_title,
                content=translate("Message", "Error checking for updates."),
                duration=info_bar_duration,
                parent=self,
            )

        elif result != APP_VERSION:
            InfoBar.info(
                title=info_bar_title,
                content=translate(
                    "Message",
                    "New version {result} is available! You are currently on version {APP_VERSION}."
                ).format(result=result, APP_VERSION=APP_VERSION),
                duration=info_bar_duration,
                parent=self,
            )

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
    if "debug" in sys.argv:
        logging.basicConfig(level=logging.WARNING, filename="latest.log", filemode="w")
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle("Fusion")
    QThreadPool.globalInstance().setMaxThreadCount(32)
    app = App(sys.argv)
    Path(f"{platformdirs.user_data_dir()}/{APP_NAME}").mkdir(parents=True, exist_ok=True)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
