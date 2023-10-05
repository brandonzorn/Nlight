# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 384)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_widget = QWidget(self.centralwidget)
        self.side_menu_widget.setObjectName("side_menu_widget")
        self.side_menu_widget.setStyleSheet("")
        self.verticalLayout = QVBoxLayout(self.side_menu_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.side_menu_widget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_library = QPushButton(self.frame)
        self.btn_library.setObjectName("btn_library")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_library.sizePolicy().hasHeightForWidth()
        )
        self.btn_library.setSizePolicy(sizePolicy)
        self.btn_library.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_library.setStyleSheet("")
        self.btn_library.setLocale(
            QLocale(QLocale.English, QLocale.UnitedStates)
        )
        self.btn_library.setCheckable(True)
        self.btn_library.setAutoRepeat(False)
        self.btn_library.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_library)

        self.btn_main = QPushButton(self.frame)
        self.btn_main.setObjectName("btn_main")
        sizePolicy.setHeightForWidth(
            self.btn_main.sizePolicy().hasHeightForWidth()
        )
        self.btn_main.setSizePolicy(sizePolicy)
        self.btn_main.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_main.setStyleSheet("")
        self.btn_main.setCheckable(True)
        self.btn_main.setChecked(True)
        self.btn_main.setAutoRepeat(False)
        self.btn_main.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_main)

        self.btn_shikimori = QPushButton(self.frame)
        self.btn_shikimori.setObjectName("btn_shikimori")
        sizePolicy.setHeightForWidth(
            self.btn_shikimori.sizePolicy().hasHeightForWidth()
        )
        self.btn_shikimori.setSizePolicy(sizePolicy)
        self.btn_shikimori.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_shikimori.setStyleSheet("")
        self.btn_shikimori.setCheckable(True)
        self.btn_shikimori.setAutoRepeat(False)
        self.btn_shikimori.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_shikimori)

        self.btn_history = QPushButton(self.frame)
        self.btn_history.setObjectName("btn_history")
        sizePolicy.setHeightForWidth(
            self.btn_history.sizePolicy().hasHeightForWidth()
        )
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setStyleSheet("")
        self.btn_history.setCheckable(True)
        self.btn_history.setAutoRepeat(False)
        self.btn_history.setAutoExclusive(True)
        self.btn_history.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.btn_history)

        self.verticalSpacer = QSpacerItem(
            17, 17, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout.addWidget(self.side_menu_widget)

        self.top_item_widget = QWidget(self.centralwidget)
        self.top_item_widget.setObjectName("top_item_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.top_item_widget.sizePolicy().hasHeightForWidth()
        )
        self.top_item_widget.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(32, 32, 32, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        # endif
        self.top_item_widget.setPalette(palette)
        self.top_item_widget.setStyleSheet("")
        self.verticalLayout_2 = QVBoxLayout(self.top_item_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_item = QStackedWidget(self.top_item_widget)
        self.top_item.setObjectName("top_item")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.top_item.sizePolicy().hasHeightForWidth()
        )
        self.top_item.setSizePolicy(sizePolicy2)
        self.top_item.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.top_item)

        self.horizontalLayout.addWidget(self.top_item_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.top_item.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Nlight", None)
        )
        self.btn_library.setText(
            QCoreApplication.translate("MainWindow", "Library", None)
        )
        self.btn_main.setText(
            QCoreApplication.translate("MainWindow", "Main", None)
        )
        self.btn_shikimori.setText(
            QCoreApplication.translate("MainWindow", "Shikimori", None)
        )
        self.btn_history.setText(
            QCoreApplication.translate("MainWindow", "History", None)
        )

    # retranslateUi
