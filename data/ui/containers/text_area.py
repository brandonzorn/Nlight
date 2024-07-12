# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_area.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSlider, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(607, 508)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.size_frame = QFrame(Form)
        self.size_frame.setObjectName(u"size_frame")
        self.size_frame.setFrameShape(QFrame.StyledPanel)
        self.size_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.size_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.size_slider = QSlider(self.size_frame)
        self.size_slider.setObjectName(u"size_slider")
        self.size_slider.setFocusPolicy(Qt.NoFocus)
        self.size_slider.setMinimum(9)
        self.size_slider.setMaximum(25)
        self.size_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.size_slider)


        self.verticalLayout_2.addWidget(self.size_frame)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text_browser = QTextBrowser(self.frame)
        self.text_browser.setObjectName(u"text_browser")
        self.text_browser.setFocusPolicy(Qt.NoFocus)
        self.text_browser.setTextInteractionFlags(Qt.NoTextInteraction)
        self.text_browser.setOpenLinks(False)

        self.verticalLayout.addWidget(self.text_browser)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

