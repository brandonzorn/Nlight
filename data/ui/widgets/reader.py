# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reader.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidgetItem, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ListWidget, SimpleCardWidget,
    ToolButton)

class Ui_ReaderWidget(object):
    def setupUi(self, ReaderWidget):
        if not ReaderWidget.objectName():
            ReaderWidget.setObjectName(u"ReaderWidget")
        ReaderWidget.resize(640, 480)
        self.horizontalLayout_2 = QHBoxLayout(ReaderWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.readerCardWidget = SimpleCardWidget(ReaderWidget)
        self.readerCardWidget.setObjectName(u"readerCardWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readerCardWidget.sizePolicy().hasHeightForWidth())
        self.readerCardWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.readerCardWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.readerWidget = QWidget(self.readerCardWidget)
        self.readerWidget.setObjectName(u"readerWidget")
        sizePolicy.setHeightForWidth(self.readerWidget.sizePolicy().hasHeightForWidth())
        self.readerWidget.setSizePolicy(sizePolicy)
        self.reader_layout = QHBoxLayout(self.readerWidget)
        self.reader_layout.setSpacing(0)
        self.reader_layout.setObjectName(u"reader_layout")
        self.reader_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.readerWidget)

        self.actionsHLayout = QHBoxLayout()
        self.actionsHLayout.setObjectName(u"actionsHLayout")
        self.readerActionsWidget = QWidget(self.readerCardWidget)
        self.readerActionsWidget.setObjectName(u"readerActionsWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.readerActionsWidget.sizePolicy().hasHeightForWidth())
        self.readerActionsWidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.readerActionsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(10, 29, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.prev_chapter_btn = ToolButton(self.readerActionsWidget)
        self.prev_chapter_btn.setObjectName(u"prev_chapter_btn")

        self.horizontalLayout.addWidget(self.prev_chapter_btn)

        self.prev_page_btn = ToolButton(self.readerActionsWidget)
        self.prev_page_btn.setObjectName(u"prev_page_btn")

        self.horizontalLayout.addWidget(self.prev_page_btn)

        self.chapterLabel = BodyLabel(self.readerActionsWidget)
        self.chapterLabel.setObjectName(u"chapterLabel")
        self.chapterLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.chapterLabel)

        self.pageLabel = BodyLabel(self.readerActionsWidget)
        self.pageLabel.setObjectName(u"pageLabel")
        self.pageLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.pageLabel)

        self.next_page_btn = ToolButton(self.readerActionsWidget)
        self.next_page_btn.setObjectName(u"next_page_btn")

        self.horizontalLayout.addWidget(self.next_page_btn)

        self.next_chapter_btn = ToolButton(self.readerActionsWidget)
        self.next_chapter_btn.setObjectName(u"next_chapter_btn")

        self.horizontalLayout.addWidget(self.next_chapter_btn)

        self.horizontalSpacer_2 = QSpacerItem(11, 29, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.actionsHLayout.addWidget(self.readerActionsWidget)

        self.windowActionsWidget = QWidget(self.readerCardWidget)
        self.windowActionsWidget.setObjectName(u"windowActionsWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.windowActionsWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.fullscreenButton = ToolButton(self.windowActionsWidget)
        self.fullscreenButton.setObjectName(u"fullscreenButton")

        self.horizontalLayout_4.addWidget(self.fullscreenButton)

        self.chaptersListButton = ToolButton(self.windowActionsWidget)
        self.chaptersListButton.setObjectName(u"chaptersListButton")

        self.horizontalLayout_4.addWidget(self.chaptersListButton)


        self.actionsHLayout.addWidget(self.windowActionsWidget)


        self.verticalLayout_3.addLayout(self.actionsHLayout)


        self.horizontalLayout_2.addWidget(self.readerCardWidget)

        self.chaptersCard = CardWidget(ReaderWidget)
        self.chaptersCard.setObjectName(u"chaptersCard")
        self.verticalLayout_2 = QVBoxLayout(self.chaptersCard)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chaptersList = ListWidget(self.chaptersCard)
        self.chaptersList.setObjectName(u"chaptersList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chaptersList.sizePolicy().hasHeightForWidth())
        self.chaptersList.setSizePolicy(sizePolicy2)
        self.chaptersList.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.chaptersList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chaptersList.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.chaptersList)


        self.horizontalLayout_2.addWidget(self.chaptersCard)


        self.retranslateUi(ReaderWidget)

        QMetaObject.connectSlotsByName(ReaderWidget)
    # setupUi

    def retranslateUi(self, ReaderWidget):
#if QT_CONFIG(shortcut)
        self.prev_chapter_btn.setShortcut(qtTrId(u""))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(shortcut)
        self.prev_page_btn.setShortcut(qtTrId(u""))
#endif // QT_CONFIG(shortcut)
        self.chapterLabel.setText(qtTrId(u"label.Chapter"))
        self.pageLabel.setText(qtTrId(u"label.Page"))
#if QT_CONFIG(shortcut)
        self.next_page_btn.setShortcut(qtTrId(u""))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(shortcut)
        self.next_chapter_btn.setShortcut(qtTrId(u""))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(shortcut)
        self.fullscreenButton.setShortcut(qtTrId(u""))
#endif // QT_CONFIG(shortcut)
        pass
    # retranslateUi

