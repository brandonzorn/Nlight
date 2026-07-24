from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import (
    FluentIcon,
    FluentWindow,
    NavigationItemPosition,
    Router,
)

from nlightreader.consts.files.files import NlFluentIcons
from nlightreader.models import Manga
from nlightreader.widgets.pages import (
    ExternalLibraryPage,
    HistoryPage,
    InfoPage,
    LibraryPage,
    MainPage,
    SettingsPage,
)


class ParentWindow(FluentWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setMinimumSize(self.screen().size() / 2)

        self.library_interface = LibraryPage(self)
        self.main_interface = MainPage(self)
        self.external_library_interface = ExternalLibraryPage(self)
        self.history_interface = HistoryPage(self)
        self.settings_interface = SettingsPage(self)

        self.info_interface: InfoPage | None = None

        self.library_interface.manga_open.connect(self.open_info)
        self.main_interface.manga_open.connect(self.open_info)
        self.external_library_interface.manga_open.connect(self.open_info)
        self.history_interface.manga_open.connect(self.open_info)

        self.settings_interface.mica_enable_changed.connect(
            self.setMicaEffectEnabled,
        )

        self.stackedWidget.currentChanged.connect(self.on_widget_change)

        self.init_navigation()

    def init_navigation(self) -> None:
        self.addSubInterface(
            self.library_interface,
            FluentIcon.LIBRARY,
            self.tr("Library"),
        )
        self.addSubInterface(
            self.main_interface,
            FluentIcon.HOME,
            self.tr("Main"),
        )
        self.addSubInterface(
            self.external_library_interface,
            NlFluentIcons.SHIKIMORI,
            self.tr("Shikimori"),
        )
        self.addSubInterface(
            self.history_interface,
            FluentIcon.HISTORY,
            self.tr("History"),
        )
        self.addSubInterface(
            self.settings_interface,
            FluentIcon.SETTING,
            self.tr("Settings"),
            position=NavigationItemPosition.BOTTOM,
        )

    def _switch_to_last(self) -> None:
        last = self._history.history[-1].routeKey
        self.switchTo(self.stackedWidget.findChild(QWidget, name=last))

    @property
    def _history(self) -> Router:
        return self.navigationInterface.panel.history

    @Slot(int)
    def on_widget_change(self, value: int) -> None:
        if value in range(4):
            if any(
                i.objectName() == "InfoPage"
                for i in self.stackedWidget.view.children()
            ):
                self.delete_info_interface()
        self.navigationInterface.setReturnButtonVisible(
            self.stackedWidget.count() > 5,
        )
        if self.stackedWidget.currentWidget().objectName() in (
            "InfoPage",
            "ReaderWidget",
        ):
            return
        self.stackedWidget.currentWidget().setup()

    def delete_info_interface(self) -> None:
        if self.info_interface is not None:
            self.stackedWidget.view.removeWidget(self.info_interface)
            self.info_interface.deleteLater()
            self.info_interface = None

    @Slot(Manga)
    def open_info(self, manga: Manga) -> None:
        stack = self.stackedWidget.view
        self.stackedWidget.setEnabled(False)

        @Slot()
        def set_info_widget() -> None:
            stack.addWidget(self.info_interface)
            self.switchTo(self.info_interface)
            self.stackedWidget.setEnabled(True)

        @Slot()
        def delete_info_widget() -> None:
            self.info_interface.close()
            self.stackedWidget.setEnabled(True)

        if self.stackedWidget.currentWidget().objectName() == "FormInfo":
            self.stackedWidget.view.removeWidget(self.info_interface)

        self.info_interface = InfoPage(manga)
        self.info_interface.opened_related_manga.connect(self.open_info)
        self.info_interface.setup_done.connect(set_info_widget)
        self.info_interface.setup_error.connect(delete_info_widget)
        self.info_interface.setup()


__all__ = ["ParentWindow"]
