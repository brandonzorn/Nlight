# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manga_item.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CardWidget)

class Ui_MangaItem(object):
    def setupUi(self, MangaItem):
        if not MangaItem.objectName():
            MangaItem.setObjectName(u"MangaItem")
        MangaItem.resize(400, 380)
        MangaItem.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.widget_layout = QVBoxLayout(MangaItem)
        self.widget_layout.setSpacing(3)
        self.widget_layout.setObjectName(u"widget_layout")
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.image_card = CardWidget(MangaItem)
        self.image_card.setObjectName(u"image_card")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_card.sizePolicy().hasHeightForWidth())
        self.image_card.setSizePolicy(sizePolicy)
        self.card_layout = QVBoxLayout(self.image_card)
        self.card_layout.setSpacing(0)
        self.card_layout.setObjectName(u"card_layout")
        self.card_layout.setContentsMargins(0, 0, 0, 0)
        self.image_label = QLabel(self.image_card)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.card_layout.addWidget(self.image_label)


        self.widget_layout.addWidget(self.image_card)

        self.title_label = BodyLabel(MangaItem)
        self.title_label.setObjectName(u"title_label")

        self.widget_layout.addWidget(self.title_label)


        self.retranslateUi(MangaItem)

        QMetaObject.connectSlotsByName(MangaItem)
    # setupUi

    def retranslateUi(self, MangaItem):
        pass
    # retranslateUi

