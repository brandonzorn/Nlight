# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'genres.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, PushButton, SimpleCardWidget)

class Ui_GenresDialog(object):
    def setupUi(self, GenresDialog):
        if not GenresDialog.objectName():
            GenresDialog.setObjectName(u"GenresDialog")
        GenresDialog.resize(489, 239)
        GenresDialog.setStyleSheet(u"")
        GenresDialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_2 = QVBoxLayout(GenresDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = SimpleCardWidget(GenresDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.frame)

        self.acrions_frame = SimpleCardWidget(GenresDialog)
        self.acrions_frame.setObjectName(u"acrions_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.acrions_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_btn = PushButton(self.acrions_frame)
        self.ok_btn.setObjectName(u"ok_btn")

        self.horizontalLayout.addWidget(self.ok_btn)

        self.cancel_btn = PushButton(self.acrions_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.acrions_frame)


        self.retranslateUi(GenresDialog)

        QMetaObject.connectSlotsByName(GenresDialog)
    # setupUi

    def retranslateUi(self, GenresDialog):
        GenresDialog.setWindowTitle(QCoreApplication.translate("GenresDialog", u"Genres", None))
        self.ok_btn.setText(QCoreApplication.translate("GenresDialog", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("GenresDialog", u"Cancel", None))
    # retranslateUi

