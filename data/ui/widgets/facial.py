# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facial.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidgetItem,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, LineEdit, ListWidget,
    PushButton, SearchLineEdit, ToolButton)

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(737, 480)
        MainPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_5 = QHBoxLayout(MainPage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.search = QVBoxLayout()
        self.search.setObjectName(u"search")
        self.search.setContentsMargins(0, 0, -1, 0)
        self.itemsWidget = QWidget(MainPage)
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

        self.search.addWidget(self.itemsWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.text_frame = QFrame(MainPage)
        self.text_frame.setObjectName(u"text_frame")
        self.horizontalLayout = QHBoxLayout(self.text_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_line = SearchLineEdit(self.text_frame)
        self.title_line.setObjectName(u"title_line")

        self.horizontalLayout.addWidget(self.title_line)

        self.filter_btn = PushButton(self.text_frame)
        self.filter_btn.setObjectName(u"filter_btn")
        self.filter_btn.setCheckable(True)
        self.filter_btn.setChecked(True)

        self.horizontalLayout.addWidget(self.filter_btn)


        self.horizontalLayout_3.addWidget(self.text_frame)

        self.page_frame = QFrame(MainPage)
        self.page_frame.setObjectName(u"page_frame")
        self.horizontalLayout_9 = QHBoxLayout(self.page_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.prev_btn = ToolButton(self.page_frame)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.prev_btn.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_9.addWidget(self.prev_btn)

        self.page_label = BodyLabel(self.page_frame)
        self.page_label.setObjectName(u"page_label")

        self.horizontalLayout_9.addWidget(self.page_label)

        self.next_btn = ToolButton(self.page_frame)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout_9.addWidget(self.next_btn)


        self.horizontalLayout_3.addWidget(self.page_frame)


        self.search.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.search)

        self.all_filters = QWidget(MainPage)
        self.all_filters.setObjectName(u"all_filters")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.all_filters.sizePolicy().hasHeightForWidth())
        self.all_filters.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.all_filters)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.catalogs_frame = CardWidget(self.all_filters)
        self.catalogs_frame.setObjectName(u"catalogs_frame")
        self.verticalLayout_4 = QVBoxLayout(self.catalogs_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.catalogs_list = ListWidget(self.catalogs_frame)
        self.catalogs_list.setObjectName(u"catalogs_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.catalogs_list.sizePolicy().hasHeightForWidth())
        self.catalogs_list.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.catalogs_list)


        self.horizontalLayout_6.addWidget(self.catalogs_frame)

        self.filters_widget = QWidget(self.all_filters)
        self.filters_widget.setObjectName(u"filters_widget")
        self.verticalLayout_2 = QVBoxLayout(self.filters_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ordersCard = CardWidget(self.filters_widget)
        self.ordersCard.setObjectName(u"ordersCard")
        self.ordersCardVLayout = QVBoxLayout(self.ordersCard)
        self.ordersCardVLayout.setObjectName(u"ordersCardVLayout")
        self.ordersLabel = BodyLabel(self.ordersCard)
        self.ordersLabel.setObjectName(u"ordersLabel")

        self.ordersCardVLayout.addWidget(self.ordersLabel)

        self.ordersVLayout = QVBoxLayout()
        self.ordersVLayout.setObjectName(u"ordersVLayout")

        self.ordersCardVLayout.addLayout(self.ordersVLayout)


        self.verticalLayout_2.addWidget(self.ordersCard)

        self.kindsCard = CardWidget(self.filters_widget)
        self.kindsCard.setObjectName(u"kindsCard")
        self.kindsCardVLayout = QVBoxLayout(self.kindsCard)
        self.kindsCardVLayout.setObjectName(u"kindsCardVLayout")
        self.kindsLabel = BodyLabel(self.kindsCard)
        self.kindsLabel.setObjectName(u"kindsLabel")

        self.kindsCardVLayout.addWidget(self.kindsLabel)

        self.kindsVLayout = QVBoxLayout()
        self.kindsVLayout.setObjectName(u"kindsVLayout")

        self.kindsCardVLayout.addLayout(self.kindsVLayout)


        self.verticalLayout_2.addWidget(self.kindsCard)

        self.moreFiltersWidget = QWidget(self.filters_widget)
        self.moreFiltersWidget.setObjectName(u"moreFiltersWidget")
        self.verticalLayout_3 = QVBoxLayout(self.moreFiltersWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.genresButton = PushButton(self.moreFiltersWidget)
        self.genresButton.setObjectName(u"genresButton")
        self.genresButton.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.verticalLayout_3.addWidget(self.genresButton)

        self.catalogsButton = PushButton(self.moreFiltersWidget)
        self.catalogsButton.setObjectName(u"catalogsButton")

        self.verticalLayout_3.addWidget(self.catalogsButton)


        self.verticalLayout_2.addWidget(self.moreFiltersWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.filter_actions_widget = QWidget(self.filters_widget)
        self.filter_actions_widget.setObjectName(u"filter_actions_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.filter_actions_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.reset_btn = PushButton(self.filter_actions_widget)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_7.addWidget(self.reset_btn)

        self.apply_btn = PushButton(self.filter_actions_widget)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout_7.addWidget(self.apply_btn)


        self.verticalLayout_2.addWidget(self.filter_actions_widget)


        self.horizontalLayout_6.addWidget(self.filters_widget)


        self.horizontalLayout_5.addWidget(self.all_filters)


        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        self.title_line.setPlaceholderText(QCoreApplication.translate("MainPage", u"Search", None))
        self.filter_btn.setText(QCoreApplication.translate("MainPage", u"Filters", None))
        self.page_label.setText(QCoreApplication.translate("MainPage", u"Page", None))
        self.ordersLabel.setText(QCoreApplication.translate("MainPage", u"Order", None))
        self.kindsLabel.setText(QCoreApplication.translate("MainPage", u"Kind", None))
        self.genresButton.setText(QCoreApplication.translate("MainPage", u"Genres list", None))
        self.catalogsButton.setText(QCoreApplication.translate("MainPage", u"Catalogs", None))
        self.reset_btn.setText(QCoreApplication.translate("MainPage", u"Reset", None))
        self.apply_btn.setText(QCoreApplication.translate("MainPage", u"Apply", None))
        pass
    # retranslateUi

