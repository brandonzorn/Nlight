# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reader.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import nlight_res_rc

class Ui_ReaderWindow(object):
    def setupUi(self, ReaderWindow):
        if not ReaderWindow.objectName():
            ReaderWindow.setObjectName(u"ReaderWindow")
        ReaderWindow.resize(704, 610)
        ReaderWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(ReaderWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.reader_widget = QWidget(self.widget)
        self.reader_widget.setObjectName(u"reader_widget")
        sizePolicy.setHeightForWidth(self.reader_widget.sizePolicy().hasHeightForWidth())
        self.reader_widget.setSizePolicy(sizePolicy)
        self.reader_layout = QHBoxLayout(self.reader_widget)
        self.reader_layout.setObjectName(u"reader_layout")
        self.reader_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.reader_widget)

        self.actions_layout = QHBoxLayout()
        self.actions_layout.setObjectName(u"actions_layout")
        self.actions_frame = QFrame(self.widget)
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
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.page_actions_btn.addItem(self.horizontalSpacer)

        self.prev_chapter_btn = QPushButton(self.actions_frame)
        self.prev_chapter_btn.setObjectName(u"prev_chapter_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.prev_chapter_btn.sizePolicy().hasHeightForWidth())
        self.prev_chapter_btn.setSizePolicy(sizePolicy2)
        self.prev_chapter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_chapter_btn.setFocusPolicy(Qt.NoFocus)

        self.page_actions_btn.addWidget(self.prev_chapter_btn)

        self.prev_page_btn = QPushButton(self.actions_frame)
        self.prev_page_btn.setObjectName(u"prev_page_btn")
        sizePolicy2.setHeightForWidth(self.prev_page_btn.sizePolicy().hasHeightForWidth())
        self.prev_page_btn.setSizePolicy(sizePolicy2)
        self.prev_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_page_btn.setFocusPolicy(Qt.NoFocus)

        self.page_actions_btn.addWidget(self.prev_page_btn)

        self.chapter_label = QLabel(self.actions_frame)
        self.chapter_label.setObjectName(u"chapter_label")
        self.chapter_label.setWordWrap(True)

        self.page_actions_btn.addWidget(self.chapter_label)

        self.page_label = QLabel(self.actions_frame)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setWordWrap(True)

        self.page_actions_btn.addWidget(self.page_label)

        self.next_page_btn = QPushButton(self.actions_frame)
        self.next_page_btn.setObjectName(u"next_page_btn")
        sizePolicy2.setHeightForWidth(self.next_page_btn.sizePolicy().hasHeightForWidth())
        self.next_page_btn.setSizePolicy(sizePolicy2)
        self.next_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_page_btn.setFocusPolicy(Qt.NoFocus)

        self.page_actions_btn.addWidget(self.next_page_btn)

        self.next_chapter_btn = QPushButton(self.actions_frame)
        self.next_chapter_btn.setObjectName(u"next_chapter_btn")
        sizePolicy2.setHeightForWidth(self.next_chapter_btn.sizePolicy().hasHeightForWidth())
        self.next_chapter_btn.setSizePolicy(sizePolicy2)
        self.next_chapter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_chapter_btn.setFocusPolicy(Qt.NoFocus)

        self.page_actions_btn.addWidget(self.next_chapter_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.page_actions_btn.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.page_actions_btn)


        self.actions_layout.addWidget(self.actions_frame)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fullscreen_btn = QPushButton(self.frame)
        self.fullscreen_btn.setObjectName(u"fullscreen_btn")
        sizePolicy2.setHeightForWidth(self.fullscreen_btn.sizePolicy().hasHeightForWidth())
        self.fullscreen_btn.setSizePolicy(sizePolicy2)
        self.fullscreen_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen_btn.setFocusPolicy(Qt.NoFocus)
        self.fullscreen_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.fullscreen_btn)

        self.ch_list_btn = QPushButton(self.frame)
        self.ch_list_btn.setObjectName(u"ch_list_btn")
        sizePolicy2.setHeightForWidth(self.ch_list_btn.sizePolicy().hasHeightForWidth())
        self.ch_list_btn.setSizePolicy(sizePolicy2)
        self.ch_list_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ch_list_btn.setFocusPolicy(Qt.NoFocus)
        self.ch_list_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.ch_list_btn)


        self.actions_layout.addWidget(self.frame)


        self.verticalLayout_3.addLayout(self.actions_layout)


        self.horizontalLayout_3.addWidget(self.widget)

        self.chapters_frame = QFrame(self.centralwidget)
        self.chapters_frame.setObjectName(u"chapters_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chapters_frame.sizePolicy().hasHeightForWidth())
        self.chapters_frame.setSizePolicy(sizePolicy3)
        self.chapters_frame.setFrameShape(QFrame.StyledPanel)
        self.chapters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.chapters_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.items_list = QListWidget(self.chapters_frame)
        self.items_list.setObjectName(u"items_list")
        self.items_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.items_list.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.items_list)


        self.horizontalLayout_3.addWidget(self.chapters_frame)

        ReaderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReaderWindow)

        QMetaObject.connectSlotsByName(ReaderWindow)
    # setupUi

    def retranslateUi(self, ReaderWindow):
        ReaderWindow.setWindowTitle(QCoreApplication.translate("ReaderWindow", u"MainWindow", None))
        self.prev_chapter_btn.setText("")
#if QT_CONFIG(shortcut)
        self.prev_chapter_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.prev_page_btn.setText("")
#if QT_CONFIG(shortcut)
        self.prev_page_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.chapter_label.setText(QCoreApplication.translate("ReaderWindow", u"\u0413\u043b\u0430\u0432\u0430 1", None))
        self.page_label.setText(QCoreApplication.translate("ReaderWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page_btn.setText("")
#if QT_CONFIG(shortcut)
        self.next_page_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.next_chapter_btn.setText("")
#if QT_CONFIG(shortcut)
        self.next_chapter_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.fullscreen_btn.setText("")
#if QT_CONFIG(shortcut)
        self.fullscreen_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.ch_list_btn.setText("")
#if QT_CONFIG(shortcut)
        self.ch_list_btn.setShortcut(QCoreApplication.translate("ReaderWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

