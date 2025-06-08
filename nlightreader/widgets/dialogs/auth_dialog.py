import webbrowser

from qfluentwidgets import (
    LineEdit,
    MessageBoxBase,
    PasswordLineEdit,
    PushButton,
    SubtitleLabel,
)


class AbstractAuthDialog(MessageBoxBase):
    def __init__(self, catalog, parent):
        super().__init__(parent)
        self.session = catalog.session
        self.widget.setMinimumWidth(350)

        self.titleLabel = SubtitleLabel(self.tr("Authenticate"), parent=self)

        self.yesButton.setText(self.tr("Sign in"))
        self.yesButton.setEnabled(False)

        self.cancelButton.setText(self.tr("Cancel"))

        self.viewLayout.addWidget(self.titleLabel)

    def verify_user_data(self):
        raise NotImplementedError

    def get_user_data(self):
        raise NotImplementedError


class TokenAuthMessageBox(AbstractAuthDialog):
    def __init__(self, catalog, parent):
        super().__init__(catalog, parent)
        self.getCodeButton = PushButton(self.tr("Get code"))
        self.getCodeButton.clicked.connect(self.__open_login_page)

        self.tokenLineEdit = LineEdit(self)
        self.tokenLineEdit.setPlaceholderText(self.tr("Authorization code"))
        self.tokenLineEdit.setClearButtonEnabled(True)
        self.tokenLineEdit.textChanged.connect(self.verify_user_data)

        self.viewLayout.addWidget(self.tokenLineEdit)
        self.viewLayout.addWidget(self.getCodeButton)

    def verify_user_data(self):
        self.yesButton.setEnabled(bool(self.tokenLineEdit.text()))

    def get_user_data(self):
        return {
            "token": self.tokenLineEdit.text(),
        }

    def __open_login_page(self):
        webbrowser.open_new_tab(self.session.get_auth_url())


class UserDataAuthMessageBox(AbstractAuthDialog):
    def __init__(self, catalog, parent):
        super().__init__(catalog, parent)
        self.loginLineEdit = LineEdit(self)
        self.loginLineEdit.setPlaceholderText(self.tr("Login"))
        self.loginLineEdit.setClearButtonEnabled(True)
        self.loginLineEdit.textChanged.connect(self.verify_user_data)

        self.passwordLineEdit = PasswordLineEdit(self)
        self.passwordLineEdit.setPlaceholderText(self.tr("Password"))
        self.passwordLineEdit.setClearButtonEnabled(True)
        self.passwordLineEdit.textChanged.connect(self.verify_user_data)

        self.viewLayout.addWidget(self.loginLineEdit)
        self.viewLayout.addWidget(self.passwordLineEdit)

    def verify_user_data(self):
        self.yesButton.setEnabled(
            bool(
                self.loginLineEdit.text(),
            )
            and bool(
                self.passwordLineEdit.text(),
            ),
        )

    def get_user_data(self):
        return {
            "username": self.loginLineEdit.text(),
            "password": self.passwordLineEdit.text(),
        }
