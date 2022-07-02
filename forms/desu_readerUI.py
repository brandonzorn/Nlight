# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_readerUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(527, 604)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        Dialog.setPalette(palette)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.text_size_slider = QSlider(Dialog)
        self.text_size_slider.setObjectName(u"text_size_slider")
        self.text_size_slider.setEnabled(True)
        self.text_size_slider.setFocusPolicy(Qt.NoFocus)
        self.text_size_slider.setMinimum(9)
        self.text_size_slider.setMaximum(25)
        self.text_size_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.text_size_slider)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 507, 492))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.img = QLabel(self.scrollAreaWidgetContents)
        self.img.setObjectName(u"img")
        self.img.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.img.setWordWrap(True)
        self.img.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.img)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_page = QPushButton(Dialog)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setEnabled(True)
        self.prev_page.setFocusPolicy(Qt.NoFocus)
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon = QIcon()
        icon.addFile(u"../images/prev.png", QSize(), QIcon.Normal, QIcon.On)
        self.prev_page.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.prev_page)

        self.lbl_page = QLabel(Dialog)
        self.lbl_page.setObjectName(u"lbl_page")

        self.horizontalLayout_3.addWidget(self.lbl_page)

        self.next_page = QPushButton(Dialog)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setFocusPolicy(Qt.NoFocus)
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon1 = QIcon()
        icon1.addFile(u"../images/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.next_page.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.next_page)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prev_chp = QPushButton(Dialog)
        self.prev_chp.setObjectName(u"prev_chp")
        self.prev_chp.setFocusPolicy(Qt.NoFocus)
        self.prev_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon2 = QIcon()
        icon2.addFile(u"../images/double_prev.png", QSize(), QIcon.Normal, QIcon.On)
        self.prev_chp.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.prev_chp)

        self.lbl_chp = QLabel(Dialog)
        self.lbl_chp.setObjectName(u"lbl_chp")

        self.horizontalLayout_2.addWidget(self.lbl_chp)

        self.next_chp = QPushButton(Dialog)
        self.next_chp.setObjectName(u"next_chp")
        self.next_chp.setFocusPolicy(Qt.NoFocus)
        self.next_chp.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon3 = QIcon()
        icon3.addFile(u"../images/double_next.png", QSize(), QIcon.Normal, QIcon.On)
        self.next_chp.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.next_chp)

        self.btn_fullscreen = QPushButton(Dialog)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fullscreen.sizePolicy().hasHeightForWidth())
        self.btn_fullscreen.setSizePolicy(sizePolicy)
        self.btn_fullscreen.setFocusPolicy(Qt.NoFocus)
        self.btn_fullscreen.setStyleSheet(u"background-color: rgb(0, 133, 52);")
        icon4 = QIcon()
        icon4.addFile(u"../images/fullscreen.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_fullscreen.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_fullscreen)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.img.setText("")
        self.prev_page.setText("")
        self.lbl_page.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page.setText("")
        self.prev_chp.setText("")
        self.lbl_chp.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u0430 1", None))
        self.next_chp.setText("")
        self.btn_fullscreen.setText("")
    # retranslateUi

