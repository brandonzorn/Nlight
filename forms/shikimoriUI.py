# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shikimoriUI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(515, 451)
        Form.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_manga = QListWidget(Form)
        self.list_manga.setObjectName(u"list_manga")

        self.verticalLayout.addWidget(self.list_manga)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_search = QLineEdit(Form)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.line_search)

        self.btn_search = QPushButton(Form)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_search)

        self.prev_page = QPushButton(Form)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.prev_page)

        self.label_page = QLabel(Form)
        self.label_page.setObjectName(u"label_page")
        self.label_page.setTextFormat(Qt.AutoText)
        self.label_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_page)

        self.next_page = QPushButton(Form)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.next_page)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.b_planned = QPushButton(Form)
        self.b_planned.setObjectName(u"b_planned")
        self.b_planned.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.b_planned)

        self.b_completed = QPushButton(Form)
        self.b_completed.setObjectName(u"b_completed")
        self.b_completed.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.b_completed)

        self.b_watching = QPushButton(Form)
        self.b_watching.setObjectName(u"b_watching")
        self.b_watching.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.b_watching)

        self.b_rewatching = QPushButton(Form)
        self.b_rewatching.setObjectName(u"b_rewatching")
        self.b_rewatching.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.b_rewatching)

        self.b_on_hold = QPushButton(Form)
        self.b_on_hold.setObjectName(u"b_on_hold")
        self.b_on_hold.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.b_on_hold)

        self.b_dropped = QPushButton(Form)
        self.b_dropped.setObjectName(u"b_dropped")
        self.b_dropped.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.b_dropped)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_auth = QPushButton(Form)
        self.btn_auth.setObjectName(u"btn_auth")
        self.btn_auth.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.btn_auth)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_search.setText("")
        self.prev_page.setText("")
        self.label_page.setText(QCoreApplication.translate("Form", u" \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page.setText("")
        self.b_planned.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043e", None))
        self.b_completed.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e", None))
        self.b_watching.setText(QCoreApplication.translate("Form", u"\u0427\u0438\u0442\u0430\u044e", None))
        self.b_rewatching.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0447\u0438\u0442\u044b\u0432\u0430\u044e", None))
        self.b_on_hold.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043b\u043e\u0436\u0435\u043d\u043e", None))
        self.b_dropped.setText(QCoreApplication.translate("Form", u"\u0411\u0440\u043e\u0448\u0435\u043d\u043e", None))
        self.btn_auth.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

