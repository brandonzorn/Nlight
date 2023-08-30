# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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

from qfluentwidgets import (CardWidget, PushButton, SimpleCardWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(562, 350)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.items_frame = SimpleCardWidget(Form)
        self.items_frame.setObjectName(u"items_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items_frame.sizePolicy().hasHeightForWidth())
        self.items_frame.setSizePolicy(sizePolicy)
        self.items_layout = QVBoxLayout(self.items_frame)
        self.items_layout.setObjectName(u"items_layout")

        self.horizontalLayout.addWidget(self.items_frame)

        self.lists_frame = SimpleCardWidget(Form)
        self.lists_frame.setObjectName(u"lists_frame")
        self.verticalLayout_2 = QVBoxLayout(self.lists_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.planned_btn = PushButton(self.lists_frame)
        self.planned_btn.setObjectName(u"planned_btn")
        self.planned_btn.setCheckable(True)
        self.planned_btn.setChecked(True)
        self.planned_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.planned_btn)

        self.completed_btn = PushButton(self.lists_frame)
        self.completed_btn.setObjectName(u"completed_btn")
        self.completed_btn.setCheckable(True)
        self.completed_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.completed_btn)

        self.reading_btn = PushButton(self.lists_frame)
        self.reading_btn.setObjectName(u"reading_btn")
        self.reading_btn.setCheckable(True)
        self.reading_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.reading_btn)

        self.re_reading_btn = PushButton(self.lists_frame)
        self.re_reading_btn.setObjectName(u"re_reading_btn")
        self.re_reading_btn.setCheckable(True)
        self.re_reading_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.re_reading_btn)

        self.on_hold_btn = PushButton(self.lists_frame)
        self.on_hold_btn.setObjectName(u"on_hold_btn")
        self.on_hold_btn.setCheckable(True)
        self.on_hold_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.on_hold_btn)

        self.dropped_btn = PushButton(self.lists_frame)
        self.dropped_btn.setObjectName(u"dropped_btn")
        self.dropped_btn.setCheckable(True)
        self.dropped_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dropped_btn)

        self.verticalSpacer = QSpacerItem(20, 91, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.lists_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.planned_btn.setText(QCoreApplication.translate("Form", u"Planned", None))
        self.completed_btn.setText(QCoreApplication.translate("Form", u"Completed", None))
        self.reading_btn.setText(QCoreApplication.translate("Form", u"Reading", None))
        self.re_reading_btn.setText(QCoreApplication.translate("Form", u"Re-reading", None))
        self.on_hold_btn.setText(QCoreApplication.translate("Form", u"On hold", None))
        self.dropped_btn.setText(QCoreApplication.translate("Form", u"Dropped", None))
        pass
    # retranslateUi

