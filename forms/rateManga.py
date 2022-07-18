# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rateManga.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(569, 525)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 32, 32);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.chapters = QSpinBox(self.frame)
        self.chapters.setObjectName(u"chapters")
        self.chapters.setMaximum(999)

        self.horizontalLayout.addWidget(self.chapters)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(450, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.score = QSpinBox(self.frame_2)
        self.score.setObjectName(u"score")
        self.score.setMaximum(10)

        self.horizontalLayout_3.addWidget(self.score)


        self.verticalLayout.addWidget(self.frame_2)

        self.lib_list = QComboBox(Dialog)
        self.lib_list.setObjectName(u"lib_list")

        self.verticalLayout.addWidget(self.lib_list)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_cancel = QPushButton(self.frame_3)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.btn_add = QPushButton(self.frame_3)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_add)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Chapters", None))
        self.chapters.setSuffix("")
        self.chapters.setPrefix("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Score", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_add.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi

