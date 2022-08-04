# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import desu_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(669, 472)
        MainWindow.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 32, 32);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_menu_widget = QWidget(self.centralwidget)
        self.side_menu_widget.setObjectName(u"side_menu_widget")
        self.side_menu_widget.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"	padding: 5px 1px;\n"
"    background: transparent;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	font-weight: bold;\n"
"	icon-size: 24px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	border-left: 3px solid green;\n"
"	background-color: gray;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border-left: 3px solid green;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.side_menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_mylist = QPushButton(self.side_menu_widget)
        self.btn_mylist.setObjectName(u"btn_mylist")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mylist.sizePolicy().hasHeightForWidth())
        self.btn_mylist.setSizePolicy(sizePolicy)
        self.btn_mylist.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mylist.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/library.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mylist.setIcon(icon)
        self.btn_mylist.setCheckable(True)
        self.btn_mylist.setAutoRepeat(False)
        self.btn_mylist.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_mylist)

        self.btn_main = QPushButton(self.side_menu_widget)
        self.btn_main.setObjectName(u"btn_main")
        sizePolicy.setHeightForWidth(self.btn_main.sizePolicy().hasHeightForWidth())
        self.btn_main.setSizePolicy(sizePolicy)
        self.btn_main.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_main.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/main.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main.setIcon(icon1)
        self.btn_main.setCheckable(True)
        self.btn_main.setChecked(True)
        self.btn_main.setAutoRepeat(False)
        self.btn_main.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_main)

        self.btn_shikimori = QPushButton(self.side_menu_widget)
        self.btn_shikimori.setObjectName(u"btn_shikimori")
        sizePolicy.setHeightForWidth(self.btn_shikimori.sizePolicy().hasHeightForWidth())
        self.btn_shikimori.setSizePolicy(sizePolicy)
        self.btn_shikimori.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_shikimori.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/shikimori.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_shikimori.setIcon(icon2)
        self.btn_shikimori.setCheckable(True)
        self.btn_shikimori.setAutoRepeat(False)
        self.btn_shikimori.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_shikimori)

        self.btn_history = QPushButton(self.side_menu_widget)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_history.setIcon(icon3)
        self.btn_history.setCheckable(True)
        self.btn_history.setAutoRepeat(False)
        self.btn_history.setAutoExclusive(True)
        self.btn_history.setAutoDefault(False)

        self.verticalLayout.addWidget(self.btn_history)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_settings = QPushButton(self.side_menu_widget)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon4)
        self.btn_settings.setCheckable(False)
        self.btn_settings.setAutoRepeat(False)
        self.btn_settings.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.btn_settings)


        self.horizontalLayout.addWidget(self.side_menu_widget, 0, Qt.AlignLeft)

        self.top_item_widget = QWidget(self.centralwidget)
        self.top_item_widget.setObjectName(u"top_item_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_item_widget.sizePolicy().hasHeightForWidth())
        self.top_item_widget.setSizePolicy(sizePolicy1)
        self.top_item_widget.setStyleSheet(u"QPushButton {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.top_item_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_item = QStackedWidget(self.top_item_widget)
        self.top_item.setObjectName(u"top_item")

        self.verticalLayout_2.addWidget(self.top_item)


        self.horizontalLayout.addWidget(self.top_item_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.top_item.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_mylist.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.btn_shikimori.setText(QCoreApplication.translate("MainWindow", u"Shikimori", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

