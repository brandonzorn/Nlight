from PySide6.QtWidgets import QMainWindow

from data.ui.mainWindow import Ui_MainWindow
from desureader.utils.database import Database
from desureader.widgets.facial import FormFacial
from desureader.widgets.history import FormHistory
from desureader.widgets.info import FormInfo
from desureader.widgets.library import FormLibrary
from desureader.widgets.shikimori import FormShikimori


class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db: Database = Database()
        self.ui.btn_ongoings.hide()
        self.ui.btn_downloads.hide()
        self.ui.btn_main.clicked.connect(self.clicked_main)
        self.ui.btn_mylist.clicked.connect(self.clicked_library)
        self.ui.btn_shikimori.clicked.connect(self.clicked_shikimori)
        self.ui.btn_history.clicked.connect(self.clicked_history)

        self.Form_facial = FormFacial()
        self.Form_facial.ui.items_list.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_facial.get_current_manga()))

        self.Form_library = FormLibrary()
        self.Form_library.ui.items_list.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_library.get_current_manga()))

        self.Form_shikimori = FormShikimori()
        self.Form_shikimori.ui.items_list.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_shikimori.get_current_manga()))

        self.Form_history = FormHistory()
        self.Form_history.ui.items_list.doubleClicked.connect(
            lambda: self.clicked_chapters(self.Form_history.get_current_manga()))

        self.Form_info = FormInfo()
        self.Form_info.ui.back_btn.clicked.connect(self.back)

        self.ui.top_item.addWidget(self.Form_facial)

    def clicked_main(self):
        self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(self.Form_facial)

    def clicked_chapters(self, manga):
        self.ui.side_menu_widget.hide()
        self.ui.top_item.addWidget(self.Form_info)
        self.ui.top_item.setCurrentWidget(self.Form_info)
        self.db.add_manga(manga)
        self.Form_info.setup(manga)

    def clicked_shikimori(self):
        self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(self.Form_shikimori)
        self.Form_shikimori.setup()

    def clicked_library(self):
        self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(self.Form_library)
        self.Form_library.update_list()

    def clicked_history(self):
        self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(self.Form_history)
        self.Form_history.setup()

    def back(self):
        self.ui.side_menu_widget.show()
        self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
