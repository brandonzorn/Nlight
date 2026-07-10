# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QSizePolicy, QSpacerItem, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CardWidget, SimpleCardWidget, TitleLabel, ToolButton,
    TreeWidget)

class Ui_HistoryPage(object):
    def setupUi(self, HistoryPage):
        if not HistoryPage.objectName():
            HistoryPage.setObjectName(u"HistoryPage")
        HistoryPage.resize(640, 480)
        HistoryPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_2 = QVBoxLayout(HistoryPage)
        self.verticalLayout_2.setSpacing(28)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(60, 60, 60, 10)
        self.titleLabel = TitleLabel(HistoryPage)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout_2.addWidget(self.titleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.itemsWidget = CardWidget(HistoryPage)
        self.itemsWidget.setObjectName(u"itemsWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.itemsWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.itemsTree = TreeWidget(self.itemsWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.itemsTree.setHeaderItem(__qtreewidgetitem)
        self.itemsTree.setObjectName(u"itemsTree")
        self.itemsTree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.itemsTree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.itemsTree.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.itemsTree.setWordWrap(True)
        self.itemsTree.header().setVisible(False)

        self.horizontalLayout_2.addWidget(self.itemsTree)


        self.horizontalLayout.addWidget(self.itemsWidget)

        self.actionsFrame = SimpleCardWidget(HistoryPage)
        self.actionsFrame.setObjectName(u"actionsFrame")
        self.actionsFrame.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.actionsFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.delete_btn = ToolButton(self.actionsFrame)
        self.delete_btn.setObjectName(u"delete_btn")

        self.verticalLayout.addWidget(self.delete_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.actionsFrame)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(HistoryPage)

        QMetaObject.connectSlotsByName(HistoryPage)
    # setupUi

    def retranslateUi(self, HistoryPage):
        self.titleLabel.setText(QCoreApplication.translate("HistoryPage", u"History", None))
        pass
    # retranslateUi

