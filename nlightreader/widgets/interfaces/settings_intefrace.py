from qfluentwidgets import (
    BodyLabel,
    ExpandLayout,
    HyperlinkCard,
    InfoBar,
    OptionsSettingCard,
    PrimaryPushSettingCard,
    ScrollArea,
    SettingCardGroup,
    SwitchSettingCard,
)
from qfluentwidgets import FluentIcon
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget
from nlightreader.consts.app import APP_VERSION
from nlightreader.utils.config import cfg


class SettingsInterface(ScrollArea):
    check_for_updates_signal = Signal()
    theme_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("SettingsInterface")
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.setStyleSheet(
            """
            QWidget {background: transparent;}
            QScrollArea {border: none;}
            BodyLabel {font: 33px 'Microsoft YaHei Light';}
            """,
        )
        self.settingLabel = BodyLabel(
            self.tr("Settings"),
            self,
        )

        self.personalGroup = SettingCardGroup(
            self.tr("Personalization"),
            self.scrollWidget,
        )
        self.themeCard = OptionsSettingCard(
            cfg.theme_mode,
            FluentIcon.BRUSH,
            self.tr("Application theme"),
            self.tr("Change the appearance of application"),
            texts=[
                self.tr("Light"),
                self.tr("Dark"),
                self.tr("Use system setting"),
            ],
            parent=self.personalGroup,
        )
        self.zoomCard = OptionsSettingCard(
            cfg.dpi_scale,
            FluentIcon.ZOOM,
            self.tr("Interface zoom"),
            self.tr("Change the size of widgets and fonts"),
            texts=[
                "100%",
                "125%",
                "150%",
                "175%",
                "200%",
                self.tr("Use system setting"),
            ],
            parent=self.personalGroup,
        )
        self.languageCard = OptionsSettingCard(
            cfg.language,
            FluentIcon.LANGUAGE,
            self.tr("Language"),
            self.tr("Set your preferred language for UI"),
            texts=[
                "Русский",
                "Українська",
                "English",
                self.tr("Use system setting"),
            ],
            parent=self.personalGroup,
        )

        self.utilsSoftwareGroup = SettingCardGroup(
            self.tr("Episodes"),
            self.scrollWidget,
        )
        self.enableKodikServerCard = SwitchSettingCard(
            FluentIcon.ACCEPT,
            self.tr(
                "Automatically mark episodes as watched",
            ),
            configItem=cfg.enable_kodik_server,
            parent=self.utilsSoftwareGroup,
        )

        self.updateSoftwareGroup = SettingCardGroup(
            self.tr("Software update"),
            self.scrollWidget,
        )
        self.updateOnStartUpCard = SwitchSettingCard(
            FluentIcon.UPDATE,
            self.tr(
                "Check for updates when the application starts",
            ),
            self.tr(
                "The new version will be more stable and have more features",
            ),
            configItem=cfg.check_updates_at_startup,
            parent=self.updateSoftwareGroup,
        )

        self.aboutGroup = SettingCardGroup(
            self.tr("About"),
            self.scrollWidget,
        )
        self.projectCard = HyperlinkCard(
            "https://github.com/brandonzorn/Nlight/",
            self.tr("Project on GitHub"),
            FluentIcon.GITHUB,
            self.tr("Project on GitHub"),
            self.tr(
                "",
            ),
            self.aboutGroup,
        )
        self.aboutCard = PrimaryPushSettingCard(
            self.tr("Check for updates"),
            FluentIcon.INFO,
            self.tr("About"),
            f"© 2022 brandonzorn. {self.tr('Version')} {APP_VERSION}",
            self.aboutGroup,
        )

        self.__init_widget()

    def setup(self):
        pass

    def __init_widget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff,
        )
        self.setViewportMargins(0, 120, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        self.__init_layout()
        self.__connect_signals()

    def __init_layout(self):
        self.settingLabel.move(60, 63)

        self.personalGroup.addSettingCard(self.themeCard)
        self.personalGroup.addSettingCard(self.zoomCard)
        self.personalGroup.addSettingCard(self.languageCard)

        self.utilsSoftwareGroup.addSettingCard(self.enableKodikServerCard)

        self.updateSoftwareGroup.addSettingCard(self.updateOnStartUpCard)

        self.aboutGroup.addSettingCard(self.projectCard)
        self.aboutGroup.addSettingCard(self.aboutCard)

        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(60, 10, 60, 0)
        self.expandLayout.addWidget(self.personalGroup)
        self.expandLayout.addWidget(self.utilsSoftwareGroup)
        self.expandLayout.addWidget(self.updateSoftwareGroup)
        self.expandLayout.addWidget(self.aboutGroup)

    def __show_restart_tooltip(self):
        InfoBar.warning(
            "",
            self.tr(
                "Changes will take effect after restarting the application",
            ),
            parent=self.window(),
        )

    def __connect_signals(self):
        cfg.appRestartSig.connect(self.__show_restart_tooltip)
        self.aboutCard.clicked.connect(self.check_for_updates_signal)
        self.themeCard.optionChanged.connect(self.theme_changed)
