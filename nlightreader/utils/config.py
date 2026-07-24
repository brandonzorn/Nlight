from enum import Enum
import sys

from PySide6.QtCore import QLocale
from qfluentwidgets import (
    BoolValidator,
    ConfigItem,
    ConfigSerializer,
    OptionsConfigItem,
    OptionsValidator,
    QConfig,
    qconfig,
    Theme,
)

from nlightreader.consts.paths.paths import APP_DATA_PATH


def is_win11() -> bool:
    return sys.platform == "win32" and sys.getwindowsversion().build >= 22000


class Language(Enum):
    RUSSIAN = QLocale(QLocale.Language.Russian)
    UKRAINIAN = QLocale(QLocale.Language.Ukrainian)
    ENGLISH = QLocale(QLocale.Language.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    def serialize(self, value: Language) -> str:
        return value.value.name() if value != Language.AUTO else "Auto"

    def deserialize(self, value: str) -> Language:
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


class Config(QConfig):
    dpi_scale = OptionsConfigItem(
        "MainWindow",
        "DpiScale",
        "Auto",
        OptionsValidator(
            [
                1,
                1.25,
                1.5,
                1.75,
                2,
                "Auto",
            ],
        ),
        restart=True,
    )
    language = OptionsConfigItem(
        "MainWindow",
        "Language",
        Language.ENGLISH,
        OptionsValidator(Language),
        LanguageSerializer(),
        restart=True,
    )
    mica_enabled = ConfigItem(
        "MainWindow",
        "MicaEnabled",
        is_win11(),
        BoolValidator(),
    )
    check_updates_at_startup = ConfigItem(
        "Update",
        "CheckUpdateAtStartUp",
        True,
        BoolValidator(),
    )
    enable_kodik_metrics = ConfigItem(
        "Utils",
        "EnableKodikMetrics",
        False,
        BoolValidator(),
        restart=True,
    )


cfg = Config()
cfg.themeMode.value = Theme.AUTO
qconfig.load(APP_DATA_PATH / "config.json", cfg)


__all__ = ["cfg"]
