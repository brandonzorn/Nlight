from PySide6.QtWidgets import QMainWindow

from form_facial import FormFacial
from form_history import FormHistory
from form_info import FormInfo
from form_library import FormLibrary
from form_shikimori import FormShikimori
from forms.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

    def add_widget(self, widget):
        self.ui.horizontalLayout.addWidget(widget)
