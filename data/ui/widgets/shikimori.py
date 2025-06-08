# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shikimori.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, LineEdit, PushButton,
    SearchLineEdit, SimpleCardWidget, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(662, 397)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search = QVBoxLayout()
        self.search.setObjectName(u"search")
        self.items_frame = SimpleCardWidget(Form)
        self.items_frame.setObjectName(u"items_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items_frame.sizePolicy().hasHeightForWidth())
        self.items_frame.setSizePolicy(sizePolicy)
        self.items_layout = QVBoxLayout(self.items_frame)
        self.items_layout.setObjectName(u"items_layout")

        self.search.addWidget(self.items_frame)

        self.search_frame = SimpleCardWidget(Form)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.text_frame = SimpleCardWidget(self.search_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.horizontalLayout = QHBoxLayout(self.text_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_line = SearchLineEdit(self.text_frame)
        self.title_line.setObjectName(u"title_line")

        self.horizontalLayout.addWidget(self.title_line)


        self.horizontalLayout_3.addWidget(self.text_frame)

        self.page_frame = SimpleCardWidget(self.search_frame)
        self.page_frame.setObjectName(u"page_frame")
        self.horizontalLayout_5 = QHBoxLayout(self.page_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.prev_btn = ToolButton(self.page_frame)
        self.prev_btn.setObjectName(u"prev_btn")

        self.horizontalLayout_5.addWidget(self.prev_btn)

        self.page_label = BodyLabel(self.page_frame)
        self.page_label.setObjectName(u"page_label")

        self.horizontalLayout_5.addWidget(self.page_label)

        self.next_btn = ToolButton(self.page_frame)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout_5.addWidget(self.next_btn)


        self.horizontalLayout_3.addWidget(self.page_frame)


        self.search.addWidget(self.search_frame)


        self.horizontalLayout_4.addLayout(self.search)

        self.lists_frame = SimpleCardWidget(Form)
        self.lists_frame.setObjectName(u"lists_frame")
        self.verticalLayout = QVBoxLayout(self.lists_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.planned_btn = PushButton(self.lists_frame)
        self.planned_btn.setObjectName(u"planned_btn")
        self.planned_btn.setCheckable(True)
        self.planned_btn.setChecked(True)
        self.planned_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.planned_btn)

        self.completed_btn = PushButton(self.lists_frame)
        self.completed_btn.setObjectName(u"completed_btn")
        self.completed_btn.setCheckable(True)
        self.completed_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.completed_btn)

        self.reading_btn = PushButton(self.lists_frame)
        self.reading_btn.setObjectName(u"reading_btn")
        self.reading_btn.setCheckable(True)
        self.reading_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reading_btn)

        self.re_reading_btn = PushButton(self.lists_frame)
        self.re_reading_btn.setObjectName(u"re_reading_btn")
        self.re_reading_btn.setCheckable(True)
        self.re_reading_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.re_reading_btn)

        self.on_hold_btn = PushButton(self.lists_frame)
        self.on_hold_btn.setObjectName(u"on_hold_btn")
        self.on_hold_btn.setCheckable(True)
        self.on_hold_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.on_hold_btn)

        self.dropped_btn = PushButton(self.lists_frame)
        self.dropped_btn.setObjectName(u"dropped_btn")
        self.dropped_btn.setCheckable(True)
        self.dropped_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dropped_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.auth_btn = PushButton(self.lists_frame)
        self.auth_btn.setObjectName(u"auth_btn")

        self.verticalLayout.addWidget(self.auth_btn)


        self.horizontalLayout_4.addWidget(self.lists_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.title_line.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.page_label.setText(QCoreApplication.translate("Form", u"Page 1", None))
        self.planned_btn.setText(QCoreApplication.translate("Form", u"Planned", None))
        self.completed_btn.setText(QCoreApplication.translate("Form", u"Completed", None))
        self.reading_btn.setText(QCoreApplication.translate("Form", u"Reading", None))
        self.re_reading_btn.setText(QCoreApplication.translate("Form", u"Re-reading", None))
        self.on_hold_btn.setText(QCoreApplication.translate("Form", u"On hold", None))
        self.dropped_btn.setText(QCoreApplication.translate("Form", u"Dropped", None))
        self.auth_btn.setText(QCoreApplication.translate("Form", u"Sign in", None))
        pass
    # retranslateUi

