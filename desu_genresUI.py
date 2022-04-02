# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desu_genresUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(730, 329)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.g_parody = QCheckBox(Dialog)
        self.g_parody.setObjectName(u"g_parody")

        self.gridLayout.addWidget(self.g_parody, 4, 3, 1, 1)

        self.g_space = QCheckBox(Dialog)
        self.g_space.setObjectName(u"g_space")

        self.gridLayout.addWidget(self.g_space, 3, 1, 1, 1)

        self.g_color = QCheckBox(Dialog)
        self.g_color.setObjectName(u"g_color")

        self.gridLayout.addWidget(self.g_color, 0, 2, 1, 1)

        self.g_psychological = QCheckBox(Dialog)
        self.g_psychological.setObjectName(u"g_psychological")

        self.gridLayout.addWidget(self.g_psychological, 5, 2, 1, 1)

        self.g_adventure = QCheckBox(Dialog)
        self.g_adventure.setObjectName(u"g_adventure")

        self.gridLayout.addWidget(self.g_adventure, 5, 1, 1, 1)

        self.g_scifi = QCheckBox(Dialog)
        self.g_scifi.setObjectName(u"g_scifi")

        self.gridLayout.addWidget(self.g_scifi, 4, 2, 1, 1)

        self.g_isekai = QCheckBox(Dialog)
        self.g_isekai.setObjectName(u"g_isekai")

        self.gridLayout.addWidget(self.g_isekai, 2, 3, 1, 1)

        self.g_seinen = QCheckBox(Dialog)
        self.g_seinen.setObjectName(u"g_seinen")

        self.gridLayout.addWidget(self.g_seinen, 6, 3, 1, 1)

        self.g_supernatural = QCheckBox(Dialog)
        self.g_supernatural.setObjectName(u"g_supernatural")

        self.gridLayout.addWidget(self.g_supernatural, 6, 0, 1, 1)

        self.g_mecha = QCheckBox(Dialog)
        self.g_mecha.setObjectName(u"g_mecha")

        self.gridLayout.addWidget(self.g_mecha, 3, 4, 1, 1)

        self.g_hentai = QCheckBox(Dialog)
        self.g_hentai.setObjectName(u"g_hentai")

        self.gridLayout.addWidget(self.g_hentai, 8, 4, 1, 1)

        self.g_harem = QCheckBox(Dialog)
        self.g_harem.setObjectName(u"g_harem")

        self.gridLayout.addWidget(self.g_harem, 1, 0, 1, 1)

        self.g_shounenai = QCheckBox(Dialog)
        self.g_shounenai.setObjectName(u"g_shounenai")

        self.gridLayout.addWidget(self.g_shounenai, 7, 0, 1, 1)

        self.g_genderbender = QCheckBox(Dialog)
        self.g_genderbender.setObjectName(u"g_genderbender")

        self.gridLayout.addWidget(self.g_genderbender, 7, 1, 1, 1)

        self.g_fantasy = QCheckBox(Dialog)
        self.g_fantasy.setObjectName(u"g_fantasy")

        self.gridLayout.addWidget(self.g_fantasy, 8, 3, 1, 1)

        self.g_sliceoflife = QCheckBox(Dialog)
        self.g_sliceoflife.setObjectName(u"g_sliceoflife")

        self.gridLayout.addWidget(self.g_sliceoflife, 4, 4, 1, 1)

        self.g_romance = QCheckBox(Dialog)
        self.g_romance.setObjectName(u"g_romance")

        self.gridLayout.addWidget(self.g_romance, 5, 3, 1, 1)

        self.g_shoujo = QCheckBox(Dialog)
        self.g_shoujo.setObjectName(u"g_shoujo")

        self.gridLayout.addWidget(self.g_shoujo, 6, 1, 1, 1)

        self.g_yonkoma = QCheckBox(Dialog)
        self.g_yonkoma.setObjectName(u"g_yonkoma")

        self.gridLayout.addWidget(self.g_yonkoma, 2, 1, 1, 1)

        self.g_demons = QCheckBox(Dialog)
        self.g_demons.setObjectName(u"g_demons")

        self.gridLayout.addWidget(self.g_demons, 1, 2, 1, 1)

        self.g_thriller = QCheckBox(Dialog)
        self.g_thriller.setObjectName(u"g_thriller")

        self.gridLayout.addWidget(self.g_thriller, 8, 0, 1, 1)

        self.g_shounen = QCheckBox(Dialog)
        self.g_shounen.setObjectName(u"g_shounen")

        self.gridLayout.addWidget(self.g_shounen, 6, 4, 1, 1)

        self.g_horror = QCheckBox(Dialog)
        self.g_horror.setObjectName(u"g_horror")

        self.gridLayout.addWidget(self.g_horror, 8, 1, 1, 1)

        self.g_sports = QCheckBox(Dialog)
        self.g_sports.setObjectName(u"g_sports")

        self.gridLayout.addWidget(self.g_sports, 7, 2, 1, 1)

        self.g_martialarts = QCheckBox(Dialog)
        self.g_martialarts.setObjectName(u"g_martialarts")

        self.gridLayout.addWidget(self.g_martialarts, 0, 1, 1, 1)

        self.g_heroicfantasy = QCheckBox(Dialog)
        self.g_heroicfantasy.setObjectName(u"g_heroicfantasy")

        self.gridLayout.addWidget(self.g_heroicfantasy, 1, 1, 1, 1)

        self.g_vampire = QCheckBox(Dialog)
        self.g_vampire.setObjectName(u"g_vampire")

        self.gridLayout.addWidget(self.g_vampire, 0, 3, 1, 1)

        self.g_music = QCheckBox(Dialog)
        self.g_music.setObjectName(u"g_music")

        self.gridLayout.addWidget(self.g_music, 4, 1, 1, 1)

        self.g_yaoi = QCheckBox(Dialog)
        self.g_yaoi.setObjectName(u"g_yaoi")

        self.gridLayout.addWidget(self.g_yaoi, 9, 4, 1, 1)

        self.g_magic = QCheckBox(Dialog)
        self.g_magic.setObjectName(u"g_magic")

        self.gridLayout.addWidget(self.g_magic, 3, 3, 1, 1)

        self.g_mystic = QCheckBox(Dialog)
        self.g_mystic.setObjectName(u"g_mystic")

        self.gridLayout.addWidget(self.g_mystic, 4, 0, 1, 1)

        self.g_shoujoai = QCheckBox(Dialog)
        self.g_shoujoai.setObjectName(u"g_shoujoai")

        self.gridLayout.addWidget(self.g_shoujoai, 6, 2, 1, 1)

        self.g_samurai = QCheckBox(Dialog)
        self.g_samurai.setObjectName(u"g_samurai")

        self.gridLayout.addWidget(self.g_samurai, 5, 4, 1, 1)

        self.g_action = QCheckBox(Dialog)
        self.g_action.setObjectName(u"g_action")

        self.gridLayout.addWidget(self.g_action, 9, 1, 1, 1)

        self.g_tragedy = QCheckBox(Dialog)
        self.g_tragedy.setObjectName(u"g_tragedy")

        self.gridLayout.addWidget(self.g_tragedy, 7, 4, 1, 1)

        self.g_comedy = QCheckBox(Dialog)
        self.g_comedy.setObjectName(u"g_comedy")

        self.gridLayout.addWidget(self.g_comedy, 3, 0, 1, 1)

        self.g_litrpg = QCheckBox(Dialog)
        self.g_litrpg.setObjectName(u"g_litrpg")

        self.gridLayout.addWidget(self.g_litrpg, 3, 2, 1, 1)

        self.g_ecchi = QCheckBox(Dialog)
        self.g_ecchi.setObjectName(u"g_ecchi")

        self.gridLayout.addWidget(self.g_ecchi, 9, 2, 1, 1)

        self.g_historical = QCheckBox(Dialog)
        self.g_historical.setObjectName(u"g_historical")

        self.gridLayout.addWidget(self.g_historical, 2, 4, 1, 1)

        self.g_drama = QCheckBox(Dialog)
        self.g_drama.setObjectName(u"g_drama")

        self.gridLayout.addWidget(self.g_drama, 2, 0, 1, 1)

        self.g_mystery = QCheckBox(Dialog)
        self.g_mystery.setObjectName(u"g_mystery")

        self.gridLayout.addWidget(self.g_mystery, 1, 3, 1, 1)

        self.g_postapocalyptic = QCheckBox(Dialog)
        self.g_postapocalyptic.setObjectName(u"g_postapocalyptic")

        self.gridLayout.addWidget(self.g_postapocalyptic, 5, 0, 1, 1)

        self.g_fiction = QCheckBox(Dialog)
        self.g_fiction.setObjectName(u"g_fiction")

        self.gridLayout.addWidget(self.g_fiction, 8, 2, 1, 1)

        self.g_school = QCheckBox(Dialog)
        self.g_school.setObjectName(u"g_school")

        self.gridLayout.addWidget(self.g_school, 9, 0, 1, 1)

        self.g_dementia = QCheckBox(Dialog)
        self.g_dementia.setObjectName(u"g_dementia")

        self.gridLayout.addWidget(self.g_dementia, 0, 0, 1, 1)

        self.g_superpower = QCheckBox(Dialog)
        self.g_superpower.setObjectName(u"g_superpower")

        self.gridLayout.addWidget(self.g_superpower, 7, 3, 1, 1)

        self.g_web = QCheckBox(Dialog)
        self.g_web.setObjectName(u"g_web")

        self.gridLayout.addWidget(self.g_web, 0, 4, 1, 1)

        self.g_game = QCheckBox(Dialog)
        self.g_game.setObjectName(u"g_game")

        self.gridLayout.addWidget(self.g_game, 2, 2, 1, 1)

        self.g_josei = QCheckBox(Dialog)
        self.g_josei.setObjectName(u"g_josei")

        self.gridLayout.addWidget(self.g_josei, 1, 4, 1, 1)

        self.g_yuri = QCheckBox(Dialog)
        self.g_yuri.setObjectName(u"g_yuri")

        self.gridLayout.addWidget(self.g_yuri, 9, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.g_parody.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u0434\u0438\u044f", None))
        self.g_space.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0441\u043c\u043e\u0441", None))
        self.g_color.setText(QCoreApplication.translate("Dialog", u"\u0412 \u0446\u0432\u0435\u0442\u0435", None))
        self.g_psychological.setText(QCoreApplication.translate("Dialog", u"\u041f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435", None))
        self.g_adventure.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.g_scifi.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0443\u0447\u043d\u0430\u044f \u0444\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430", None))
        self.g_isekai.setText(QCoreApplication.translate("Dialog", u"\u0418\u0441\u0435\u043a\u0430\u0439", None))
        self.g_seinen.setText(QCoreApplication.translate("Dialog", u"\u0421\u0435\u0439\u043d\u0435\u043d", None))
        self.g_supernatural.setText(QCoreApplication.translate("Dialog", u"\u0421\u0432\u0435\u0440\u0445\u044a\u0435\u0441\u0442\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435", None))
        self.g_mecha.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0445\u0430", None))
        self.g_hentai.setText(QCoreApplication.translate("Dialog", u"\u0425\u0435\u043d\u0442\u0430\u0439", None))
        self.g_harem.setText(QCoreApplication.translate("Dialog", u"\u0413\u0430\u0440\u0435\u043c", None))
        self.g_shounenai.setText(QCoreApplication.translate("Dialog", u"\u0421\u0451\u043d\u0435\u043d \u0410\u0439", None))
        self.g_genderbender.setText(QCoreApplication.translate("Dialog", u"\u0421\u043c\u0435\u043d\u0430 \u043f\u043e\u043b\u0430", None))
        self.g_fantasy.setText(QCoreApplication.translate("Dialog", u"\u0424\u044d\u043d\u0442\u0435\u0437\u0438", None))
        self.g_sliceoflife.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0432\u0441\u0435\u0434\u043d\u0435\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.g_romance.setText(QCoreApplication.translate("Dialog", u"\u0420\u043e\u043c\u0430\u043d\u0442\u0438\u043a\u0430", None))
        self.g_shoujo.setText(QCoreApplication.translate("Dialog", u"\u0421\u0451\u0434\u0437\u0435", None))
        self.g_yonkoma.setText(QCoreApplication.translate("Dialog", u"\u0401\u043d\u043a\u043e\u043c\u0430", None))
        self.g_demons.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u043c\u043e\u043d\u044b", None))
        self.g_thriller.setText(QCoreApplication.translate("Dialog", u"\u0422\u0440\u0438\u043b\u043b\u0435\u0440", None))
        self.g_shounen.setText(QCoreApplication.translate("Dialog", u"\u0421\u0451\u043d\u0435\u043d", None))
        self.g_horror.setText(QCoreApplication.translate("Dialog", u"\u0423\u0436\u0430\u0441\u044b", None))
        self.g_sports.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043e\u0440\u0442", None))
        self.g_martialarts.setText(QCoreApplication.translate("Dialog", u"\u0411\u043e\u0435\u0432\u044b\u0435 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0430", None))
        self.g_heroicfantasy.setText(QCoreApplication.translate("Dialog", u"\u0413\u0435\u0440\u043e\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0444\u044d\u043d\u0442\u0435\u0437\u0438", None))
        self.g_vampire.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u043c\u043f\u0438\u0440\u044b", None))
        self.g_music.setText(QCoreApplication.translate("Dialog", u"\u041c\u0443\u0437\u044b\u043a\u0430", None))
        self.g_yaoi.setText(QCoreApplication.translate("Dialog", u"\u042f\u043e\u0439", None))
        self.g_magic.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0433\u0438\u044f", None))
        self.g_mystic.setText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.g_shoujoai.setText(QCoreApplication.translate("Dialog", u"\u0421\u0451\u0434\u0437\u0435 \u0410\u0439", None))
        self.g_samurai.setText(QCoreApplication.translate("Dialog", u"\u0421\u0430\u043c\u0443\u0440\u0430\u0438", None))
        self.g_action.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0448\u0435\u043d", None))
        self.g_tragedy.setText(QCoreApplication.translate("Dialog", u"\u0422\u0440\u0430\u0433\u0435\u0434\u0438\u044f", None))
        self.g_comedy.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0435\u0434\u0438\u044f", None))
        self.g_litrpg.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u0442RPG", None))
        self.g_ecchi.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0442\u0438", None))
        self.g_historical.setText(QCoreApplication.translate("Dialog", u"\u0418\u0441\u0442\u043e\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.g_drama.setText(QCoreApplication.translate("Dialog", u"\u0414\u0440\u0430\u043c\u0430", None))
        self.g_mystery.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432", None))
        self.g_postapocalyptic.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u0442\u0430\u043f\u043e\u043a\u0430\u043b\u0438\u043f\u0442\u0438\u043a\u0430", None))
        self.g_fiction.setText(QCoreApplication.translate("Dialog", u"\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430", None))
        self.g_school.setText(QCoreApplication.translate("Dialog", u"\u0428\u043a\u043e\u043b\u0430", None))
        self.g_dementia.setText(QCoreApplication.translate("Dialog", u"\u0411\u0435\u0437\u0443\u043c\u0438\u0435", None))
        self.g_superpower.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043f\u0435\u0440 \u0441\u0438\u043b\u0430", None))
        self.g_web.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0431", None))
        self.g_game.setText(QCoreApplication.translate("Dialog", u"\u0418\u0433\u0440\u044b", None))
        self.g_josei.setText(QCoreApplication.translate("Dialog", u"\u0414\u0437\u0451\u0441\u0435\u0439", None))
        self.g_yuri.setText(QCoreApplication.translate("Dialog", u"\u042e\u0440\u0438", None))
    # retranslateUi

