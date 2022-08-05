# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desuUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(498, 364)
        Dialog.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QDialog{\n"
"	background-color: rgb(32, 32, 32);\n"
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
"}")
        self.horizontalLayout_4 = QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.items_frame = QFrame(Dialog)
        self.items_frame.setObjectName(u"items_frame")
        self.items_frame.setFrameShape(QFrame.StyledPanel)
        self.items_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.items_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.list_manga = QListWidget(self.items_frame)
        self.list_manga.setObjectName(u"list_manga")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 133, 52, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.list_manga.setPalette(palette)
        self.list_manga.setAutoFillBackground(False)
        self.list_manga.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.list_manga)


        self.verticalLayout_3.addWidget(self.items_frame)

        self.search_frame = QFrame(Dialog)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.text_frame = QFrame(self.search_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.text_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_search = QLineEdit(self.text_frame)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.line_search)

        self.btn_search = QPushButton(self.text_frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon = QIcon()
        icon.addFile(u"images/search.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_search.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_search)


        self.horizontalLayout_3.addWidget(self.text_frame)

        self.page_frame = QFrame(self.search_frame)
        self.page_frame.setObjectName(u"page_frame")
        self.page_frame.setFrameShape(QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.page_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prev_page = QPushButton(self.page_frame)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon1 = QIcon()
        icon1.addFile(u"images/prev.png", QSize(), QIcon.Normal, QIcon.On)
        self.prev_page.setIcon(icon1)

        self.horizontalLayout.addWidget(self.prev_page)

        self.label_page = QLabel(self.page_frame)
        self.label_page.setObjectName(u"label_page")

        self.horizontalLayout.addWidget(self.label_page)

        self.next_page = QPushButton(self.page_frame)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon2 = QIcon()
        icon2.addFile(u"images/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.next_page.setIcon(icon2)

        self.horizontalLayout.addWidget(self.next_page)


        self.horizontalLayout_3.addWidget(self.page_frame)


        self.verticalLayout_3.addWidget(self.search_frame)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.catalogs_frame = QFrame(Dialog)
        self.catalogs_frame.setObjectName(u"catalogs_frame")
        self.catalogs_frame.setFrameShape(QFrame.StyledPanel)
        self.catalogs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.catalogs_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.catalog_list = QListWidget(self.catalogs_frame)
        self.catalog_list.setObjectName(u"catalog_list")
        self.catalog_list.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalog_list.sizePolicy().hasHeightForWidth())
        self.catalog_list.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(240, 240, 240, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 120, 215, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.catalog_list.setPalette(palette1)

        self.verticalLayout_8.addWidget(self.catalog_list)


        self.horizontalLayout_4.addWidget(self.catalogs_frame)

        self.filters_frame = QFrame(Dialog)
        self.filters_frame.setObjectName(u"filters_frame")
        self.filters_frame.setStyleSheet(u"QWidget {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.filters_frame.setFrameShape(QFrame.StyledPanel)
        self.filters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.filters_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.order_frame = QFrame(self.filters_frame)
        self.order_frame.setObjectName(u"order_frame")
        self.order_frame.setFrameShape(QFrame.StyledPanel)
        self.order_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.order_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_sort = QLabel(self.order_frame)
        self.label_sort.setObjectName(u"label_sort")

        self.verticalLayout_2.addWidget(self.label_sort)

        self.order_grid = QGridLayout()
        self.order_grid.setObjectName(u"order_grid")

        self.verticalLayout_2.addLayout(self.order_grid)


        self.verticalLayout.addWidget(self.order_frame)

        self.kind_frame = QFrame(self.filters_frame)
        self.kind_frame.setObjectName(u"kind_frame")
        self.kind_frame.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QDialog{\n"
"	background-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"QAbstractButton{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.kind_frame.setFrameShape(QFrame.StyledPanel)
        self.kind_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.kind_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_type = QLabel(self.kind_frame)
        self.label_type.setObjectName(u"label_type")

        self.verticalLayout_4.addWidget(self.label_type)

        self.kind_grid = QGridLayout()
        self.kind_grid.setObjectName(u"kind_grid")

        self.verticalLayout_4.addLayout(self.kind_grid)


        self.verticalLayout.addWidget(self.kind_frame)

        self.genres_frame = QFrame(self.filters_frame)
        self.genres_frame.setObjectName(u"genres_frame")
        self.genres_frame.setFrameShape(QFrame.StyledPanel)
        self.genres_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.genres_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_genre = QLabel(self.genres_frame)
        self.label_genre.setObjectName(u"label_genre")

        self.verticalLayout_5.addWidget(self.label_genre)

        self.btn_genres_list = QPushButton(self.genres_frame)
        self.btn_genres_list.setObjectName(u"btn_genres_list")
        self.btn_genres_list.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.verticalLayout_5.addWidget(self.btn_genres_list)


        self.verticalLayout.addWidget(self.genres_frame)

        self.filter_catalogs_frame = QFrame(self.filters_frame)
        self.filter_catalogs_frame.setObjectName(u"filter_catalogs_frame")
        self.filter_catalogs_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_catalogs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.filter_catalogs_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_catalogs = QPushButton(self.filter_catalogs_frame)
        self.btn_catalogs.setObjectName(u"btn_catalogs")
        self.btn_catalogs.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.verticalLayout_7.addWidget(self.btn_catalogs)


        self.verticalLayout.addWidget(self.filter_catalogs_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.actions_frame = QFrame(self.filters_frame)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setStyleSheet(u"")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.actions_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.filter_reset = QPushButton(self.actions_frame)
        self.filter_reset.setObjectName(u"filter_reset")
        self.filter_reset.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_5.addWidget(self.filter_reset)

        self.filter_apply = QPushButton(self.actions_frame)
        self.filter_apply.setObjectName(u"filter_apply")
        self.filter_apply.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.horizontalLayout_5.addWidget(self.filter_apply)


        self.verticalLayout.addWidget(self.actions_frame)


        self.horizontalLayout_4.addWidget(self.filters_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_search.setText("")
        self.prev_page.setText("")
        self.label_page.setText(QCoreApplication.translate("Dialog", u" \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page.setText("")
        self.label_sort.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.label_type.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.label_genre.setText(QCoreApplication.translate("Dialog", u"\u0416\u0430\u043d\u0440", None))
        self.btn_genres_list.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0436\u0430\u043d\u0440\u043e\u0432", None))
        self.btn_catalogs.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438", None))
        self.filter_reset.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.filter_apply.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

