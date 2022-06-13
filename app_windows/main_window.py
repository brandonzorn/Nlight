from PySide6.QtWidgets import QMainWindow

from form.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def add_widget(self, widget):
        self.ui.horizontalLayout.addWidget(widget)
