# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import nlight_res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(543, 464)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_frame = QFrame(Form)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.back_btn = QPushButton(self.header_frame)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.back_btn)

        self.horizontalSpacer_2 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lib_frame = QFrame(self.header_frame)
        self.lib_frame.setObjectName(u"lib_frame")
        self.lib_frame.setFrameShape(QFrame.StyledPanel)
        self.lib_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.lib_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.lib_list_box = QComboBox(self.lib_frame)
        self.lib_list_box.setObjectName(u"lib_list_box")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lib_list_box.sizePolicy().hasHeightForWidth())
        self.lib_list_box.setSizePolicy(sizePolicy)
        self.lib_list_box.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.lib_list_box)

        self.add_btn = QPushButton(self.lib_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.add_btn)


        self.verticalLayout_7.addWidget(self.lib_frame)

        self.shikimori_frame = QFrame(self.header_frame)
        self.shikimori_frame.setObjectName(u"shikimori_frame")
        self.shikimori_frame.setFrameShape(QFrame.StyledPanel)
        self.shikimori_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.shikimori_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.shikimori_btn = QPushButton(self.shikimori_frame)
        self.shikimori_btn.setObjectName(u"shikimori_btn")
        self.shikimori_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.shikimori_btn)


        self.verticalLayout_7.addWidget(self.shikimori_frame)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addWidget(self.header_frame)

        self.manga_layout = QVBoxLayout()
        self.manga_layout.setObjectName(u"manga_layout")
        self.info_layout = QHBoxLayout()
        self.info_layout.setObjectName(u"info_layout")
        self.image_frame = QFrame(Form)
        self.image_frame.setObjectName(u"image_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_frame.sizePolicy().hasHeightForWidth())
        self.image_frame.setSizePolicy(sizePolicy1)
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.image_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.image = QLabel(self.image_frame)
        self.image.setObjectName(u"image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy2)
        self.image.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.image)


        self.info_layout.addWidget(self.image_frame)

        self.title_frame = QFrame(Form)
        self.title_frame.setObjectName(u"title_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy3)
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.title_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.name_label = QLabel(self.title_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.name_label)

        self.russian_label = QLabel(self.title_frame)
        self.russian_label.setObjectName(u"russian_label")
        self.russian_label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.russian_label)

        self.status_label = QLabel(self.title_frame)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout_5.addWidget(self.status_label)

        self.catalog_score_label = QLabel(self.title_frame)
        self.catalog_score_label.setObjectName(u"catalog_score_label")

        self.verticalLayout_5.addWidget(self.catalog_score_label)

        self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.volumes_label = QLabel(self.title_frame)
        self.volumes_label.setObjectName(u"volumes_label")

        self.verticalLayout_5.addWidget(self.volumes_label)

        self.chapters_label = QLabel(self.title_frame)
        self.chapters_label.setObjectName(u"chapters_label")

        self.verticalLayout_5.addWidget(self.chapters_label)


        self.info_layout.addWidget(self.title_frame)


        self.manga_layout.addLayout(self.info_layout)

        self.related_layout = QHBoxLayout()
        self.related_layout.setObjectName(u"related_layout")
        self.related_frame = QFrame(Form)
        self.related_frame.setObjectName(u"related_frame")
        self.related_frame.setFrameShape(QFrame.StyledPanel)
        self.related_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.related_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.related_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.related_list = QListWidget(self.related_frame)
        self.related_list.setObjectName(u"related_list")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.related_list.sizePolicy().hasHeightForWidth())
        self.related_list.setSizePolicy(sizePolicy4)
        self.related_list.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.related_list)


        self.related_layout.addWidget(self.related_frame)

        self.characters_frame = QFrame(Form)
        self.characters_frame.setObjectName(u"characters_frame")
        sizePolicy2.setHeightForWidth(self.characters_frame.sizePolicy().hasHeightForWidth())
        self.characters_frame.setSizePolicy(sizePolicy2)
        self.characters_frame.setMinimumSize(QSize(0, 0))
        self.characters_frame.setFrameShape(QFrame.StyledPanel)
        self.characters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.characters_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.characters_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)

        self.characters_list = QListWidget(self.characters_frame)
        self.characters_list.setObjectName(u"characters_list")

        self.verticalLayout_11.addWidget(self.characters_list)


        self.related_layout.addWidget(self.characters_frame)


        self.manga_layout.addLayout(self.related_layout)

        self.description_frame = QFrame(Form)
        self.description_frame.setObjectName(u"description_frame")
        self.description_frame.setFrameShape(QFrame.StyledPanel)
        self.description_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.description_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.description_text = QTextBrowser(self.description_frame)
        self.description_text.setObjectName(u"description_text")
        self.description_text.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_3.addWidget(self.description_text)


        self.manga_layout.addWidget(self.description_frame)


        self.verticalLayout_10.addLayout(self.manga_layout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.items_frame = QFrame(Form)
        self.items_frame.setObjectName(u"items_frame")
        self.items_frame.setFrameShape(QFrame.StyledPanel)
        self.items_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.items_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.items_tree = QTreeWidget(self.items_frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.items_tree.setHeaderItem(__qtreewidgetitem)
        self.items_tree.setObjectName(u"items_tree")
        self.items_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.items_tree.setHeaderHidden(True)
        self.items_tree.header().setVisible(False)

        self.verticalLayout.addWidget(self.items_tree)


        self.horizontalLayout_4.addWidget(self.items_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.back_btn.setText("")
        self.add_btn.setText("")
        self.shikimori_btn.setText("")
        self.image.setText("")
        self.name_label.setText(QCoreApplication.translate("Form", u"name", None))
        self.russian_label.setText(QCoreApplication.translate("Form", u"russian", None))
        self.status_label.setText(QCoreApplication.translate("Form", u"status", None))
        self.catalog_score_label.setText(QCoreApplication.translate("Form", u"score", None))
        self.volumes_label.setText(QCoreApplication.translate("Form", u"volumes", None))
        self.chapters_label.setText(QCoreApplication.translate("Form", u"chapters", None))
        self.label.setText(QCoreApplication.translate("Form", u"Related", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Characters", None))
        pass
    # retranslateUi

