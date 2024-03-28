# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infojOTtZx.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListWidgetItem, QSizePolicy, QSpacerItem,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, ElevatedCardWidget,
    ListWidget, SimpleCardWidget, TextEdit, ToolButton,
    TreeWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(736, 531)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_frame = SimpleCardWidget(Form)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_2 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lib_frame = SimpleCardWidget(self.header_frame)
        self.lib_frame.setObjectName(u"lib_frame")
        self.lib_frame.setFrameShape(QFrame.StyledPanel)
        self.lib_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.lib_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lib_list_box = ComboBox(self.lib_frame)
        self.lib_list_box.setObjectName(u"lib_list_box")

        self.horizontalLayout.addWidget(self.lib_list_box)

        self.add_btn = ToolButton(self.lib_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.add_btn)


        self.verticalLayout_7.addWidget(self.lib_frame)

        self.shikimori_frame = SimpleCardWidget(self.header_frame)
        self.shikimori_frame.setObjectName(u"shikimori_frame")
        self.shikimori_frame.setFrameShape(QFrame.StyledPanel)
        self.shikimori_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.shikimori_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.shikimori_btn = ToolButton(self.shikimori_frame)
        self.shikimori_btn.setObjectName(u"shikimori_btn")

        self.horizontalLayout_2.addWidget(self.shikimori_btn)


        self.verticalLayout_7.addWidget(self.shikimori_frame)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addWidget(self.header_frame)

        self.manga_layout = QVBoxLayout()
        self.manga_layout.setObjectName(u"manga_layout")
        self.info_layout = QHBoxLayout()
        self.info_layout.setObjectName(u"info_layout")
        self.image_frame = SimpleCardWidget(Form)
        self.image_frame.setObjectName(u"image_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_frame.sizePolicy().hasHeightForWidth())
        self.image_frame.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.image_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.image = QLabel(self.image_frame)
        self.image.setObjectName(u"image")
        self.image.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.image)


        self.info_layout.addWidget(self.image_frame)

        self.title_frame = SimpleCardWidget(Form)
        self.title_frame.setObjectName(u"title_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.title_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.name_label = BodyLabel(self.title_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.name_label)

        self.russian_label = BodyLabel(self.title_frame)
        self.russian_label.setObjectName(u"russian_label")

        self.verticalLayout_8.addWidget(self.russian_label)

        self.status_label = BodyLabel(self.title_frame)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout_8.addWidget(self.status_label)

        self.catalog_score_label = BodyLabel(self.title_frame)
        self.catalog_score_label.setObjectName(u"catalog_score_label")

        self.verticalLayout_8.addWidget(self.catalog_score_label)

        self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.volumes_label = BodyLabel(self.title_frame)
        self.volumes_label.setObjectName(u"volumes_label")

        self.verticalLayout_8.addWidget(self.volumes_label)

        self.chapters_label = BodyLabel(self.title_frame)
        self.chapters_label.setObjectName(u"chapters_label")

        self.verticalLayout_8.addWidget(self.chapters_label)


        self.info_layout.addWidget(self.title_frame)


        self.manga_layout.addLayout(self.info_layout)

        self.related_layout = QHBoxLayout()
        self.related_layout.setObjectName(u"related_layout")
        self.related_frame = ElevatedCardWidget(Form)
        self.related_frame.setObjectName(u"related_frame")
        self.verticalLayout_4 = QVBoxLayout(self.related_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = BodyLabel(self.related_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.related_list = ListWidget(self.related_frame)
        self.related_list.setObjectName(u"related_list")
        self.related_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.related_list.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.related_list)


        self.related_layout.addWidget(self.related_frame)

        self.characters_frame = ElevatedCardWidget(Form)
        self.characters_frame.setObjectName(u"characters_frame")
        self.verticalLayout_2 = QVBoxLayout(self.characters_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = BodyLabel(self.characters_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.characters_list = ListWidget(self.characters_frame)
        self.characters_list.setObjectName(u"characters_list")
        self.characters_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.characters_list.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.characters_list)


        self.related_layout.addWidget(self.characters_frame)


        self.manga_layout.addLayout(self.related_layout)

        self.description_frame = SimpleCardWidget(Form)
        self.description_frame.setObjectName(u"description_frame")
        self.verticalLayout_3 = QVBoxLayout(self.description_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.description_text = TextEdit(self.description_frame)
        self.description_text.setObjectName(u"description_text")
        self.description_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.description_text.setUndoRedoEnabled(False)
        self.description_text.setReadOnly(True)
        self.description_text.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_3.addWidget(self.description_text)


        self.manga_layout.addWidget(self.description_frame)


        self.verticalLayout_10.addLayout(self.manga_layout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.items_frame = ElevatedCardWidget(Form)
        self.items_frame.setObjectName(u"items_frame")
        self.verticalLayout_5 = QVBoxLayout(self.items_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.items_tree = TreeWidget(self.items_frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.items_tree.setHeaderItem(__qtreewidgetitem)
        self.items_tree.setObjectName(u"items_tree")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.items_tree.sizePolicy().hasHeightForWidth())
        self.items_tree.setSizePolicy(sizePolicy2)
        self.items_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.items_tree.header().setVisible(False)

        self.verticalLayout_5.addWidget(self.items_tree)


        self.horizontalLayout_4.addWidget(self.items_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
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

