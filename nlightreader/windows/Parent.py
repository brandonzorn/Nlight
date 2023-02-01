from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from data.ui.mainWindow import Ui_MainWindow
from nlightreader.items import Manga
from nlightreader.widgets import FormFacial, FormLibrary, FormShikimori, FormHistory, FormInfo


class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Form_facial = FormFacial()
        self.Form_library = FormLibrary()
        self.Form_shikimori = FormShikimori()
        self.Form_history = FormHistory()

        self.ui.btn_main.clicked.connect(lambda: self.change_widget(self.Form_facial))
        self.ui.btn_library.clicked.connect(lambda: self.change_widget(self.Form_library))
        self.ui.btn_shikimori.clicked.connect(lambda: self.change_widget(self.Form_shikimori))
        self.ui.btn_history.clicked.connect(lambda: self.change_widget(self.Form_history))

        self.Form_facial.signals.manga_open.connect(lambda x: self.open_info(x))
        self.Form_library.signals.manga_open.connect(lambda x: self.open_info(x))
        self.Form_shikimori.signals.manga_open.connect(lambda x: self.open_info(x))
        self.Form_history.signals.manga_open.connect(lambda x: self.open_info(x))

        self.ui.top_item.currentChanged.connect(self.widgets_checker)

        self.change_widget(self.Form_facial)

    def change_widget(self, widget):
        if self.ui.top_item.currentWidget() == widget:
            return
        widget.setup()
        if self.ui.top_item.currentWidget():
            self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(widget)
        self.ui.top_item.setCurrentWidget(widget)

    @Slot(Manga)
    def open_info(self, manga: Manga):
        info = FormInfo()
        info.setup(manga)
        info.opened_related_manga.connect(lambda x: self.open_info(x))
        self.ui.top_item.addWidget(info)
        self.ui.top_item.setCurrentWidget(info)

    @Slot()
    def widgets_checker(self):
        count = self.ui.top_item.count()
        if count == 1 and self.ui.side_menu_widget.isHidden():
            self.ui.top_item.currentWidget().update_content()
            self.ui.side_menu_widget.show()
        elif count > 1 and self.ui.side_menu_widget.isVisible():
            self.ui.side_menu_widget.hide()
