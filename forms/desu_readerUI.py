# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_readerUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)
import desu_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.slider_frame = QFrame(self.centralwidget)
        self.slider_frame.setObjectName(u"slider_frame")
        self.slider_frame.setFrameShape(QFrame.StyledPanel)
        self.slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.slider_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_size_slider = QSlider(self.slider_frame)
        self.text_size_slider.setObjectName(u"text_size_slider")
        self.text_size_slider.setEnabled(True)
        self.text_size_slider.setFocusPolicy(Qt.NoFocus)
        self.text_size_slider.setMinimum(9)
        self.text_size_slider.setMaximum(25)
        self.text_size_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.text_size_slider)


        self.verticalLayout_2.addWidget(self.slider_frame)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 502, 454))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(32, 32, 32);")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.img = QLabel(self.scrollAreaWidgetContents)
        self.img.setObjectName(u"img")
        self.img.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.img.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.img.setWordWrap(True)
        self.img.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.img)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.actions_frame = QFrame(self.centralwidget)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.actions_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_page = QPushButton(self.actions_frame)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setEnabled(True)
        self.prev_page.setFocusPolicy(Qt.NoFocus)
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon = QIcon()
        icon.addFile(u":/icons/images/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_page.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.prev_page)

        self.lbl_page = QLabel(self.actions_frame)
        self.lbl_page.setObjectName(u"lbl_page")

        self.horizontalLayout_3.addWidget(self.lbl_page)

        self.next_page = QPushButton(self.actions_frame)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setFocusPolicy(Qt.NoFocus)
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_page.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.next_page)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prev_chp = QPushButton(self.actions_frame)
        self.prev_chp.setObjectName(u"prev_chp")
        self.prev_chp.setFocusPolicy(Qt.NoFocus)
        self.prev_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/double_prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_chp.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.prev_chp)

        self.lbl_chp = QLabel(self.actions_frame)
        self.lbl_chp.setObjectName(u"lbl_chp")

        self.horizontalLayout_2.addWidget(self.lbl_chp)

        self.next_chp = QPushButton(self.actions_frame)
        self.next_chp.setObjectName(u"next_chp")
        self.next_chp.setFocusPolicy(Qt.NoFocus)
        self.next_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/double_next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_chp.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.next_chp)

        self.btn_fullscreen = QPushButton(self.actions_frame)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fullscreen.sizePolicy().hasHeightForWidth())
        self.btn_fullscreen.setSizePolicy(sizePolicy)
        self.btn_fullscreen.setFocusPolicy(Qt.NoFocus)
        self.btn_fullscreen.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/fullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fullscreen.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_fullscreen)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.actions_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img.setText("")
        self.prev_page.setText("")
        self.lbl_page.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page.setText("")
        self.prev_chp.setText("")
        self.lbl_chp.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u0430 1", None))
        self.next_chp.setText("")
        self.btn_fullscreen.setText("")
    # retranslateUi

