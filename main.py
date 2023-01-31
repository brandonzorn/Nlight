import sys
import time

import darkdetect
from PySide6.QtCore import QSize, Qt, QTranslator, QLocale, QThreadPool
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication

from nlightreader import ParentWindow
from nlightreader.consts import app_icon_path, APP_VERSION, APP_NAME
from nlightreader.consts.paths.fonts import helvetica_regular_path
from nlightreader.utils import init_app_paths, get_locale_path, get_ui_style, Worker


class App(ParentWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        self.setWindowTitle(APP_NAME)
        self.update_theme()
        self.show()

    def update_theme(self):
        def set_style():
            app.setStyleSheet(get_ui_style(darkdetect.theme()))
            self.update_theme()

        def theme_updater():
            theme = darkdetect.theme()
            while True:
                time.sleep(1)
                if darkdetect.theme() != theme or self.isHidden():
                    return
        Worker(target=theme_updater, callback=set_style).start()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle('Fusion')
    QThreadPool.globalInstance().setMaxThreadCount(60)
    app = QApplication(sys.argv)
    trans = QTranslator()
    trans.load(get_locale_path(QLocale().language()))
    app.installTranslator(trans)
    font = QFont(helvetica_regular_path, 9)
    app.setFont(font)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setWindowIcon(QIcon(app_icon_path))
    app.setStyleSheet(get_ui_style(darkdetect.theme()))
    app_paths = [APP_NAME]
    init_app_paths(app_paths)
    a = App()
    sys.exit(app.exec())
