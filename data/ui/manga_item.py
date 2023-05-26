# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manga_item.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_manga_item_widget(object):
    def setupUi(self, manga_item_widget):
        if not manga_item_widget.objectName():
            manga_item_widget.setObjectName(u"manga_item_widget")
        manga_item_widget.resize(485, 406)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(manga_item_widget.sizePolicy().hasHeightForWidth())
        manga_item_widget.setSizePolicy(sizePolicy)
        manga_item_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(manga_item_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.manga_item_frame = QFrame(manga_item_widget)
        self.manga_item_frame.setObjectName(u"manga_item_frame")
        sizePolicy.setHeightForWidth(self.manga_item_frame.sizePolicy().hasHeightForWidth())
        self.manga_item_frame.setSizePolicy(sizePolicy)
        self.manga_item_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.manga_item_frame.setContextMenuPolicy(Qt.CustomContextMenu)
        self.manga_item_frame.setStyleSheet(u"")
        self.manga_item_frame.setFrameShape(QFrame.StyledPanel)
        self.manga_item_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.manga_item_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.image = QLabel(self.manga_item_frame)
        self.image.setObjectName(u"image")
        self.image.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.image)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.name_lbl = QLabel(self.manga_item_frame)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.name_lbl)


        self.verticalLayout.addWidget(self.manga_item_frame)


        self.retranslateUi(manga_item_widget)

        QMetaObject.connectSlotsByName(manga_item_widget)
    # setupUi

    def retranslateUi(self, manga_item_widget):
        manga_item_widget.setWindowTitle(QCoreApplication.translate("manga_item_widget", u"Form", None))
        self.image.setText("")
        self.name_lbl.setText("")
    # retranslateUi

