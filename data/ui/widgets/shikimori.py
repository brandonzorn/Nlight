# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shikimori.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PushButton, SearchLineEdit,
    ToolButton)

class Ui_ExternalLibraryPage(object):
    def setupUi(self, ExternalLibraryPage):
        if not ExternalLibraryPage.objectName():
            ExternalLibraryPage.setObjectName(u"ExternalLibraryPage")
        ExternalLibraryPage.resize(640, 480)
        ExternalLibraryPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_4 = QHBoxLayout(ExternalLibraryPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.itemsWidget = QWidget(ExternalLibraryPage)
        self.itemsWidget.setObjectName(u"itemsWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemsWidget.sizePolicy().hasHeightForWidth())
        self.itemsWidget.setSizePolicy(sizePolicy)
        self.itemsLayout = QVBoxLayout(self.itemsWidget)
        self.itemsLayout.setSpacing(0)
        self.itemsLayout.setObjectName(u"itemsLayout")
        self.itemsLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.itemsWidget)

        self.searchWidget = QWidget(ExternalLibraryPage)
        self.searchWidget.setObjectName(u"searchWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.searchWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.text_widget = QWidget(self.searchWidget)
        self.text_widget.setObjectName(u"text_widget")
        self.horizontalLayout = QHBoxLayout(self.text_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.searchLineEdit = SearchLineEdit(self.text_widget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.horizontalLayout.addWidget(self.searchLineEdit)


        self.horizontalLayout_3.addWidget(self.text_widget)

        self.page_widget = QWidget(self.searchWidget)
        self.page_widget.setObjectName(u"page_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.page_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.previousButton = ToolButton(self.page_widget)
        self.previousButton.setObjectName(u"previousButton")

        self.horizontalLayout_2.addWidget(self.previousButton)

        self.pageLabel = BodyLabel(self.page_widget)
        self.pageLabel.setObjectName(u"pageLabel")

        self.horizontalLayout_2.addWidget(self.pageLabel)

        self.nextButton = ToolButton(self.page_widget)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout_2.addWidget(self.nextButton)


        self.horizontalLayout_3.addWidget(self.page_widget)


        self.verticalLayout_2.addWidget(self.searchWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.libraryListWidget = QWidget(ExternalLibraryPage)
        self.libraryListWidget.setObjectName(u"libraryListWidget")
        self.verticalLayout = QVBoxLayout(self.libraryListWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plannedButton = PushButton(self.libraryListWidget)
        self.plannedButton.setObjectName(u"plannedButton")
        self.plannedButton.setCheckable(True)
        self.plannedButton.setChecked(True)
        self.plannedButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.plannedButton)

        self.completedButton = PushButton(self.libraryListWidget)
        self.completedButton.setObjectName(u"completedButton")
        self.completedButton.setCheckable(True)
        self.completedButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.completedButton)

        self.readingButton = PushButton(self.libraryListWidget)
        self.readingButton.setObjectName(u"readingButton")
        self.readingButton.setCheckable(True)
        self.readingButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.readingButton)

        self.reReadingButton = PushButton(self.libraryListWidget)
        self.reReadingButton.setObjectName(u"reReadingButton")
        self.reReadingButton.setCheckable(True)
        self.reReadingButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reReadingButton)

        self.onHoldButton = PushButton(self.libraryListWidget)
        self.onHoldButton.setObjectName(u"onHoldButton")
        self.onHoldButton.setCheckable(True)
        self.onHoldButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.onHoldButton)

        self.droppedButton = PushButton(self.libraryListWidget)
        self.droppedButton.setObjectName(u"droppedButton")
        self.droppedButton.setCheckable(True)
        self.droppedButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.droppedButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.signInButton = PushButton(self.libraryListWidget)
        self.signInButton.setObjectName(u"signInButton")

        self.verticalLayout.addWidget(self.signInButton)


        self.horizontalLayout_4.addWidget(self.libraryListWidget)


        self.retranslateUi(ExternalLibraryPage)

        QMetaObject.connectSlotsByName(ExternalLibraryPage)
    # setupUi

    def retranslateUi(self, ExternalLibraryPage):
        self.searchLineEdit.setPlaceholderText(qtTrId(u"label.Search"))
        self.pageLabel.setText(qtTrId(u"label.Page"))
        self.plannedButton.setText(qtTrId(u"library-list.Planned"))
        self.completedButton.setText(qtTrId(u"library-list.Completed"))
        self.readingButton.setText(qtTrId(u"library-list.Reading"))
        self.reReadingButton.setText(qtTrId(u"library-list.Re-reading"))
        self.onHoldButton.setText(qtTrId(u"library-list.On hold"))
        self.droppedButton.setText(qtTrId(u"library-list.Dropped"))
        self.signInButton.setText(qtTrId(u""))
        pass
    # retranslateUi

