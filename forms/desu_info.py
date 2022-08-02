# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_info.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout,
                               QLabel, QListWidget, QPushButton,
                               QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(672, 549)
        Form.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 133, 52);\n"
"background-color: rgb(32, 32, 32);")
        self.horizontalLayout_6 = QHBoxLayout(Form)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_back = QPushButton(self.frame)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"images/back.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_back.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_back)

        self.horizontalSpacer = QSpacerItem(123, 36, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.add_lib_frame = QFrame(self.frame)
        self.add_lib_frame.setObjectName(u"add_lib_frame")
        self.add_lib_frame.setFrameShape(QFrame.StyledPanel)
        self.add_lib_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.add_lib_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lib_list = QComboBox(self.add_lib_frame)
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.addItem("")
        self.lib_list.setObjectName(u"lib_list")
        self.lib_list.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_4.addWidget(self.lib_list)

        self.btn_add_to_lib = QPushButton(self.add_lib_frame)
        self.btn_add_to_lib.setObjectName(u"btn_add_to_lib")
        self.btn_add_to_lib.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"images/favorite.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_add_to_lib.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.btn_add_to_lib)


        self.verticalLayout_4.addWidget(self.add_lib_frame)

        self.add_shikimrori_frame = QFrame(self.frame)
        self.add_shikimrori_frame.setObjectName(u"add_shikimrori_frame")
        self.add_shikimrori_frame.setFrameShape(QFrame.StyledPanel)
        self.add_shikimrori_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.add_shikimrori_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_shikimori = QPushButton(self.add_shikimrori_frame)
        self.btn_shikimori.setObjectName(u"btn_shikimori")
        self.btn_shikimori.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.btn_shikimori)


        self.verticalLayout_4.addWidget(self.add_shikimrori_frame)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.frame)

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

        self.name_frame = QFrame(Form)
        self.name_frame.setObjectName(u"name_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_frame.sizePolicy().hasHeightForWidth())
        self.name_frame.setSizePolicy(sizePolicy1)
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.name_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.russian = QLabel(self.name_frame)
        self.russian.setObjectName(u"russian")
        self.russian.setWordWrap(True)

        self.verticalLayout.addWidget(self.russian)

        self.name = QLabel(self.name_frame)
        self.name.setObjectName(u"name")
        self.name.setWordWrap(True)

        self.verticalLayout.addWidget(self.name)

        self.verticalSpacer = QSpacerItem(38, 186, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.name_frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

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


        self.verticalLayout_2.addWidget(self.rate_frame)

        self.related_frame = QFrame(Form)
        self.related_frame.setObjectName(u"related_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.related_frame.sizePolicy().hasHeightForWidth())
        self.related_frame.setSizePolicy(sizePolicy2)
        self.related_frame.setFrameShape(QFrame.StyledPanel)
        self.related_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.related_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.related_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.manga_relations = QListWidget(self.related_frame)
        self.manga_relations.setObjectName(u"manga_relations")
        sizePolicy1.setHeightForWidth(self.manga_relations.sizePolicy().hasHeightForWidth())
        self.manga_relations.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.manga_relations)


        self.verticalLayout_2.addWidget(self.related_frame)

        self.description = QTextEdit(Form)
        self.description.setObjectName(u"description")
        self.description.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy1)
        self.description.setFocusPolicy(Qt.ClickFocus)
        self.description.setUndoRedoEnabled(True)
        self.description.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.description)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.chapters = QListWidget(Form)
        self.chapters.setObjectName(u"chapters")
        self.chapters.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.chapters)


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
        self.btn_shikimori.setText("")
        self.image.setText("")
        self.russian.setText(QCoreApplication.translate("Form", u"russian", None))
        self.name.setText(QCoreApplication.translate("Form", u"name", None))
        self.rate.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433:", None))
        self.star_1.setText("")
        self.star_2.setText("")
        self.star_3.setText("")
        self.star_4.setText("")
        self.star_5.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0435:", None))
    # retranslateUi

