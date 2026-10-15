# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_area.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
    QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, SimpleCardWidget, Slider, TextEdit)

class Ui_TextArea(object):
    def setupUi(self, TextArea):
        if not TextArea.objectName():
            TextArea.setObjectName(u"TextArea")
        TextArea.resize(640, 480)
        self.verticalLayout_2 = QVBoxLayout(TextArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fontSizeCard = SimpleCardWidget(TextArea)
        self.fontSizeCard.setObjectName(u"fontSizeCard")
        self.horizontalLayout_2 = QHBoxLayout(self.fontSizeCard)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fontSizeSlider = Slider(self.fontSizeCard)
        self.fontSizeSlider.setObjectName(u"fontSizeSlider")
        self.fontSizeSlider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.fontSizeSlider.setMinimum(9)
        self.fontSizeSlider.setMaximum(25)
        self.fontSizeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.fontSizeSlider)


        self.verticalLayout_2.addWidget(self.fontSizeCard)

        self.contentWidget = SimpleCardWidget(TextArea)
        self.contentWidget.setObjectName(u"contentWidget")
        self.contentHLayout = QHBoxLayout(self.contentWidget)
        self.contentHLayout.setSpacing(0)
        self.contentHLayout.setObjectName(u"contentHLayout")
        self.contentHLayout.setContentsMargins(0, 0, 0, 0)
        self.contentText = TextEdit(self.contentWidget)
        self.contentText.setObjectName(u"contentText")
        self.contentText.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.contentText.setFrameShape(QFrame.Shape.NoFrame)

        self.contentHLayout.addWidget(self.contentText)


        self.verticalLayout_2.addWidget(self.contentWidget)


        self.retranslateUi(TextArea)

        QMetaObject.connectSlotsByName(TextArea)
    # setupUi

    def retranslateUi(self, TextArea):
        pass
    # retranslateUi

