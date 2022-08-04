# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(587, 187)
        Dialog.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"QDialog{\n"
"	background-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 133, 52);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	border-left: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border-left: 3px solid white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.scale_box_2 = QComboBox(self.frame)
        self.scale_box_2.setObjectName(u"scale_box_2")

        self.horizontalLayout.addWidget(self.scale_box_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"StyleFactory", None))
    # retranslateUi

