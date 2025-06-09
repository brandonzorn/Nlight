from PySide6.QtCore import QSize, Slot
from qfluentwidgets import FluentIcon, FluentWindow, NavigationItemPosition

from nlightreader.consts.files.files import NlFluentIcons
from nlightreader.models import Manga
from nlightreader.utils.translator import translate
from nlightreader.widgets.pages import (
    ExternalLibraryPage,
    HistoryPage,
    InfoPage,
    LibraryPage,
    MainPage,
    SettingsPage,
)


class ParentWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        self.library_interface = LibraryPage()
        self.main_interface = MainPage()
        self.external_library_interface = ExternalLibraryPage()
        self.history_interface = HistoryPage()

        self.settings_interface = SettingsPage()

        self.info_interface: InfoPage | None = None

        self.library_interface.manga_open.connect(self.open_info)
        self.main_interface.manga_open.connect(self.open_info)
        self.external_library_interface.manga_open.connect(self.open_info)
        self.history_interface.manga_open.connect(self.open_info)

        self.stackedWidget.currentChanged.connect(self.on_widget_change)

        self.init_navigation()

    def init_navigation(self):
        self.addSubInterface(
            self.library_interface,
            FluentIcon.LIBRARY,
            translate("MainWindow", "Library"),
        )
        self.addSubInterface(
            self.main_interface,
            FluentIcon.HOME,
            translate("MainWindow", "Main"),
        )
        self.addSubInterface(
            self.external_library_interface,
            NlFluentIcons.SHIKIMORI,
            translate("MainWindow", "Shikimori"),
        )
        self.addSubInterface(
            self.history_interface,
            FluentIcon.HISTORY,
            translate("MainWindow", "History"),
        )
        self.addSubInterface(
            self.settings_interface,
            FluentIcon.SETTING,
            translate("MainWindow", "Settings"),
            position=NavigationItemPosition.BOTTOM,
        )

    @Slot(int)
    def on_widget_change(self, value):
        if value in range(4):
            if any(
                i.objectName() == "FormInfo"
                for i in self.stackedWidget.view.children()
            ):
                self.delete_info_interface()
        self.navigationInterface.setReturnButtonVisible(
            self.stackedWidget.count() > 5,
        )
        if self.stackedWidget.currentWidget().objectName() in (
            "FormInfo",
            "ReaderWidget",
        ):
            return
        self.stackedWidget.currentWidget().setup()

    def set_min_size_by_screen(self):
        self.setMinimumSize(
            QSize(
                self.screen().size().width() // 2,
                self.screen().size().height() // 2,
            ),
        )

    def delete_info_interface(self):
        self.stackedWidget.view.removeWidget(self.info_interface)
        self.info_interface.deleteLater()
        self.info_interface = None

    @Slot(Manga)
    def open_info(self, manga: Manga):
        stack = self.stackedWidget.view
        self.stackedWidget.setEnabled(False)

        @Slot()
        def set_info_widget():
            stack.addWidget(self.info_interface)
            self.switchTo(self.info_interface)
            self.stackedWidget.setEnabled(True)

        @Slot()
        def delete_info_widget():
            self.info_interface.close()
            self.stackedWidget.setEnabled(True)

        if self.stackedWidget.currentWidget().objectName() == "FormInfo":
            self.stackedWidget.view.removeWidget(self.info_interface)

        self.info_interface = InfoPage()
        self.info_interface.opened_related_manga.connect(self.open_info)
        self.info_interface.setup_done.connect(set_info_widget)
        self.info_interface.setup_error.connect(delete_info_widget)
        self.info_interface.setup(manga)


__all__ = [
    "ParentWindow",
]
