import os
import sys
from threading import Thread
from typing import override

from PySide6.QtCore import QThreadPool, QTimer, Slot
from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import (
    FluentTranslator,
    isDarkTheme,
    SystemThemeListener,
)

from data import resource  # noqa:F401
from nlightreader import ParentWindow
from nlightreader.consts.app import APP_NAME, APP_VERSION
from nlightreader.consts.files import Icons
from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.utils import kodik_server
from nlightreader.utils.config import cfg
from nlightreader.utils.threads import NThread
from nlightreader.utils.translator import AppTranslator
from nlightreader.utils.utils import check_for_updates

__all__ = []


class App(QApplication):
    def __init__(self) -> None:
        super().__init__()
        self.setApplicationDisplayName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setWindowIcon(QIcon(Icons.APP))

        locale = cfg.get(cfg.language).value

        self.translator = FluentTranslator(locale)
        self.installTranslator(self.translator)

        self.app_translator = AppTranslator(locale)
        self.installTranslator(self.app_translator)


class MainWindow(ParentWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setMicaEffectEnabled(cfg.get(cfg.mica_enabled))
        self.themeListener = SystemThemeListener(self)

        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(Icons.APP))
        self._update_checker = NThread(
            target=check_for_updates,
            callback=self.show_update_info,
            error_callback=self.show_update_info,
        )

        self.settings_interface.check_for_updates_signal.connect(
            self._start_check_for_updates,
        )

        self.themeListener.start()
        if cfg.get(cfg.check_updates_at_startup):
            self._start_check_for_updates()

    @override
    def closeEvent(self, event: QCloseEvent, /) -> None:
        self.themeListener.terminate()
        self.themeListener.deleteLater()
        app.closeAllWindows()
        super().closeEvent(event)

    @override
    def _onThemeChangedFinished(self) -> None:
        super()._onThemeChangedFinished()
        if self.isMicaEffectEnabled():
            QTimer.singleShot(
                100,
                lambda: self.windowEffect.setMicaEffect(
                    self.winId(),
                    isDarkTheme(),
                ),
            )

    @Slot()
    def _start_check_for_updates(self) -> None:
        self._update_checker.terminate()
        self._update_checker.wait()
        self._update_checker.start()

    @Slot()
    def show_update_info(self, result: str | None = None) -> None:
        if result is None:
            self.settings_interface.show_err_updates_tooltip()
        elif result != APP_VERSION:
            self.settings_interface.show_has_updates_tooltip(result)
        else:
            self.settings_interface.show_no_updates_tooltip()


if __name__ == "__main__":
    APP_DATA_PATH.mkdir(parents=True, exist_ok=True)
    QThreadPool.globalInstance().setMaxThreadCount(32)

    if cfg.get(cfg.dpi_scale) != "Auto":
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
        os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpi_scale))

    kodik_server: Thread = kodik_server.get_local_server(
        server_port=8000,
        track_progress=cfg.get(cfg.enable_kodik_metrics),
    )
    kodik_server.start()

    app = App()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
