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
    QSizePolicy, QTreeWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, SimpleCardWidget, TitleLabel, ToolButton,
    TreeWidget)

class Ui_HistoryPage(object):
    def setupUi(self, HistoryPage):
        if not HistoryPage.objectName():
            HistoryPage.setObjectName(u"HistoryPage")
        HistoryPage.resize(640, 480)
        HistoryPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.page_layout = QVBoxLayout(HistoryPage)
        self.page_layout.setSpacing(28)
        self.page_layout.setObjectName(u"page_layout")
        self.page_layout.setContentsMargins(60, 60, 60, 10)
        self.title_label = TitleLabel(HistoryPage)
        self.title_label.setObjectName(u"title_label")

        self.page_layout.addWidget(self.title_label)

        self.body_layout = QHBoxLayout()
        self.body_layout.setSpacing(6)
        self.body_layout.setObjectName(u"body_layout")
        self.items_widget = CardWidget(HistoryPage)
        self.items_widget.setObjectName(u"items_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.items_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.items_tree = TreeWidget(self.items_widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.items_tree.setHeaderItem(__qtreewidgetitem)
        self.items_tree.setObjectName(u"items_tree")
        self.items_tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.items_tree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.items_tree.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.items_tree.setWordWrap(True)
        self.items_tree.header().setVisible(False)

        self.horizontalLayout_2.addWidget(self.items_tree)


        self.body_layout.addWidget(self.items_widget)

        self.actions_widget = QWidget(HistoryPage)
        self.actions_widget.setObjectName(u"actions_widget")
        self.verticalLayout_3 = QVBoxLayout(self.actions_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.delete_button = ToolButton(self.actions_widget)
        self.delete_button.setObjectName(u"delete_button")

        self.verticalLayout_3.addWidget(self.delete_button)

        self.actions_card = SimpleCardWidget(self.actions_widget)
        self.actions_card.setObjectName(u"actions_card")
        self.actions_card.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actions_card.sizePolicy().hasHeightForWidth())
        self.actions_card.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.actions_card)


        self.body_layout.addWidget(self.actions_widget)


        self.page_layout.addLayout(self.body_layout)


        self.retranslateUi(HistoryPage)

        QMetaObject.connectSlotsByName(HistoryPage)
    # setupUi

    def retranslateUi(self, HistoryPage):
        self.title_label.setText(QCoreApplication.translate("HistoryPage", u"History", None))
        pass
    # retranslateUi

