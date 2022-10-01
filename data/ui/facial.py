# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facial.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import desu_res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(617, 494)
        Form.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.search = QVBoxLayout()
        self.search.setObjectName(u"search")
        self.items_frame = QFrame(Form)
        self.items_frame.setObjectName(u"items_frame")
        self.items_frame.setFrameShape(QFrame.StyledPanel)
        self.items_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.items_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.items_list = QListWidget(self.items_frame)
        self.items_list.setObjectName(u"items_list")
        self.items_list.setProperty("isWrapping", False)
        self.items_list.setWordWrap(True)

        self.verticalLayout.addWidget(self.items_list)


        self.search.addWidget(self.items_frame)

        self.search_frame = QFrame(Form)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.text_frame = QFrame(self.search_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.text_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_line = QLineEdit(self.text_frame)
        self.title_line.setObjectName(u"title_line")

        self.horizontalLayout_2.addWidget(self.title_line)

        self.search_btn = QPushButton(self.text_frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/data/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.search_btn)


        self.horizontalLayout_3.addWidget(self.text_frame)

        self.page_frame = QFrame(self.search_frame)
        self.page_frame.setObjectName(u"page_frame")
        self.page_frame.setFrameShape(QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.page_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prev_btn = QPushButton(self.page_frame)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/data/icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.prev_btn)

        self.page_label = QLabel(self.page_frame)
        self.page_label.setObjectName(u"page_label")

        self.horizontalLayout.addWidget(self.page_label)

        self.next_btn = QPushButton(self.page_frame)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/data/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.next_btn)


        self.horizontalLayout_3.addWidget(self.page_frame)


        self.search.addWidget(self.search_frame)


        self.horizontalLayout_5.addLayout(self.search)

        self.catalogs_frame = QFrame(Form)
        self.catalogs_frame.setObjectName(u"catalogs_frame")
        self.catalogs_frame.setFrameShape(QFrame.StyledPanel)
        self.catalogs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.catalogs_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.catalogs_list = QListWidget(self.catalogs_frame)
        self.catalogs_list.setObjectName(u"catalogs_list")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalogs_list.sizePolicy().hasHeightForWidth())
        self.catalogs_list.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.catalogs_list)


        self.horizontalLayout_5.addWidget(self.catalogs_frame)

        self.filters = QVBoxLayout()
        self.filters.setObjectName(u"filters")
        self.orders_frame = QFrame(Form)
        self.orders_frame.setObjectName(u"orders_frame")
        self.orders_frame.setStyleSheet(u"QAbstractButton {\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.orders_frame.setFrameShape(QFrame.StyledPanel)
        self.orders_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.orders_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.orders_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.orders_grid = QGridLayout()
        self.orders_grid.setObjectName(u"orders_grid")

        self.verticalLayout_5.addLayout(self.orders_grid)


        self.filters.addWidget(self.orders_frame)

        self.kinds_frame = QFrame(Form)
        self.kinds_frame.setObjectName(u"kinds_frame")
        self.kinds_frame.setStyleSheet(u"QAbstractButton {\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.kinds_frame.setFrameShape(QFrame.StyledPanel)
        self.kinds_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.kinds_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.kinds_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.kinds_grid = QGridLayout()
        self.kinds_grid.setObjectName(u"kinds_grid")

        self.verticalLayout_4.addLayout(self.kinds_grid)


        self.filters.addWidget(self.kinds_frame)

        self.genres_frame = QFrame(Form)
        self.genres_frame.setObjectName(u"genres_frame")
        self.genres_frame.setFrameShape(QFrame.StyledPanel)
        self.genres_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.genres_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.genres_btn = QPushButton(self.genres_frame)
        self.genres_btn.setObjectName(u"genres_btn")
        self.genres_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.genres_btn)


        self.filters.addWidget(self.genres_frame)

        self.filter_catalog_frame = QFrame(Form)
        self.filter_catalog_frame.setObjectName(u"filter_catalog_frame")
        self.filter_catalog_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_catalog_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.filter_catalog_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.catalogs_btn = QPushButton(self.filter_catalog_frame)
        self.catalogs_btn.setObjectName(u"catalogs_btn")
        self.catalogs_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.catalogs_btn)


        self.filters.addWidget(self.filter_catalog_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.filters.addItem(self.verticalSpacer)

        self.filter_actions_frame = QFrame(Form)
        self.filter_actions_frame.setObjectName(u"filter_actions_frame")
        self.filter_actions_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.filter_actions_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.reset_btn = QPushButton(self.filter_actions_frame)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.reset_btn)

        self.apply_btn = QPushButton(self.filter_actions_frame)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.apply_btn)


        self.filters.addWidget(self.filter_actions_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addLayout(self.filters)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_btn.setText("")
        self.prev_btn.setText("")
        self.page_label.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f", None))
        self.genres_btn.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0436\u0430\u043d\u0440\u043e\u0432", None))
        self.catalogs_btn.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.apply_btn.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

