# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_area.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QSizePolicy, QTextBrowser, QVBoxLayout, QWidget

from qfluentwidgets import CardWidget, SimpleCardWidget, Slider


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(607, 508)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.size_frame = SimpleCardWidget(Form)
        self.size_frame.setObjectName("size_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.size_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.size_slider = Slider(self.size_frame)
        self.size_slider.setObjectName("size_slider")
        self.size_slider.setFocusPolicy(Qt.NoFocus)
        self.size_slider.setMinimum(9)
        self.size_slider.setMaximum(25)
        self.size_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.size_slider)

        self.verticalLayout_2.addWidget(self.size_frame)

        self.frame = SimpleCardWidget(Form)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_browser = QTextBrowser(self.frame)
        self.text_browser.setObjectName("text_browser")
        self.text_browser.setFocusPolicy(Qt.NoFocus)
        self.text_browser.setFrameShape(QFrame.NoFrame)
        self.text_browser.setTextInteractionFlags(Qt.NoTextInteraction)
        self.text_browser.setOpenLinks(False)

        self.verticalLayout_3.addWidget(self.text_browser)

        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))

    # retranslateUi
