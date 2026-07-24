# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_area.ui'
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

        self.textCard = SimpleCardWidget(TextArea)
        self.textCard.setObjectName(u"textCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textCard.sizePolicy().hasHeightForWidth())
        self.textCard.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.textCard)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textContent = TextEdit(self.textCard)
        self.textContent.setObjectName(u"textContent")
        self.textContent.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.textContent.setFrameShape(QFrame.Shape.NoFrame)
        self.textContent.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.textContent)


        self.verticalLayout_2.addWidget(self.textCard)


        self.retranslateUi(TextArea)

        QMetaObject.connectSlotsByName(TextArea)
    # setupUi

    def retranslateUi(self, TextArea):
        pass
    # retranslateUi

