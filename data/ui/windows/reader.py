# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reader.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import nlight_res_rc

class Ui_ReaderWindow(object):
    def setupUi(self, ReaderWindow):
        if not ReaderWindow.objectName():
            ReaderWindow.setObjectName(u"ReaderWindow")
        ReaderWindow.resize(489, 600)
        ReaderWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(ReaderWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.text_reader = QWidget(self.centralwidget)
        self.text_reader.setObjectName(u"text_reader")
        self.verticalLayout_2 = QVBoxLayout(self.text_reader)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.size_frame = QFrame(self.text_reader)
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

        self.content_frame = QFrame(self.text_reader)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.content_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.text = QTextBrowser(self.content_frame)
        self.text.setObjectName(u"text")
        self.text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text.setAutoFormatting(QTextEdit.AutoNone)
        self.text.setAcceptRichText(True)
        self.text.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_6.addWidget(self.text)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.verticalLayout_4.addWidget(self.text_reader)

        self.image_reader = QFrame(self.centralwidget)
        self.image_reader.setObjectName(u"image_reader")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_reader.sizePolicy().hasHeightForWidth())
        self.image_reader.setSizePolicy(sizePolicy)
        self.image_reader.setFrameShape(QFrame.StyledPanel)
        self.image_reader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.image_reader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.image_reader)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 449, 200))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.img = QLabel(self.scrollAreaWidgetContents)
        self.img.setObjectName(u"img")
        self.img.setStyleSheet(u"")
        self.img.setAlignment(Qt.AlignCenter)
        self.img.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_5.addWidget(self.img)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.image_reader)

        self.actions_layout = QHBoxLayout()
        self.actions_layout.setObjectName(u"actions_layout")
        self.actions_frame = QFrame(self.centralwidget)
        self.actions_frame.setObjectName(u"actions_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.actions_frame.sizePolicy().hasHeightForWidth())
        self.actions_frame.setSizePolicy(sizePolicy1)
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

        self.page_actions_btn.addWidget(self.prev_page_btn)

        self.page_label = QLabel(self.actions_frame)
        self.page_label.setObjectName(u"page_label")

        self.page_actions_btn.addWidget(self.page_label)

        self.next_page_btn = QPushButton(self.actions_frame)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_page_btn.setFocusPolicy(Qt.NoFocus)

        self.page_actions_btn.addWidget(self.next_page_btn)


        self.verticalLayout.addLayout(self.page_actions_btn)

        self.chapter_actions_label = QHBoxLayout()
        self.chapter_actions_label.setObjectName(u"chapter_actions_label")
        self.prev_chapter_btn = QPushButton(self.actions_frame)
        self.prev_chapter_btn.setObjectName(u"prev_chapter_btn")
        self.prev_chapter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_chapter_btn.setFocusPolicy(Qt.NoFocus)

        self.chapter_actions_label.addWidget(self.prev_chapter_btn)

        self.chapter_label = QLabel(self.actions_frame)
        self.chapter_label.setObjectName(u"chapter_label")

        self.chapter_actions_label.addWidget(self.chapter_label)

        self.next_chapter_btn = QPushButton(self.actions_frame)
        self.next_chapter_btn.setObjectName(u"next_chapter_btn")
        self.next_chapter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_chapter_btn.setFocusPolicy(Qt.NoFocus)

        self.chapter_actions_label.addWidget(self.next_chapter_btn)


        self.verticalLayout.addLayout(self.chapter_actions_label)


        self.actions_layout.addWidget(self.actions_frame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.fullscreen_btn = QPushButton(self.frame)
        self.fullscreen_btn.setObjectName(u"fullscreen_btn")
        self.fullscreen_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen_btn.setFocusPolicy(Qt.NoFocus)
        self.fullscreen_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.fullscreen_btn)


        self.actions_layout.addWidget(self.frame)


        self.verticalLayout_4.addLayout(self.actions_layout)

        ReaderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReaderWindow)

        QMetaObject.connectSlotsByName(ReaderWindow)
    # setupUi

    def retranslateUi(self, ReaderWindow):
        ReaderWindow.setWindowTitle(QCoreApplication.translate("ReaderWindow", u"MainWindow", None))
        self.prev_page_btn.setText("")
#if QT_CONFIG(shortcut)
        self.prev_page_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.page_label.setText(QCoreApplication.translate("ReaderWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page_btn.setText("")
#if QT_CONFIG(shortcut)
        self.next_page_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.prev_chapter_btn.setText("")
#if QT_CONFIG(shortcut)
        self.prev_chapter_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.chapter_label.setText(QCoreApplication.translate("ReaderWindow", u"\u0413\u043b\u0430\u0432\u0430 1", None))
        self.next_chapter_btn.setText("")
#if QT_CONFIG(shortcut)
        self.next_chapter_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.fullscreen_btn.setText("")
#if QT_CONFIG(shortcut)
        self.fullscreen_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

