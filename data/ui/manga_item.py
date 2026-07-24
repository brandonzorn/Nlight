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
        self.mangaItemVLayout = QVBoxLayout(MangaItem)
        self.mangaItemVLayout.setSpacing(3)
        self.mangaItemVLayout.setObjectName(u"mangaItemVLayout")
        self.mangaItemVLayout.setContentsMargins(0, 0, 0, 0)
        self.imageCardWidget = CardWidget(MangaItem)
        self.imageCardWidget.setObjectName(u"imageCardWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCardWidget.sizePolicy().hasHeightForWidth())
        self.imageCardWidget.setSizePolicy(sizePolicy)
        self.imageVLayout = QVBoxLayout(self.imageCardWidget)
        self.imageVLayout.setSpacing(0)
        self.imageVLayout.setObjectName(u"imageVLayout")
        self.imageVLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLabel = QLabel(self.imageCardWidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.imageVLayout.addWidget(self.imageLabel)


        self.mangaItemVLayout.addWidget(self.imageCardWidget)

        self.nameLabel = BodyLabel(MangaItem)
        self.nameLabel.setObjectName(u"nameLabel")

        self.mangaItemVLayout.addWidget(self.nameLabel)


        self.retranslateUi(MangaItem)

        QMetaObject.connectSlotsByName(MangaItem)
    # setupUi

    def retranslateUi(self, MangaItem):
        pass
    # retranslateUi

