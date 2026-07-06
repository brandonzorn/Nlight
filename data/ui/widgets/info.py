# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QListWidgetItem, QSizePolicy, QSpacerItem, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, ImageLabel,
    ListWidget, ScrollArea, SimpleCardWidget, TextEdit,
    ToolButton, TreeWidget)

class Ui_InfoPage(object):
    def setupUi(self, InfoPage):
        if not InfoPage.objectName():
            InfoPage.setObjectName(u"InfoPage")
        InfoPage.resize(736, 531)
        InfoPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_4 = QHBoxLayout(InfoPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea = ScrollArea(InfoPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 440, 982))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 18, 0)
        self.headerWidget = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.headerHLayout = QHBoxLayout(self.headerWidget)
        self.headerHLayout.setObjectName(u"headerHLayout")
        self.headerHLayout.setContentsMargins(0, 0, 0, 0)
        self.headerHSpacer = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerHLayout.addItem(self.headerHSpacer)

        self.headerContentVLayout = QVBoxLayout()
        self.headerContentVLayout.setObjectName(u"headerContentVLayout")
        self.libraryWidget = SimpleCardWidget(self.headerWidget)
        self.libraryWidget.setObjectName(u"libraryWidget")
        self.libraryWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.libraryWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.libraryWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.libraryListComboBox = ComboBox(self.libraryWidget)
        self.libraryListComboBox.setObjectName(u"libraryListComboBox")

        self.horizontalLayout.addWidget(self.libraryListComboBox)

        self.addButton = ToolButton(self.libraryWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.addButton)


        self.headerContentVLayout.addWidget(self.libraryWidget)

        self.shikimoriWidget = SimpleCardWidget(self.headerWidget)
        self.shikimoriWidget.setObjectName(u"shikimoriWidget")
        self.shikimoriWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.shikimoriWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.shikimoriWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.shikimoriButton = ToolButton(self.shikimoriWidget)
        self.shikimoriButton.setObjectName(u"shikimoriButton")

        self.horizontalLayout_2.addWidget(self.shikimoriButton)


        self.headerContentVLayout.addWidget(self.shikimoriWidget)


        self.headerHLayout.addLayout(self.headerContentVLayout)


        self.verticalLayout.addWidget(self.headerWidget)

        self.mangaVLayout = QVBoxLayout()
        self.mangaVLayout.setObjectName(u"mangaVLayout")
        self.infoHLayout = QHBoxLayout()
        self.infoHLayout.setObjectName(u"infoHLayout")
        self.previewWidget = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.previewWidget.setObjectName(u"previewWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewWidget.sizePolicy().hasHeightForWidth())
        self.previewWidget.setSizePolicy(sizePolicy)
        self.previewLayout = QVBoxLayout(self.previewWidget)
        self.previewLayout.setObjectName(u"previewLayout")
        self.imageLabel = ImageLabel(self.previewWidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.previewLayout.addWidget(self.imageLabel)


        self.infoHLayout.addWidget(self.previewWidget)

        self.title_frame = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.title_frame.setObjectName(u"title_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.title_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.name_label = BodyLabel(self.title_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.name_label)

        self.russian_label = BodyLabel(self.title_frame)
        self.russian_label.setObjectName(u"russian_label")

        self.verticalLayout_8.addWidget(self.russian_label)

        self.status_label = BodyLabel(self.title_frame)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout_8.addWidget(self.status_label)

        self.catalog_score_label = BodyLabel(self.title_frame)
        self.catalog_score_label.setObjectName(u"catalog_score_label")

        self.verticalLayout_8.addWidget(self.catalog_score_label)

        self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.volumes_label = BodyLabel(self.title_frame)
        self.volumes_label.setObjectName(u"volumes_label")

        self.verticalLayout_8.addWidget(self.volumes_label)

        self.chapters_label = BodyLabel(self.title_frame)
        self.chapters_label.setObjectName(u"chapters_label")

        self.verticalLayout_8.addWidget(self.chapters_label)


        self.infoHLayout.addWidget(self.title_frame)


        self.mangaVLayout.addLayout(self.infoHLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.descriptionTextEdit = TextEdit(self.scrollAreaWidgetContents)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.descriptionTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.descriptionTextEdit.setUndoRedoEnabled(False)
        self.descriptionTextEdit.setReadOnly(True)
        self.descriptionTextEdit.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_9.addWidget(self.descriptionTextEdit)

        self.charactersWidget = CardWidget(self.scrollAreaWidgetContents)
        self.charactersWidget.setObjectName(u"charactersWidget")
        self.verticalLayout_2 = QVBoxLayout(self.charactersWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.charactersLabel = BodyLabel(self.charactersWidget)
        self.charactersLabel.setObjectName(u"charactersLabel")

        self.verticalLayout_2.addWidget(self.charactersLabel)

        self.charactersList = ListWidget(self.charactersWidget)
        self.charactersList.setObjectName(u"charactersList")
        self.charactersList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.charactersList.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.charactersList)


        self.verticalLayout_9.addWidget(self.charactersWidget)

        self.relatedWidget = CardWidget(self.scrollAreaWidgetContents)
        self.relatedWidget.setObjectName(u"relatedWidget")
        self.verticalLayout_4 = QVBoxLayout(self.relatedWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.relatedLabel = BodyLabel(self.relatedWidget)
        self.relatedLabel.setObjectName(u"relatedLabel")

        self.verticalLayout_4.addWidget(self.relatedLabel)

        self.relatedList = ListWidget(self.relatedWidget)
        self.relatedList.setObjectName(u"relatedList")
        self.relatedList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.relatedList.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.relatedList)


        self.verticalLayout_9.addWidget(self.relatedWidget)


        self.mangaVLayout.addLayout(self.verticalLayout_9)


        self.verticalLayout.addLayout(self.mangaVLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.itemsWidget = SimpleCardWidget(InfoPage)
        self.itemsWidget.setObjectName(u"itemsWidget")
        self.itemsVLayout = QVBoxLayout(self.itemsWidget)
        self.itemsVLayout.setSpacing(0)
        self.itemsVLayout.setObjectName(u"itemsVLayout")
        self.itemsVLayout.setContentsMargins(0, 0, 0, 0)
        self.itemsTree = TreeWidget(self.itemsWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.itemsTree.setHeaderItem(__qtreewidgetitem)
        self.itemsTree.setObjectName(u"itemsTree")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.itemsTree.sizePolicy().hasHeightForWidth())
        self.itemsTree.setSizePolicy(sizePolicy2)
        self.itemsTree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.itemsTree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.itemsTree.setWordWrap(True)
        self.itemsTree.header().setVisible(False)

        self.itemsVLayout.addWidget(self.itemsTree)


        self.horizontalLayout_4.addWidget(self.itemsWidget)


        self.retranslateUi(InfoPage)

        QMetaObject.connectSlotsByName(InfoPage)
    # setupUi

    def retranslateUi(self, InfoPage):
        self.name_label.setText(QCoreApplication.translate("InfoPage", u"name", None))
        self.russian_label.setText(QCoreApplication.translate("InfoPage", u"russian", None))
        self.status_label.setText(QCoreApplication.translate("InfoPage", u"status", None))
        self.catalog_score_label.setText(QCoreApplication.translate("InfoPage", u"score", None))
        self.volumes_label.setText(QCoreApplication.translate("InfoPage", u"volumes", None))
        self.chapters_label.setText(QCoreApplication.translate("InfoPage", u"chapters", None))
        self.charactersLabel.setText(QCoreApplication.translate("InfoPage", u"Characters", None))
        self.relatedLabel.setText(QCoreApplication.translate("InfoPage", u"Related", None))
        pass
    # retranslateUi

