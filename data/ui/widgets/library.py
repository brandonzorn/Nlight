# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, qtTrId)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import PushButton

class Ui_LibraryPage(object):
    def setupUi(self, LibraryPage):
        if not LibraryPage.objectName():
            LibraryPage.setObjectName(u"LibraryPage")
        LibraryPage.resize(640, 480)
        LibraryPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout = QHBoxLayout(LibraryPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.itemsWidget = QWidget(LibraryPage)
        self.itemsWidget.setObjectName(u"itemsWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemsWidget.sizePolicy().hasHeightForWidth())
        self.itemsWidget.setSizePolicy(sizePolicy)
        self.items_layout = QVBoxLayout(self.itemsWidget)
        self.items_layout.setSpacing(0)
        self.items_layout.setObjectName(u"items_layout")
        self.items_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.itemsWidget)

        self.libraryListsWidget = QWidget(LibraryPage)
        self.libraryListsWidget.setObjectName(u"libraryListsWidget")
        self.verticalLayout_2 = QVBoxLayout(self.libraryListsWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plannedButton = PushButton(self.libraryListsWidget)
        self.plannedButton.setObjectName(u"plannedButton")
        self.plannedButton.setCheckable(True)
        self.plannedButton.setChecked(True)
        self.plannedButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.plannedButton)

        self.completedButton = PushButton(self.libraryListsWidget)
        self.completedButton.setObjectName(u"completedButton")
        self.completedButton.setCheckable(True)
        self.completedButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.completedButton)

        self.readingButton = PushButton(self.libraryListsWidget)
        self.readingButton.setObjectName(u"readingButton")
        self.readingButton.setCheckable(True)
        self.readingButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.readingButton)

        self.reReadingButton = PushButton(self.libraryListsWidget)
        self.reReadingButton.setObjectName(u"reReadingButton")
        self.reReadingButton.setCheckable(True)
        self.reReadingButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.reReadingButton)

        self.onHoldButton = PushButton(self.libraryListsWidget)
        self.onHoldButton.setObjectName(u"onHoldButton")
        self.onHoldButton.setCheckable(True)
        self.onHoldButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.onHoldButton)

        self.droppedButton = PushButton(self.libraryListsWidget)
        self.droppedButton.setObjectName(u"droppedButton")
        self.droppedButton.setCheckable(True)
        self.droppedButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.droppedButton)

        self.verticalSpacer = QSpacerItem(20, 91, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.libraryListsWidget)


        self.retranslateUi(LibraryPage)

        QMetaObject.connectSlotsByName(LibraryPage)
    # setupUi

    def retranslateUi(self, LibraryPage):
        self.plannedButton.setText(qtTrId(u"library-list.Planned"))
        self.completedButton.setText(qtTrId(u"library-list.Completed"))
        self.readingButton.setText(qtTrId(u"library-list.Reading"))
        self.reReadingButton.setText(qtTrId(u"library-list.Re-reading"))
        self.onHoldButton.setText(qtTrId(u"library-list.On hold"))
        self.droppedButton.setText(qtTrId(u"library-list.Dropped"))
        pass
    # retranslateUi

