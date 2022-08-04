# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_library.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(569, 366)
        Dialog.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.list_manga = QListWidget(Dialog)
        self.list_manga.setObjectName(u"list_manga")
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
        brush2 = QBrush(QColor(0, 133, 52, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.list_manga.setPalette(palette)
        self.list_manga.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.list_manga)

        self.lists_frame = QFrame(Dialog)
        self.lists_frame.setObjectName(u"lists_frame")
        self.lists_frame.setStyleSheet(u"QPushButton {\n"
"	padding: 5px 1px;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 133, 52);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	border-left: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border-left: 3px solid white;\n"
"}")
        self.lists_frame.setFrameShape(QFrame.StyledPanel)
        self.lists_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.lists_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.b_planned = QPushButton(self.lists_frame)
        self.b_planned.setObjectName(u"b_planned")
        self.b_planned.setStyleSheet(u"")
        self.b_planned.setCheckable(True)
        self.b_planned.setChecked(True)
        self.b_planned.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b_planned)

        self.b_completed = QPushButton(self.lists_frame)
        self.b_completed.setObjectName(u"b_completed")
        self.b_completed.setStyleSheet(u"")
        self.b_completed.setCheckable(True)
        self.b_completed.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b_completed)

        self.b_watching = QPushButton(self.lists_frame)
        self.b_watching.setObjectName(u"b_watching")
        self.b_watching.setStyleSheet(u"")
        self.b_watching.setCheckable(True)
        self.b_watching.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b_watching)

        self.b_rewatching = QPushButton(self.lists_frame)
        self.b_rewatching.setObjectName(u"b_rewatching")
        self.b_rewatching.setStyleSheet(u"")
        self.b_rewatching.setCheckable(True)
        self.b_rewatching.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b_rewatching)

        self.b_on_hold = QPushButton(self.lists_frame)
        self.b_on_hold.setObjectName(u"b_on_hold")
        self.b_on_hold.setStyleSheet(u"")
        self.b_on_hold.setCheckable(True)
        self.b_on_hold.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b_on_hold)

        self.b_dropped = QPushButton(self.lists_frame)
        self.b_dropped.setObjectName(u"b_dropped")
        self.b_dropped.setStyleSheet(u"")
        self.b_dropped.setCheckable(True)
        self.b_dropped.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b_dropped)

        self.verticalSpacer = QSpacerItem(94, 181, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.lists_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.b_planned.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043e", None))
        self.b_completed.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e", None))
        self.b_watching.setText(QCoreApplication.translate("Dialog", u"\u0427\u0438\u0442\u0430\u044e", None))
        self.b_rewatching.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0447\u0438\u0442\u044b\u0432\u0430\u044e", None))
        self.b_on_hold.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043b\u043e\u0436\u0435\u043d\u043e", None))
        self.b_dropped.setText(QCoreApplication.translate("Dialog", u"\u0411\u0440\u043e\u0448\u0435\u043d\u043e", None))
    # retranslateUi

