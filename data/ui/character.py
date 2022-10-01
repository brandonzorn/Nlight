# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'character.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(269, 430)
        Dialog.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QScrollBar {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"QDialog{\n"
"	background-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"QComboBox {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 133, 52);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSpinBox {\n"
"	padding: 5px 5px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 133, 52);\n"
"	color: rgb(255, 255, 255);\n"
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
"}\n"
"QScrollBar {\n"
"    background: #292b2e;\n"
"    border-radius: 10px;\n"
"}"
                        "\n"
"QScrollBar:horizontal {\n"
"    height: 14px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width: 14px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle {\n"
"    background: rgba(84.000, 86.000, 86.000, 0.737);\n"
"    border-radius: 5px;\n"
"	min-height: 0px;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"    background: rgba(114.000, 115.000, 115.000, 0.827);\n"
"}\n"
"QScrollBar::handle:pressed {\n"
"    background: rgba(143.000, 145.000, 145.000, 0.933);\n"
"}\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"    background: transparent;\n"
"	subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
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
        self.title_frame.setStyleSheet(u"QAbstractButton {\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
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

        self.verticalLayout_2.addWidget(self.show_spoilers)


        self.horizontalLayout.addWidget(self.title_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.description_frame = QFrame(Dialog)
        self.description_frame.setObjectName(u"description_frame")
        self.description_frame.setStyleSheet(u"QComboBox {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 133, 52);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.description_frame.setFrameShape(QFrame.StyledPanel)
        self.description_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.description_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.description = QTextEdit(self.description_frame)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"")
        self.description.setReadOnly(True)
        self.description.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.description)


        self.verticalLayout_3.addWidget(self.description_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.image.setText("")
        self.name_label.setText(QCoreApplication.translate("Dialog", u"name", None))
        self.russian_label.setText(QCoreApplication.translate("Dialog", u"russian", None))
        self.show_spoilers.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c\n"
"\u0441\u043f\u043e\u0439\u043b\u0435\u0440\u044b", None))
        self.description.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

