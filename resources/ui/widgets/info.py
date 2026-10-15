# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QListWidgetItem, QSizePolicy, QSpacerItem, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, ImageLabel,
    ListWidget, SimpleCardWidget, SingleDirectionScrollArea, TextBrowser,
    ToolButton, TreeWidget)

class Ui_InfoPage(object):
    def setupUi(self, InfoPage):
        if not InfoPage.objectName():
            InfoPage.setObjectName(u"InfoPage")
        InfoPage.resize(640, 480)
        InfoPage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pageLayout = QHBoxLayout(InfoPage)
        self.pageLayout.setSpacing(0)
        self.pageLayout.setObjectName(u"pageLayout")
        self.pageLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SingleDirectionScrollArea(InfoPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 356, 984))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaVLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaVLayout.setObjectName(u"scrollAreaVLayout")
        self.scrollAreaVLayout.setContentsMargins(6, 6, 9, 6)
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
        self.horizontalLayout_2 = QHBoxLayout(self.shikimoriWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.shikimoriButton = ToolButton(self.shikimoriWidget)
        self.shikimoriButton.setObjectName(u"shikimoriButton")

        self.horizontalLayout_2.addWidget(self.shikimoriButton)


        self.headerContentVLayout.addWidget(self.shikimoriWidget)


        self.headerHLayout.addLayout(self.headerContentVLayout)


        self.scrollAreaVLayout.addWidget(self.headerWidget)

        self.infoWidget = QWidget(self.scrollAreaWidgetContents)
        self.infoWidget.setObjectName(u"infoWidget")
        self.infoHLayout = QHBoxLayout(self.infoWidget)
        self.infoHLayout.setObjectName(u"infoHLayout")
        self.infoHLayout.setContentsMargins(0, 0, 0, 0)
        self.previewWidget = SimpleCardWidget(self.infoWidget)
        self.previewWidget.setObjectName(u"previewWidget")
        self.previewLayout = QVBoxLayout(self.previewWidget)
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLabel = ImageLabel(self.previewWidget)
        self.imageLabel.setObjectName(u"imageLabel")

        self.previewLayout.addWidget(self.imageLabel)


        self.infoHLayout.addWidget(self.previewWidget)

        self.titleWidget = SimpleCardWidget(self.infoWidget)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.titleWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.name_label = BodyLabel(self.titleWidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.name_label)

        self.russian_label = BodyLabel(self.titleWidget)
        self.russian_label.setObjectName(u"russian_label")

        self.verticalLayout_8.addWidget(self.russian_label)

        self.status_label = BodyLabel(self.titleWidget)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout_8.addWidget(self.status_label)

        self.catalog_score_label = BodyLabel(self.titleWidget)
        self.catalog_score_label.setObjectName(u"catalog_score_label")

        self.verticalLayout_8.addWidget(self.catalog_score_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.volumes_label = BodyLabel(self.titleWidget)
        self.volumes_label.setObjectName(u"volumes_label")

        self.verticalLayout_8.addWidget(self.volumes_label)

        self.chapters_label = BodyLabel(self.titleWidget)
        self.chapters_label.setObjectName(u"chapters_label")

        self.verticalLayout_8.addWidget(self.chapters_label)


        self.infoHLayout.addWidget(self.titleWidget)


        self.scrollAreaVLayout.addWidget(self.infoWidget)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.descriptionCard = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.descriptionCard.setObjectName(u"descriptionCard")
        self.descriptionVLayout = QVBoxLayout(self.descriptionCard)
        self.descriptionVLayout.setObjectName(u"descriptionVLayout")
        self.descriptionVLayout.setContentsMargins(0, 0, 0, 0)
        self.descriptionHeaderHLayout = QHBoxLayout()
        self.descriptionHeaderHLayout.setObjectName(u"descriptionHeaderHLayout")
        self.descriptionLabel = BodyLabel(self.descriptionCard)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.descriptionHeaderHLayout.addWidget(self.descriptionLabel)


        self.descriptionVLayout.addLayout(self.descriptionHeaderHLayout)

        self.descriptionText = TextBrowser(self.descriptionCard)
        self.descriptionText.setObjectName(u"descriptionText")
        self.descriptionText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.descriptionText.setReadOnly(True)

        self.descriptionVLayout.addWidget(self.descriptionText)


        self.verticalLayout_9.addWidget(self.descriptionCard)

        self.charactersWidget = CardWidget(self.scrollAreaWidgetContents)
        self.charactersWidget.setObjectName(u"charactersWidget")
        self.charactersVLayout = QVBoxLayout(self.charactersWidget)
        self.charactersVLayout.setObjectName(u"charactersVLayout")
        self.charactersVLayout.setContentsMargins(0, 0, 0, 0)
        self.charactersHeaderHLayout = QHBoxLayout()
        self.charactersHeaderHLayout.setObjectName(u"charactersHeaderHLayout")
        self.charactersLabel = BodyLabel(self.charactersWidget)
        self.charactersLabel.setObjectName(u"charactersLabel")

        self.charactersHeaderHLayout.addWidget(self.charactersLabel)


        self.charactersVLayout.addLayout(self.charactersHeaderHLayout)

        self.charactersList = ListWidget(self.charactersWidget)
        self.charactersList.setObjectName(u"charactersList")
        sizePolicy1.setHeightForWidth(self.charactersList.sizePolicy().hasHeightForWidth())
        self.charactersList.setSizePolicy(sizePolicy1)
        self.charactersList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.charactersList.setWordWrap(True)

        self.charactersVLayout.addWidget(self.charactersList)


        self.verticalLayout_9.addWidget(self.charactersWidget)

        self.relatedWidget = CardWidget(self.scrollAreaWidgetContents)
        self.relatedWidget.setObjectName(u"relatedWidget")
        self.relatedVLayout = QVBoxLayout(self.relatedWidget)
        self.relatedVLayout.setObjectName(u"relatedVLayout")
        self.relatedVLayout.setContentsMargins(0, 0, 0, 0)
        self.relatedHeaderHLayout = QHBoxLayout()
        self.relatedHeaderHLayout.setObjectName(u"relatedHeaderHLayout")
        self.relatedLabel = BodyLabel(self.relatedWidget)
        self.relatedLabel.setObjectName(u"relatedLabel")

        self.relatedHeaderHLayout.addWidget(self.relatedLabel)


        self.relatedVLayout.addLayout(self.relatedHeaderHLayout)

        self.relatedList = ListWidget(self.relatedWidget)
        self.relatedList.setObjectName(u"relatedList")
        sizePolicy1.setHeightForWidth(self.relatedList.sizePolicy().hasHeightForWidth())
        self.relatedList.setSizePolicy(sizePolicy1)
        self.relatedList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.relatedList.setWordWrap(True)

        self.relatedVLayout.addWidget(self.relatedList)


        self.verticalLayout_9.addWidget(self.relatedWidget)


        self.scrollAreaVLayout.addLayout(self.verticalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.scrollAreaVLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.pageLayout.addWidget(self.scrollArea)

        self.itemsWidget = QWidget(InfoPage)
        self.itemsWidget.setObjectName(u"itemsWidget")
        self.itemsWidgetVLayout = QVBoxLayout(self.itemsWidget)
        self.itemsWidgetVLayout.setObjectName(u"itemsWidgetVLayout")
        self.itemsWidgetVLayout.setContentsMargins(6, 6, 6, 6)
        self.itemsCard = CardWidget(self.itemsWidget)
        self.itemsCard.setObjectName(u"itemsCard")
        self.itemsCardVLayout = QVBoxLayout(self.itemsCard)
        self.itemsCardVLayout.setObjectName(u"itemsCardVLayout")
        self.itemsCardVLayout.setContentsMargins(0, 0, 0, 0)
        self.itemsTree = TreeWidget(self.itemsCard)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.itemsTree.setHeaderItem(__qtreewidgetitem)
        self.itemsTree.setObjectName(u"itemsTree")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.itemsTree.sizePolicy().hasHeightForWidth())
        self.itemsTree.setSizePolicy(sizePolicy2)
        self.itemsTree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.itemsTree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.itemsTree.setWordWrap(True)
        self.itemsTree.header().setVisible(False)

        self.itemsCardVLayout.addWidget(self.itemsTree)


        self.itemsWidgetVLayout.addWidget(self.itemsCard)


        self.pageLayout.addWidget(self.itemsWidget)


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
        self.descriptionLabel.setText(QCoreApplication.translate("InfoPage", u"Description", None))
        self.charactersLabel.setText(QCoreApplication.translate("InfoPage", u"Characters", None))
        self.relatedLabel.setText(QCoreApplication.translate("InfoPage", u"Related", None))
        pass
    # retranslateUi

