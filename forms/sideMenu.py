# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sideMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(464, 309)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_mylist = QPushButton(Form)
        self.btn_mylist.setObjectName(u"btn_mylist")
        self.btn_mylist.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"images/library.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_mylist.setIcon(icon)

        self.verticalLayout.addWidget(self.btn_mylist)

        self.btn_main = QPushButton(Form)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"images/main.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main.setIcon(icon1)

        self.verticalLayout.addWidget(self.btn_main)

        self.btn_shikimori = QPushButton(Form)
        self.btn_shikimori.setObjectName(u"btn_shikimori")
        self.btn_shikimori.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"images/shikimori.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_shikimori.setIcon(icon2)

        self.verticalLayout.addWidget(self.btn_shikimori)

        self.btn_history = QPushButton(Form)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"images/history.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_history.setIcon(icon3)

        self.verticalLayout.addWidget(self.btn_history)

        self.verticalSpacer_2 = QSpacerItem(20, 328, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_mylist.setText("")
        self.btn_main.setText("")
        self.btn_shikimori.setText("")
        self.btn_history.setText("")
    # retranslateUi

