# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_info.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(873, 530)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        Dialog.setPalette(palette)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_back = QPushButton(Dialog)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_mylist = QPushButton(Dialog)
        self.btn_mylist.setObjectName(u"btn_mylist")
        self.btn_mylist.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btn_mylist)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.image = QLabel(Dialog)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.image, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name = QLabel(Dialog)
        self.name.setObjectName(u"name")

        self.verticalLayout.addWidget(self.name)

        self.russian = QLabel(Dialog)
        self.russian.setObjectName(u"russian")

        self.verticalLayout.addWidget(self.russian)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.rate = QLabel(Dialog)
        self.rate.setObjectName(u"rate")

        self.verticalLayout.addWidget(self.rate)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.star_1 = QPushButton(Dialog)
        self.star_1.setObjectName(u"star_1")
        self.star_1.setEnabled(False)
        self.star_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.star_1.setAutoDefault(False)
        self.star_1.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_1)

        self.star_2 = QPushButton(Dialog)
        self.star_2.setObjectName(u"star_2")
        self.star_2.setEnabled(False)
        self.star_2.setAutoDefault(False)
        self.star_2.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_2)

        self.star_3 = QPushButton(Dialog)
        self.star_3.setObjectName(u"star_3")
        self.star_3.setEnabled(False)
        self.star_3.setAutoDefault(False)
        self.star_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_3)

        self.star_4 = QPushButton(Dialog)
        self.star_4.setObjectName(u"star_4")
        self.star_4.setEnabled(False)
        self.star_4.setAutoDefault(False)
        self.star_4.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_4)

        self.star_5 = QPushButton(Dialog)
        self.star_5.setObjectName(u"star_5")
        self.star_5.setEnabled(False)
        self.star_5.setAutoDefault(False)
        self.star_5.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.description = QTextEdit(Dialog)
        self.description.setObjectName(u"description")
        self.description.setEnabled(False)

        self.gridLayout.addWidget(self.description, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.chapters = QListWidget(Dialog)
        self.chapters.setObjectName(u"chapters")

        self.gridLayout_3.addWidget(self.chapters, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_back.setText("")
        self.btn_mylist.setText("")
        self.image.setText("")
        self.name.setText("")
        self.russian.setText("")
        self.rate.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433:", None))
        self.star_1.setText("")
        self.star_2.setText("")
        self.star_3.setText("")
        self.star_4.setText("")
        self.star_5.setText("")
    # retranslateUi

