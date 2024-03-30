from PySide6.QtCore import Slot, QSize
from qfluentwidgets import FluentWindow, FluentIcon

from nlightreader.consts.files.files import NlFluentIcons
from nlightreader.items import Manga
from nlightreader.utils import translate
from nlightreader.widgets.NlightTemplates import FormFacial, FormLibrary, FormShikimori, FormHistory, FormInfo


class ParentWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        self.library_interface = FormLibrary()
        self.facial_interface = FormFacial()
        self.shikimori_interface = FormShikimori()
        self.history_interface = FormHistory()
        self.info_interface = None

        self.library_interface.manga_open.connect(self.open_info)
        self.facial_interface.manga_open.connect(self.open_info)
        self.shikimori_interface.manga_open.connect(self.open_info)
        self.history_interface.manga_open.connect(self.open_info)

        self.stackedWidget.currentChanged.connect(self.on_widget_change)

        self.init_navigation()

    def init_navigation(self):
        self.addSubInterface(
            self.library_interface, FluentIcon.LIBRARY, translate("MainWindow", "Library"),
        )
        self.addSubInterface(
            self.facial_interface, FluentIcon.HOME, translate("MainWindow", "Main"),
        )
        self.addSubInterface(
            self.shikimori_interface, NlFluentIcons.SHIKIMORI, translate("MainWindow", "Shikimori"),
        )
        self.addSubInterface(
            self.history_interface, FluentIcon.HISTORY, translate("MainWindow", "History"),
        )

    @Slot()
    def on_widget_change(self):
        if self.stackedWidget.currentWidget().objectName() in ("FormInfo", "ReaderWidget"):
            return
        self.stackedWidget.currentWidget().setup()

    def set_min_size_by_screen(self):
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))

    @Slot(Manga)
    def open_info(self, manga: Manga):
        stack = self.stackedWidget.view
        self.stackedWidget.setEnabled(False)

        @Slot()
        def set_info_widget():
            stack.addWidget(self.info_interface)
            stack.setCurrentWidget(self.info_interface)
            self.stackedWidget.setEnabled(True)

        @Slot()
        def delete_info_widget():
            self.info_interface.close()
            self.stackedWidget.setEnabled(True)

        @Slot(Manga)
        def open_related_manga(related_manga: Manga):
            stack.removeWidget(self.info_interface)
            self.navigationInterface.panel.history.pop()
            self.info_interface.deleteLater()
            self.info_interface = None
            self.open_info(related_manga)

        self.info_interface = FormInfo()
        self.info_interface.opened_related_manga.connect(open_related_manga)
        self.info_interface.setup_done.connect(set_info_widget)
        self.info_interface.setup_error.connect(delete_info_widget)
        self.info_interface.setup(manga)
