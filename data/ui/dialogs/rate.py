# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rate.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(555, 467)
        Dialog.setStyleSheet(u"")
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chapters_frame = QFrame(Dialog)
        self.chapters_frame.setObjectName(u"chapters_frame")
        self.chapters_frame.setFrameShape(QFrame.StyledPanel)
        self.chapters_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.chapters_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.chapters_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(391, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.chapters_box = QSpinBox(self.chapters_frame)
        self.chapters_box.setObjectName(u"chapters_box")
        self.chapters_box.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.chapters_box)


        self.verticalLayout.addWidget(self.chapters_frame)

        self.score_frame = QFrame(Dialog)
        self.score_frame.setObjectName(u"score_frame")
        self.score_frame.setFrameShape(QFrame.StyledPanel)
        self.score_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.score_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.score_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(444, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.score_box = QSpinBox(self.score_frame)
        self.score_box.setObjectName(u"score_box")
        self.score_box.setMaximum(10)

        self.horizontalLayout_3.addWidget(self.score_box)


        self.verticalLayout.addWidget(self.score_frame)

        self.status_frame = QFrame(Dialog)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setFrameShape(QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.status_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.status_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(414, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lib_list_box = QComboBox(self.status_frame)
        self.lib_list_box.setObjectName(u"lib_list_box")

        self.horizontalLayout_2.addWidget(self.lib_list_box)


        self.verticalLayout.addWidget(self.status_frame)

        self.actions_frame = QFrame(Dialog)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.actions_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_btn = QPushButton(self.actions_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.delete_btn = QPushButton(self.actions_frame)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.delete_btn)

        self.update_btn = QPushButton(self.actions_frame)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setCursor(QCursor(Qt.PointingHandCursor))

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

