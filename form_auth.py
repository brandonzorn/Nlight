import webbrowser

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from const import app_icon_path
from form.authUI import Ui_Dialog


class FormAuth(QDialog):
    def __init__(self, catalog):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.session = catalog.session
        self.setFixedSize(self.minimumSize())
        self.setWindowTitle('Authenticate')
        self.setWindowIcon(QIcon(app_icon_path))
        self.ui.btn_get.clicked.connect(self.login)
        self.ui.btn_login.clicked.connect(self.clicked_account_login)

    def clicked_account_login(self):
        code = self.ui.txt_login.text()
        if not code:
            return
        self.session.fetch_token(code)
        if self.session.check_auth():
            self.accept()

    def login(self):
        webbrowser.open_new_tab(self.session.get_auth_url())
        self.ui.btn_login.setEnabled(True)
