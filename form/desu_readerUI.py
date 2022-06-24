# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_readerUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(688, 647)
        palette = QPalette()
        Dialog.setPalette(palette)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.text_size_slider = QSlider(Dialog)
        self.text_size_slider.setObjectName(u"text_size_slider")
        self.text_size_slider.setEnabled(True)
        self.text_size_slider.setFocusPolicy(Qt.NoFocus)
        self.text_size_slider.setMinimum(9)
        self.text_size_slider.setMaximum(25)
        self.text_size_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.text_size_slider)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 668, 537))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.img = QLabel(self.scrollAreaWidgetContents)
        self.img.setObjectName(u"img")
        self.img.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.img.setWordWrap(True)
        self.img.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.img)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_page = QPushButton(Dialog)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setEnabled(True)
        self.prev_page.setFocusPolicy(Qt.NoFocus)
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_3.addWidget(self.prev_page)

        self.lbl_page = QLabel(Dialog)
        self.lbl_page.setObjectName(u"lbl_page")

        self.horizontalLayout_3.addWidget(self.lbl_page)

        self.next_page = QPushButton(Dialog)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setFocusPolicy(Qt.NoFocus)
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_3.addWidget(self.next_page)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prev_chp = QPushButton(Dialog)
        self.prev_chp.setObjectName(u"prev_chp")
        self.prev_chp.setFocusPolicy(Qt.NoFocus)
        self.prev_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_2.addWidget(self.prev_chp)

        self.lbl_chp = QLabel(Dialog)
        self.lbl_chp.setObjectName(u"lbl_chp")

        self.horizontalLayout_2.addWidget(self.lbl_chp)

        self.next_chp = QPushButton(Dialog)
        self.next_chp.setObjectName(u"next_chp")
        self.next_chp.setFocusPolicy(Qt.NoFocus)
        self.next_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_2.addWidget(self.next_chp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.img.setText("")
        self.prev_page.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.lbl_page.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page.setText(QCoreApplication.translate("Dialog", u">", None))
        self.prev_chp.setText(QCoreApplication.translate("Dialog", u"<<", None))
        self.lbl_chp.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u0430 1", None))
        self.next_chp.setText(QCoreApplication.translate("Dialog", u">>", None))
    # retranslateUi

