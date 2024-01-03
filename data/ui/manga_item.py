# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manga_item.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

from qfluentwidgets import BodyLabel, CardWidget, ElevatedCardWidget, SimpleCardWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(550, 486)
        Form.setContextMenuPolicy(Qt.CustomContextMenu)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QLabel(Form)
        self.image.setObjectName("image")
        self.image.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout.addWidget(self.image)

        self.verticalSpacer = QSpacerItem(20, 412, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.name_lbl = BodyLabel(Form)
        self.name_lbl.setObjectName("name_lbl")
        self.name_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.name_lbl)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.image.setText("")
        self.name_lbl.setText("")

    # retranslateUi
