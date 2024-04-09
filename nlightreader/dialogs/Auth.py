import webbrowser

from PySide6.QtWidgets import QDialog, QLayout

from data.ui.dialogs.auth import Ui_Dialog


class FormAuth(QDialog):
    def __init__(self, catalog, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Authenticate")
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.ui.catalog_label.setText(catalog.CATALOG_NAME)
        self.session = catalog.session
        self.setup_form(catalog.fields)

    def setup_form(self, fields: int):
        if fields == 1:
            self.ui.get_code_btn.clicked.connect(self.__open_login_page)
            self.ui.auth_btn.clicked.connect(self.verify_user_data)
            self.ui.two_frame.hide()
        else:
            self.ui.auth_btn.clicked.connect(self.verify_user_data)
            self.ui.one_frame.hide()

    def verify_user_data(self):
        if (self.ui.login_line.text() and self.ui.password_line.text()) or self.ui.auth_code_line.text():
            self.accept()

    def get_user_data(self):
        return {
            "username": self.ui.login_line.text(),
            "password": self.ui.password_line.text(),
            "token": self.ui.auth_code_line.text(),
        }

    def __open_login_page(self):
        webbrowser.open_new_tab(self.session.get_auth_url())
