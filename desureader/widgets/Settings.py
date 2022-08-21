

from data.ui.settings import Ui_Form
from desureader.widgets.BaseWidget import BaseWidget


class FormSettings(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
