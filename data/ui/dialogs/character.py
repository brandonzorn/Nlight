# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'character.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(269, 430)
        Dialog.setWindowTitle(u"Dialog")
        Dialog.setStyleSheet(u"")
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_frame = QFrame(Dialog)
        self.image_frame.setObjectName(u"image_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_frame.sizePolicy().hasHeightForWidth())
        self.image_frame.setSizePolicy(sizePolicy)
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.image_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image = QLabel(self.image_frame)
        self.image.setObjectName(u"image")
        self.image.setScaledContents(True)

        self.verticalLayout.addWidget(self.image)


        self.horizontalLayout.addWidget(self.image_frame)

        self.title_frame = QFrame(Dialog)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setStyleSheet(u"")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.title_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name_label = QLabel(self.title_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.name_label)

        self.russian_label = QLabel(self.title_frame)
        self.russian_label.setObjectName(u"russian_label")
        self.russian_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.russian_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.show_spoilers = QCheckBox(self.title_frame)
        self.show_spoilers.setObjectName(u"show_spoilers")
        self.show_spoilers.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_2.addWidget(self.show_spoilers)


        self.horizontalLayout.addWidget(self.title_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.description_frame = QFrame(Dialog)
        self.description_frame.setObjectName(u"description_frame")
        self.description_frame.setStyleSheet(u"")
        self.description_frame.setFrameShape(QFrame.StyledPanel)
        self.description_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.description_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.description = QTextBrowser(self.description_frame)
        self.description.setObjectName(u"description")
        self.description.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.description)


        self.verticalLayout_3.addWidget(self.description_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.image.setText("")
        self.name_label.setText(QCoreApplication.translate("Dialog", u"name", None))
        self.russian_label.setText(QCoreApplication.translate("Dialog", u"russian", None))
        self.show_spoilers.setText(QCoreApplication.translate("Dialog", u"Show spoilers", None))
        pass
    # retranslateUi

