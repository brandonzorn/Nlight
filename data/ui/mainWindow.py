# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import desu_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(669, 384)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 32, 32);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_menu_widget = QWidget(self.centralwidget)
        self.side_menu_widget.setObjectName(u"side_menu_widget")
        self.side_menu_widget.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QPushButton {\n"
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
        self.frame = QFrame(self.side_menu_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_library = QPushButton(self.frame)
        self.btn_library.setObjectName(u"btn_library")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_library.sizePolicy().hasHeightForWidth())
        self.btn_library.setSizePolicy(sizePolicy)
        self.btn_library.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_library.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/data/icons/library.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/data/icons/library_filled.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_library.setIcon(icon)
        self.btn_library.setCheckable(True)
        self.btn_library.setAutoRepeat(False)
        self.btn_library.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_library)

        self.btn_main = QPushButton(self.frame)
        self.btn_main.setObjectName(u"btn_main")
        sizePolicy.setHeightForWidth(self.btn_main.sizePolicy().hasHeightForWidth())
        self.btn_main.setSizePolicy(sizePolicy)
        self.btn_main.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_main.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/data/icons/main.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/data/icons/main_filled.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main.setIcon(icon1)
        self.btn_main.setCheckable(True)
        self.btn_main.setChecked(True)
        self.btn_main.setAutoRepeat(False)
        self.btn_main.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_main)

        self.btn_shikimori = QPushButton(self.frame)
        self.btn_shikimori.setObjectName(u"btn_shikimori")
        sizePolicy.setHeightForWidth(self.btn_shikimori.sizePolicy().hasHeightForWidth())
        self.btn_shikimori.setSizePolicy(sizePolicy)
        self.btn_shikimori.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_shikimori.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/data/icons/shikimori.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_shikimori.setIcon(icon2)
        self.btn_shikimori.setCheckable(True)
        self.btn_shikimori.setAutoRepeat(False)
        self.btn_shikimori.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_shikimori)

        self.btn_history = QPushButton(self.frame)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/data/icons/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_history.setIcon(icon3)
        self.btn_history.setCheckable(True)
        self.btn_history.setAutoRepeat(False)
        self.btn_history.setAutoExclusive(True)
        self.btn_history.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.btn_history)

        self.verticalSpacer = QSpacerItem(17, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.side_menu_widget)

        self.top_item_widget = QWidget(self.centralwidget)
        self.top_item_widget.setObjectName(u"top_item_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_item_widget.sizePolicy().hasHeightForWidth())
        self.top_item_widget.setSizePolicy(sizePolicy1)
        palette = QPalette()
        self.top_item_widget.setPalette(palette)
        self.top_item_widget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.top_item_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_item = QStackedWidget(self.top_item_widget)
        self.top_item.setObjectName(u"top_item")
        self.top_item.setStyleSheet(u"QComboBox {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 133, 52);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
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
"}\n"
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
"    background: rgba(143.000, 145.000, 1"
                        "45.000, 0.933);\n"
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

        self.verticalLayout_2.addWidget(self.top_item)


        self.horizontalLayout.addWidget(self.top_item_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.top_item.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_library.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430", None))
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.btn_shikimori.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u043a\u0438\u043c\u043e\u0440\u0438", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
    # retranslateUi

