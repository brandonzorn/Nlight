from PySide6.QtWidgets import QMainWindow, QStackedWidget

from app_widgets.side_widget import SideMenu
from form_facial import FormFacial
from form_history import FormHistory
from form_info import FormInfo
from form_library import FormLibrary
from form_options import FormOptions
from form_shikimori import FormShikimori
from forms.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Side menu
        self.Side_menu = SideMenu()
        self.Side_menu.ui.btn_main.clicked.connect(self.clicked_main)
        self.Side_menu.ui.btn_mylist.clicked.connect(self.clicked_library)
        self.Side_menu.ui.btn_shikimori.clicked.connect(self.clicked_shikimori)
        self.Side_menu.ui.btn_history.clicked.connect(self.clicked_history)
        self.Side_menu.ui.btn_options.clicked.connect(self.clicked_options)

        self.Form_facial = FormFacial()
        self.Form_facial.ui.list_manga.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_facial.get_current_manga()))

        self.Form_library = FormLibrary()
        self.Form_library.ui.list_manga.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_library.get_current_manga()))

        self.Form_shikimori = FormShikimori()
        self.Form_shikimori.ui.list_manga.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_shikimori.get_current_manga()))

        self.Form_history = FormHistory()
        self.Form_history.ui.listWidget.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_history.get_current_manga()))

        self.Form_info = FormInfo()
        self.Form_info.ui.btn_back.clicked.connect(self.back)

        self.Form_options = FormOptions()

        self.top_item = QStackedWidget()
        self.add_widget(self.Side_menu)
        self.add_widget(self.top_item)
        self.top_item.addWidget(self.Form_facial)
        # self.Side_menu.ui.btn_main.setIconSize(self.Side_menu.ui.btn_main.size())
        # self.Side_menu.ui.btn_shikimori.setIconSize(self.Side_menu.ui.btn_shikimori.size())
        # self.Side_menu.ui.btn_mylist.setIconSize(self.Side_menu.ui.btn_mylist.size())
        # self.Side_menu.ui.btn_history.setIconSize(self.Side_menu.ui.btn_history.size())

    def clicked_main(self):
        self.top_item.removeWidget(self.top_item.currentWidget())
        self.top_item.addWidget(self.Form_facial)

    def clicked_chapters(self, manga):
        self.Side_menu.hide()
        self.top_item.addWidget(self.Form_info)
        self.top_item.setCurrentWidget(self.Form_info)
        self.Form_info.setup(manga)

    def clicked_shikimori(self):
        self.top_item.removeWidget(self.top_item.currentWidget())
        self.top_item.addWidget(self.Form_shikimori)
        self.Form_shikimori.setup()

    def clicked_library(self):
        self.top_item.removeWidget(self.top_item.currentWidget())
        self.top_item.addWidget(self.Form_library)
        self.Form_library.update_list()

    def clicked_history(self):
        self.top_item.removeWidget(self.top_item.currentWidget())
        self.top_item.addWidget(self.Form_history)
        self.Form_history.setup()

    def clicked_catalogs(self):
        if self.Form_facial.ui.catalog_list.isHidden():
            self.Form_facial.setup_catalogs()
            self.Form_facial.ui.catalog_list.show()
        else:
            self.Form_facial.ui.catalog_list.hide()

    def change_catalog(self, index):
        self.Form_facial.update_catalog(index)

    def back(self):
        self.Side_menu.show()
        self.top_item.removeWidget(self.top_item.currentWidget())

    def clicked_options(self):
        self.Form_options.show()

    def add_widget(self, widget):
        self.ui.horizontalLayout.addWidget(widget)
