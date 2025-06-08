from enum import Enum

from PySide6.QtCore import QLocale
from qfluentwidgets import (
    BoolValidator,
    ConfigItem,
    ConfigSerializer,
    OptionsConfigItem,
    OptionsValidator,
    QConfig,
    qconfig,
)

from nlightreader.consts.paths.paths import APP_DATA_PATH


class Language(Enum):
    RUSSIAN = QLocale(QLocale.Language.Russian)
    UKRAINIAN = QLocale(QLocale.Language.Ukrainian)
    ENGLISH = QLocale(QLocale.Language.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


class Config(QConfig):
    theme_mode = OptionsConfigItem(
        "MainWindow",
        "ThemeMode",
        "Auto",
        OptionsValidator(
            [
                "Light",
                "Dark",
                "Auto",
            ],
        ),
    )
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
    check_updates_at_startup = ConfigItem(
        "Update",
        "CheckUpdateAtStartUp",
        True,
        BoolValidator(),
    )
    enable_kodik_server = ConfigItem(
        "Utils",
        "EnableKodikServer",
        True,
        BoolValidator(),
        restart=True,
    )


cfg = Config()
qconfig.load(APP_DATA_PATH / "config.json", cfg)
