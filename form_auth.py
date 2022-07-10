import webbrowser

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from const.icons import app_icon_path
from forms.authUI import Ui_Dialog


class FormAuth(QDialog):
    def __init__(self, catalog):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lbl_shikimori.setText(catalog.catalog_name)
        self.session = catalog.session
        self.setup_form(catalog.fields)

    def setup_form(self, fields: int):
        self.setWindowTitle('Authenticate')
        self.setWindowIcon(QIcon(app_icon_path))
        self.setFixedSize(self.minimumSize())
        if fields == 1:
            self.ui.btn_get.clicked.connect(self.login)
            self.ui.btn_login.clicked.connect(self.clicked_account_login)
            self.ui.widget.hide()
        else:
            self.ui.btn_login.clicked.connect(self.verify_user_data)
            self.ui.code_widget.hide()

    def clicked_account_login(self):
        code = self.ui.auth_code.text()
        if not code:
            return
        self.session.fetch_token(code)
        if self.session.check_auth():
            self.accept()

    def verify_user_data(self):
        if self.ui.username.text() and self.ui.password.text():
            self.accept()

    def get_user_data(self):
        return {'username': self.ui.username.text(), 'password': self.ui.password.text()}

    def login(self):
        webbrowser.open_new_tab(self.session.get_auth_url())
