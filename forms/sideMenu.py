# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sideMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(478, 363)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 32, 32);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_mylist = QPushButton(Form)
        self.btn_mylist.setObjectName(u"btn_mylist")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_mylist.sizePolicy().hasHeightForWidth())
        self.btn_mylist.setSizePolicy(sizePolicy1)
        self.btn_mylist.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"images/library.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_mylist.setIcon(icon)
        self.btn_mylist.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.btn_mylist)

        self.btn_main = QPushButton(Form)
        self.btn_main.setObjectName(u"btn_main")
        sizePolicy1.setHeightForWidth(self.btn_main.sizePolicy().hasHeightForWidth())
        self.btn_main.setSizePolicy(sizePolicy1)
        self.btn_main.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"images/main.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main.setIcon(icon1)
        self.btn_main.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.btn_main)

        self.btn_shikimori = QPushButton(Form)
        self.btn_shikimori.setObjectName(u"btn_shikimori")
        sizePolicy1.setHeightForWidth(self.btn_shikimori.sizePolicy().hasHeightForWidth())
        self.btn_shikimori.setSizePolicy(sizePolicy1)
        self.btn_shikimori.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"images/shikimori.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_shikimori.setIcon(icon2)
        self.btn_shikimori.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.btn_shikimori)

        self.btn_history = QPushButton(Form)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy1.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy1)
        self.btn_history.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"images/history.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_history.setIcon(icon3)
        self.btn_history.setIconSize(QSize(40, 40))
        self.btn_history.setAutoExclusive(False)
        self.btn_history.setAutoDefault(False)

        self.verticalLayout.addWidget(self.btn_history)

        self.verticalSpacer_2 = QSpacerItem(18, 168, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_options = QPushButton(Form)
        self.btn_options.setObjectName(u"btn_options")
        sizePolicy1.setHeightForWidth(self.btn_options.sizePolicy().hasHeightForWidth())
        self.btn_options.setSizePolicy(sizePolicy1)
        self.btn_options.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.btn_options.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.btn_options)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_mylist.setText("")
        self.btn_main.setText("")
        self.btn_shikimori.setText("")
        self.btn_history.setText("")
        self.btn_options.setText("")
    # retranslateUi

