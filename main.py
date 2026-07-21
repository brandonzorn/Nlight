import os
import sys
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
from nlightreader.consts.app import APP_BRANCH, APP_NAME, APP_VERSION
from nlightreader.consts.files import Icons
from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.consts.urls import GITHUB_REPO_API
from nlightreader.utils import kodik_server
from nlightreader.utils.config import cfg
from nlightreader.utils.threads import Thread
from nlightreader.utils.translator import AppTranslator
from nlightreader.utils.utils import make_request

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
        self._update_checker = Thread(
            target=self.check_for_updates,
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

    @staticmethod
    def check_for_updates() -> str | None:
        response = make_request(
            f"{GITHUB_REPO_API}/releases",
            "GET",
            params={"per_page": 2},
            content_type="json",
        )
        if not isinstance(response, list):
            return None
        latest_version = None
        for release in reversed(response):
            if not isinstance(release, dict):
                continue
            version = str(release.get("tag_name") or "")
            if APP_BRANCH in version:
                latest_version = version
        return latest_version

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

    kodik_server = kodik_server.get_local_server(
        server_port=8000,
        track_progress=cfg.get(cfg.enable_kodik_metrics),
    )
    kodik_server.start()

    app = App()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
