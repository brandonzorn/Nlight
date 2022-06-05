# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_info.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 564)
        Form.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"images/back.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_back.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lib_list = QComboBox(Form)
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.setObjectName(u"lib_list")
        self.lib_list.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lib_list)

        self.btn_add_to_lib = QPushButton(Form)
        self.btn_add_to_lib.setObjectName(u"btn_add_to_lib")
        self.btn_add_to_lib.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"images/favorite.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_add_to_lib.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_add_to_lib)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.image = QLabel(Form)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.image)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.russian = QLabel(Form)
        self.russian.setObjectName(u"russian")
        self.russian.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.russian)

        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        self.name.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.name)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.rate_frame = QFrame(Form)
        self.rate_frame.setObjectName(u"rate_frame")
        self.rate_frame.setFrameShape(QFrame.StyledPanel)
        self.rate_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.rate_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rate = QLabel(self.rate_frame)
        self.rate.setObjectName(u"rate")

        self.verticalLayout_3.addWidget(self.rate)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.star_1 = QPushButton(self.rate_frame)
        self.star_1.setObjectName(u"star_1")
        self.star_1.setEnabled(False)
        self.star_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.star_1.setAutoDefault(False)
        self.star_1.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_1)

        self.star_2 = QPushButton(self.rate_frame)
        self.star_2.setObjectName(u"star_2")
        self.star_2.setEnabled(False)
        self.star_2.setAutoDefault(False)
        self.star_2.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_2)

        self.star_3 = QPushButton(self.rate_frame)
        self.star_3.setObjectName(u"star_3")
        self.star_3.setEnabled(False)
        self.star_3.setAutoDefault(False)
        self.star_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_3)

        self.star_4 = QPushButton(self.rate_frame)
        self.star_4.setObjectName(u"star_4")
        self.star_4.setEnabled(False)
        self.star_4.setAutoDefault(False)
        self.star_4.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_4)

        self.star_5 = QPushButton(self.rate_frame)
        self.star_5.setObjectName(u"star_5")
        self.star_5.setEnabled(False)
        self.star_5.setAutoDefault(False)
        self.star_5.setFlat(True)

        self.horizontalLayout_2.addWidget(self.star_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.rate_frame)

        self.description = QTextEdit(Form)
        self.description.setObjectName(u"description")
        self.description.setEnabled(True)
        self.description.setFocusPolicy(Qt.ClickFocus)
        self.description.setUndoRedoEnabled(True)
        self.description.setReadOnly(True)

        self.verticalLayout.addWidget(self.description)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.chapters = QListWidget(Form)
        self.chapters.setObjectName(u"chapters")

        self.horizontalLayout_5.addWidget(self.chapters)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_back.setText("")
        self.lib_list.setItemText(0, QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e", None))
        self.lib_list.setItemText(1, QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e", None))
        self.lib_list.setItemText(2, QCoreApplication.translate("Form", u"\u0427\u0438\u0442\u0430\u044e", None))
        self.lib_list.setItemText(3, QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0447\u0438\u0442\u044b\u0432\u0430\u044e", None))
        self.lib_list.setItemText(4, QCoreApplication.translate("Form", u"\u041e\u0442\u043b\u043e\u0436\u0435\u043d\u043e", None))
        self.lib_list.setItemText(5, QCoreApplication.translate("Form", u"\u0411\u0440\u043e\u0448\u0435\u043d\u043e", None))

        self.btn_add_to_lib.setText("")
        self.image.setText("")
        self.russian.setText(QCoreApplication.translate("Form", u"russian", None))
        self.name.setText(QCoreApplication.translate("Form", u"name", None))
        self.rate.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433:", None))
        self.star_1.setText("")
        self.star_2.setText("")
        self.star_3.setText("")
        self.star_4.setText("")
        self.star_5.setText("")
    # retranslateUi

