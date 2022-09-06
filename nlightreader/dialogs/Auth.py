import webbrowser

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from const.icons import app_icon_path
from data.ui.auth import Ui_Dialog


class FormAuth(QDialog):
    def __init__(self, catalog):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.catalog_label.setText(catalog.catalog_name)
        self.session = catalog.session
        self.setup_form(catalog.fields)

    def setup_form(self, fields: int):
        self.setWindowTitle('Authenticate')
        self.setWindowIcon(QIcon(app_icon_path))
        self.setFixedSize(self.minimumSize())
        if fields == 1:
            self.ui.get_code_btn.clicked.connect(self.login)
            self.ui.auth_btn.clicked.connect(lambda: self.verify_user_data(fields))
            self.ui.two_frame.hide()
        else:
            self.ui.auth_btn.clicked.connect(lambda: self.verify_user_data(fields))
            self.ui.one_frame.hide()

    def verify_user_data(self, fields: int):
        if fields == 1:
            code = self.ui.auth_code_line.text()
            if not code:
                return
            self.session.fetch_token(code)
            if self.session.check_auth():
                self.accept()
        else:
            if self.ui.login_line.text() and self.ui.password_line.text():
                self.accept()

    def get_user_data(self):
        return {'username': self.ui.login_line.text(), 'password': self.ui.password_line.text()}

    def login(self):
        webbrowser.open_new_tab(self.session.get_auth_url())
