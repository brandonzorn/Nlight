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
        Dialog.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QDialog{\n"
"	background-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chapters_frame = QFrame(Dialog)
        self.chapters_frame.setObjectName(u"chapters_frame")
        self.chapters_frame.setFrameShape(QFrame.Panel)
        self.chapters_frame.setFrameShadow(QFrame.Plain)
        self.chapters_frame.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.chapters_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.chapters_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.chapters = QSpinBox(self.chapters_frame)
        self.chapters.setObjectName(u"chapters")
        self.chapters.setMaximum(999)

        self.horizontalLayout.addWidget(self.chapters)


        self.verticalLayout.addWidget(self.chapters_frame)

        self.score_frame = QFrame(Dialog)
        self.score_frame.setObjectName(u"score_frame")
        self.score_frame.setFrameShape(QFrame.Panel)
        self.score_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.score_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.score_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(450, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.score = QSpinBox(self.score_frame)
        self.score.setObjectName(u"score")
        self.score.setMaximum(10)

        self.horizontalLayout_3.addWidget(self.score)


        self.verticalLayout.addWidget(self.score_frame)

        self.status_frame = QFrame(Dialog)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setFrameShape(QFrame.Panel)
        self.status_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.status_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.status_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lib_list = QComboBox(self.status_frame)
        self.lib_list.setObjectName(u"lib_list")
        self.lib_list.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_4.addWidget(self.lib_list)


        self.verticalLayout.addWidget(self.status_frame)

        self.actions_frame = QFrame(Dialog)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setStyleSheet(u"QPushButton {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	border-left: 3px solid green;\n"
"	background-color: gray;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border-left: 3px solid green;\n"
"}")
        self.actions_frame.setFrameShape(QFrame.Panel)
        self.actions_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.actions_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_cancel = QPushButton(self.actions_frame)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.btn_delete = QPushButton(self.actions_frame)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_2.addWidget(self.btn_delete)

        self.btn_add = QPushButton(self.actions_frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_2.addWidget(self.btn_add)


        self.verticalLayout.addWidget(self.actions_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e \u0433\u043b\u0430\u0432", None))
        self.chapters.setSuffix("")
        self.chapters.setPrefix("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0446\u0435\u043d\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btn_delete.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_add.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

