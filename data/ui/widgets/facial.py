# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facial.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(613, 290)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.search = QVBoxLayout()
        self.search.setObjectName("search")
        self.items_frame = QFrame(Form)
        self.items_frame.setObjectName("items_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.items_frame.sizePolicy().hasHeightForWidth()
        )
        self.items_frame.setSizePolicy(sizePolicy)
        self.items_frame.setFrameShape(QFrame.StyledPanel)
        self.items_frame.setFrameShadow(QFrame.Raised)
        self.items_layout = QVBoxLayout(self.items_frame)
        self.items_layout.setObjectName("items_layout")

        self.search.addWidget(self.items_frame)

        self.search_frame = QFrame(Form)
        self.search_frame.setObjectName("search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.text_frame = QFrame(self.search_frame)
        self.text_frame.setObjectName("text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.text_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_line = QLineEdit(self.text_frame)
        self.title_line.setObjectName("title_line")

        self.horizontalLayout_2.addWidget(self.title_line)

        self.search_btn = QPushButton(self.text_frame)
        self.search_btn.setObjectName("search_btn")
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.search_btn)

        self.horizontalLayout_3.addWidget(self.text_frame)

        self.filter_btn = QPushButton(self.search_frame)
        self.filter_btn.setObjectName("filter_btn")
        self.filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.filter_btn.setCheckable(True)
        self.filter_btn.setChecked(True)

        self.horizontalLayout_3.addWidget(self.filter_btn)

        self.page_frame = QFrame(self.search_frame)
        self.page_frame.setObjectName("page_frame")
        self.page_frame.setFrameShape(QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.page_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prev_btn = QPushButton(self.page_frame)
        self.prev_btn.setObjectName("prev_btn")
        self.prev_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.prev_btn)

        self.page_label = QLabel(self.page_frame)
        self.page_label.setObjectName("page_label")

        self.horizontalLayout.addWidget(self.page_label)

        self.next_btn = QPushButton(self.page_frame)
        self.next_btn.setObjectName("next_btn")
        self.next_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.next_btn)

        self.horizontalLayout_3.addWidget(self.page_frame)

        self.search.addWidget(self.search_frame)

        self.horizontalLayout_5.addLayout(self.search)

        self.all_filters = QWidget(Form)
        self.all_filters.setObjectName("all_filters")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.all_filters.sizePolicy().hasHeightForWidth()
        )
        self.all_filters.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.all_filters)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.catalogs_frame = QFrame(self.all_filters)
        self.catalogs_frame.setObjectName("catalogs_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.catalogs_frame.sizePolicy().hasHeightForWidth()
        )
        self.catalogs_frame.setSizePolicy(sizePolicy2)
        self.catalogs_frame.setFrameShape(QFrame.StyledPanel)
        self.catalogs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.catalogs_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.catalogs_list = QListWidget(self.catalogs_frame)
        self.catalogs_list.setObjectName("catalogs_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.catalogs_list.sizePolicy().hasHeightForWidth()
        )
        self.catalogs_list.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.catalogs_list)

        self.horizontalLayout_6.addWidget(self.catalogs_frame)

        self.filters_widget = QWidget(self.all_filters)
        self.filters_widget.setObjectName("filters_widget")
        self.verticalLayout_2 = QVBoxLayout(self.filters_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.orders_frame = QFrame(self.filters_widget)
        self.orders_frame.setObjectName("orders_frame")
        self.orders_frame.setStyleSheet("")
        self.orders_frame.setFrameShape(QFrame.StyledPanel)
        self.orders_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.orders_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QLabel(self.orders_frame)
        self.label.setObjectName("label")

        self.verticalLayout_5.addWidget(self.label)

        self.orders_grid = QGridLayout()
        self.orders_grid.setObjectName("orders_grid")

        self.verticalLayout_5.addLayout(self.orders_grid)

        self.verticalLayout_2.addWidget(self.orders_frame)

        self.kinds_frame = QFrame(self.filters_widget)
        self.kinds_frame.setObjectName("kinds_frame")
        self.kinds_frame.setStyleSheet("")
        self.kinds_frame.setFrameShape(QFrame.StyledPanel)
        self.kinds_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.kinds_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QLabel(self.kinds_frame)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.kinds_grid = QGridLayout()
        self.kinds_grid.setObjectName("kinds_grid")

        self.verticalLayout_4.addLayout(self.kinds_grid)

        self.verticalLayout_2.addWidget(self.kinds_frame)

        self.genres_frame = QFrame(self.filters_widget)
        self.genres_frame.setObjectName("genres_frame")
        self.genres_frame.setFrameShape(QFrame.StyledPanel)
        self.genres_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.genres_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.genres_btn = QPushButton(self.genres_frame)
        self.genres_btn.setObjectName("genres_btn")
        self.genres_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.genres_btn)

        self.verticalLayout_2.addWidget(self.genres_frame)

        self.filter_catalog_frame = QFrame(self.filters_widget)
        self.filter_catalog_frame.setObjectName("filter_catalog_frame")
        self.filter_catalog_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_catalog_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.filter_catalog_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.catalogs_btn = QPushButton(self.filter_catalog_frame)
        self.catalogs_btn.setObjectName("catalogs_btn")
        self.catalogs_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.catalogs_btn)

        self.verticalLayout_2.addWidget(self.filter_catalog_frame)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.filter_actions_frame = QFrame(self.filters_widget)
        self.filter_actions_frame.setObjectName("filter_actions_frame")
        self.filter_actions_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.filter_actions_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.reset_btn = QPushButton(self.filter_actions_frame)
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.reset_btn)

        self.apply_btn = QPushButton(self.filter_actions_frame)
        self.apply_btn.setObjectName("apply_btn")
        self.apply_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.apply_btn)

        self.verticalLayout_2.addWidget(self.filter_actions_frame)

        self.horizontalLayout_6.addWidget(self.filters_widget)

        self.horizontalLayout_5.addWidget(self.all_filters)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        self.search_btn.setText("")
        self.filter_btn.setText(
            QCoreApplication.translate("Form", "Filters", None)
        )
        self.prev_btn.setText("")
        self.page_label.setText(
            QCoreApplication.translate("Form", "Page 1", None)
        )
        self.next_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", "Order", None))
        self.label_2.setText(QCoreApplication.translate("Form", "Kind", None))
        self.genres_btn.setText(
            QCoreApplication.translate("Form", "Genres list", None)
        )
        self.catalogs_btn.setText(
            QCoreApplication.translate("Form", "Catalogs", None)
        )
        self.reset_btn.setText(
            QCoreApplication.translate("Form", "Reset", None)
        )
        self.apply_btn.setText(
            QCoreApplication.translate("Form", "Apply", None)
        )
        pass

    # retranslateUi
