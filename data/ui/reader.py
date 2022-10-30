# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reader.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
        MainWindow.resize(342, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(32, 32, 32);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
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
"}\n"
"QScrollBar:horizontal {\n"
"    height: 14px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width: 14"
                        "px;\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.size_frame = QFrame(self.centralwidget)
        self.size_frame.setObjectName(u"size_frame")
        self.size_frame.setFrameShape(QFrame.StyledPanel)
        self.size_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.size_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_size_slider = QSlider(self.size_frame)
        self.text_size_slider.setObjectName(u"text_size_slider")
        self.text_size_slider.setEnabled(True)
        self.text_size_slider.setFocusPolicy(Qt.NoFocus)
        self.text_size_slider.setMinimum(9)
        self.text_size_slider.setMaximum(25)
        self.text_size_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.text_size_slider)


        self.verticalLayout_2.addWidget(self.size_frame)

        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.content_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 306, 436))
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
        self.img.setOpenExternalLinks(False)

        self.verticalLayout_5.addWidget(self.img)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.content_frame)

        self.actions_frame = QFrame(self.centralwidget)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.actions_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.page_actions_btn = QHBoxLayout()
        self.page_actions_btn.setObjectName(u"page_actions_btn")
        self.prev_page_btn = QPushButton(self.actions_frame)
        self.prev_page_btn.setObjectName(u"prev_page_btn")
        self.prev_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_page_btn.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/data/icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_page_btn.setIcon(icon)

        self.page_actions_btn.addWidget(self.prev_page_btn)

        self.page_label = QLabel(self.actions_frame)
        self.page_label.setObjectName(u"page_label")

        self.page_actions_btn.addWidget(self.page_label)

        self.next_page_btn = QPushButton(self.actions_frame)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_page_btn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/data/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_page_btn.setIcon(icon1)

        self.page_actions_btn.addWidget(self.next_page_btn)


        self.verticalLayout.addLayout(self.page_actions_btn)

        self.chapter_actions_label = QHBoxLayout()
        self.chapter_actions_label.setObjectName(u"chapter_actions_label")
        self.prev_chapter_btn = QPushButton(self.actions_frame)
        self.prev_chapter_btn.setObjectName(u"prev_chapter_btn")
        self.prev_chapter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_chapter_btn.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/data/icons/double_prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_chapter_btn.setIcon(icon2)

        self.chapter_actions_label.addWidget(self.prev_chapter_btn)

        self.chapter_label = QLabel(self.actions_frame)
        self.chapter_label.setObjectName(u"chapter_label")

        self.chapter_actions_label.addWidget(self.chapter_label)

        self.next_chapter_btn = QPushButton(self.actions_frame)
        self.next_chapter_btn.setObjectName(u"next_chapter_btn")
        self.next_chapter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_chapter_btn.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/icons/data/icons/double_next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_chapter_btn.setIcon(icon3)

        self.chapter_actions_label.addWidget(self.next_chapter_btn)

        self.fullscreen_btn = QPushButton(self.actions_frame)
        self.fullscreen_btn.setObjectName(u"fullscreen_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullscreen_btn.sizePolicy().hasHeightForWidth())
        self.fullscreen_btn.setSizePolicy(sizePolicy)
        self.fullscreen_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen_btn.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/icons/data/icons/fullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_btn.setIcon(icon4)

        self.chapter_actions_label.addWidget(self.fullscreen_btn)


        self.verticalLayout.addLayout(self.chapter_actions_label)


        self.verticalLayout_2.addWidget(self.actions_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img.setText("")
        self.prev_page_btn.setText("")
#if QT_CONFIG(shortcut)
        self.prev_page_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page_btn.setText("")
#if QT_CONFIG(shortcut)
        self.next_page_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.prev_chapter_btn.setText("")
#if QT_CONFIG(shortcut)
        self.prev_chapter_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.chapter_label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u0430 1", None))
        self.next_chapter_btn.setText("")
#if QT_CONFIG(shortcut)
        self.next_chapter_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.fullscreen_btn.setText("")
#if QT_CONFIG(shortcut)
        self.fullscreen_btn.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

