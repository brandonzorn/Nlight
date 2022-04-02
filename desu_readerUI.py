# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_readerUI.ui'
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
        Dialog.resize(663, 774)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        brush2 = QBrush(QColor(0, 133, 62, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush1)
        brush3 = QBrush(QColor(236, 240, 241, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        brush4 = QBrush(QColor(0, 120, 215, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush3)
        Dialog.setPalette(palette)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.img = QLabel(Dialog)
        self.img.setObjectName(u"img")

        self.gridLayout_2.addWidget(self.img, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.next_page = QPushButton(Dialog)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setFocusPolicy(Qt.NoFocus)
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.next_page, 0, 2, 1, 1)

        self.prev_page = QPushButton(Dialog)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setEnabled(True)
        self.prev_page.setFocusPolicy(Qt.NoFocus)
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.prev_page, 0, 0, 1, 1)

        self.lbl_page = QLabel(Dialog)
        self.lbl_page.setObjectName(u"lbl_page")

        self.gridLayout.addWidget(self.lbl_page, 0, 1, 1, 1)

        self.next_chp = QPushButton(Dialog)
        self.next_chp.setObjectName(u"next_chp")
        self.next_chp.setFocusPolicy(Qt.NoFocus)
        self.next_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.next_chp, 1, 2, 1, 1)

        self.prev_chp = QPushButton(Dialog)
        self.prev_chp.setObjectName(u"prev_chp")
        self.prev_chp.setFocusPolicy(Qt.NoFocus)
        self.prev_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.prev_chp, 1, 0, 1, 1)

        self.lbl_chp = QLabel(Dialog)
        self.lbl_chp.setObjectName(u"lbl_chp")

        self.gridLayout.addWidget(self.lbl_chp, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.img.setText("")
        self.label_2.setText("")
        self.next_page.setText(QCoreApplication.translate("Dialog", u">", None))
        self.prev_page.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.lbl_page.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_chp.setText(QCoreApplication.translate("Dialog", u">>", None))
        self.prev_chp.setText(QCoreApplication.translate("Dialog", u"<<", None))
        self.lbl_chp.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u0430 1", None))
    # retranslateUi

