from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget
from qfluentwidgets import (
    ExpandLayout,
    FluentIcon,
    HyperlinkCard,
    InfoBar,
    OptionsSettingCard,
    PrimaryPushSettingCard,
    setTheme,
    SettingCardGroup,
    SingleDirectionScrollArea,
    SwitchSettingCard,
    TitleLabel,
)

from nlightreader.consts.app import APP_VERSION
from nlightreader.consts.urls import GITHUB_REPO
from nlightreader.utils.config import cfg


class SettingsPage(SingleDirectionScrollArea):
    check_for_updates_signal = Signal()
    mica_enable_changed = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.setObjectName("SettingsPage")
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.settingLabel = TitleLabel(self.tr("Settings"), self)

        self.personalGroup = SettingCardGroup(
            self.tr("Personalization"),
            self.scrollWidget,
        )
        self.micaCard = SwitchSettingCard(
            FluentIcon.TRANSPARENT,
            self.tr("Mica effect"),
            self.tr("Apply semi transparent to windows and surfaces"),
            cfg.mica_enabled,
            self.personalGroup,
        )
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
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
            configItem=cfg.enable_kodik_metrics,
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
            GITHUB_REPO,
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

        self._init_widget()
        self.enableTransparentBackground()

    def setup(self) -> None:
        pass

    def _init_widget(self) -> None:
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff,
        )
        self.setViewportMargins(0, 120, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        self._init_layout()
        self._connect_signals()

    def _init_layout(self) -> None:
        self.settingLabel.move(60, 63)

        self.personalGroup.addSettingCard(self.themeCard)
        self.personalGroup.addSettingCard(self.micaCard)
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

    def _show_restart_tooltip(self) -> None:
        InfoBar.warning(
            "",
            self.tr(
                "Changes will take effect after restarting the application",
            ),
            parent=self.window(),
        )

    def show_no_updates_tooltip(self) -> None:
        InfoBar.success(
            title=self.tr("Checking for updates."),
            content=self.tr(
                "No updates available. You are using the latest version.",
            ),
            duration=3500,
            parent=self,
        )

    def show_has_updates_tooltip(self, result: str) -> None:
        InfoBar.info(
            title=self.tr("Checking for updates."),
            content=self.tr(
                "New version {result} is available! "
                "You are currently on version {APP_VERSION}.",
            ).format(result=result, APP_VERSION=APP_VERSION),
            duration=3500,
            parent=self,
        )

    def show_err_updates_tooltip(self) -> None:
        InfoBar.error(
            title=self.tr("Checking for updates."),
            content=self.tr(
                "Error checking for updates.",
            ),
            duration=3500,
            parent=self,
        )

    def _connect_signals(self) -> None:
        cfg.appRestartSig.connect(self._show_restart_tooltip)
        cfg.themeChanged.connect(setTheme)
        self.micaCard.checkedChanged.connect(self.mica_enable_changed)
        self.aboutCard.clicked.connect(self.check_for_updates_signal)


__all__ = ["SettingsPage"]
