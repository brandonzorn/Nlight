import webbrowser

from qfluentwidgets import MessageBoxBase, LineEdit, SubtitleLabel, PushButton

from nlightreader.utils import translate


class AuthMessageBox(MessageBoxBase):
    def __init__(self, catalog, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel("Authenticate", parent=self)
        self.tokenLineEdit = LineEdit(self)
        self.getCodeButton = PushButton(translate("Dialog", "Get code"), None)

        self.tokenLineEdit.setPlaceholderText(translate("Dialog", "Authorization code"))
        self.tokenLineEdit.setClearButtonEnabled(True)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.tokenLineEdit)
        self.viewLayout.addWidget(self.getCodeButton)

        self.yesButton.setText(translate("Dialog", "Sign in"))
        self.cancelButton.setText(translate("Dialog", "Cancel"))

        self.widget.setMinimumWidth(350)

        self.yesButton.clicked.connect(lambda: self.verify_user_data(catalog.fields))
        self.getCodeButton.clicked.connect(self.open_login_page)

        self.session = catalog.session
        self.setup_form(catalog.fields)

    def setup_form(self, fields: int):
        if fields == 1:
            ...
            # self.ui.two_frame.hide()
        else:
            ...
            # self.ui.one_frame.hide()

    def verify_user_data(self, fields: int):
        if fields == 1:
            code = self.tokenLineEdit.text()
            if not code:
                return
            self.session.fetch_token(code)
            if self.session.check_auth():
                self.accept()
        # else:
        #    if self.ui.login_line.text() and self.ui.password_line.text():
        #        self.accept()

    def get_user_data(self):
        return {
            "username": self.ui.login_line.text(),
            "password": self.ui.password_line.text(),
        }

    def open_login_page(self):
        webbrowser.open_new_tab(self.session.get_auth_url())
