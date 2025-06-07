# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rate.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, HorizontalSeparator,
    PushButton, SpinBox)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(555, 467)
        Dialog.setStyleSheet(u"")
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chapters_frame = CardWidget(Dialog)
        self.chapters_frame.setObjectName(u"chapters_frame")
        self.horizontalLayout_5 = QHBoxLayout(self.chapters_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = BodyLabel(self.chapters_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.HorizontalSeparator = HorizontalSeparator(self.chapters_frame)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")

        self.horizontalLayout_5.addWidget(self.HorizontalSeparator)

        self.chapters_box = SpinBox(self.chapters_frame)
        self.chapters_box.setObjectName(u"chapters_box")
        self.chapters_box.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.chapters_box)


        self.verticalLayout.addWidget(self.chapters_frame)

        self.score_frame = CardWidget(Dialog)
        self.score_frame.setObjectName(u"score_frame")
        self.horizontalLayout_6 = QHBoxLayout(self.score_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = BodyLabel(self.score_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.HorizontalSeparator_2 = HorizontalSeparator(self.score_frame)
        self.HorizontalSeparator_2.setObjectName(u"HorizontalSeparator_2")

        self.horizontalLayout_6.addWidget(self.HorizontalSeparator_2)

        self.score_box = SpinBox(self.score_frame)
        self.score_box.setObjectName(u"score_box")
        self.score_box.setMaximum(10)

        self.horizontalLayout_6.addWidget(self.score_box)


        self.verticalLayout.addWidget(self.score_frame)

        self.status_frame = CardWidget(Dialog)
        self.status_frame.setObjectName(u"status_frame")
        self.horizontalLayout_7 = QHBoxLayout(self.status_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = BodyLabel(self.status_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.HorizontalSeparator_3 = HorizontalSeparator(self.status_frame)
        self.HorizontalSeparator_3.setObjectName(u"HorizontalSeparator_3")

        self.horizontalLayout_7.addWidget(self.HorizontalSeparator_3)

        self.lib_list_box = ComboBox(self.status_frame)
        self.lib_list_box.setObjectName(u"lib_list_box")

        self.horizontalLayout_7.addWidget(self.lib_list_box)


        self.verticalLayout.addWidget(self.status_frame)

        self.actions_frame = QFrame(Dialog)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.actions_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cancel_btn = PushButton(self.actions_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.delete_btn = PushButton(self.actions_frame)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout.addWidget(self.delete_btn)

        self.update_btn = PushButton(self.actions_frame)
        self.update_btn.setObjectName(u"update_btn")

        self.horizontalLayout.addWidget(self.update_btn)


        self.verticalLayout.addWidget(self.actions_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Chapters read", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Rating", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"List", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.delete_btn.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.update_btn.setText(QCoreApplication.translate("Dialog", u"Update", None))
    # retranslateUi

