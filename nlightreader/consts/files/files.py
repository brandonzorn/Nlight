from enum import Enum, StrEnum

from qfluentwidgets import FluentIconBase, getIconColor, Theme


class LangIcons(StrEnum):
    GB = ":/icons/flags/gb.svg"
    RU = ":/icons/flags/ru.svg"
    JP = ":/icons/flags/jp.svg"
    UA = ":/icons/flags/ua.svg"


class Icons(StrEnum):
    APP = ":/icons/common/app-icon.png"


class NlFluentIcons(FluentIconBase, Enum):
    SHIKIMORI = "shikimori"

    def path(self, theme: Theme = Theme.AUTO) -> str:
        return f":/icons/{getIconColor(theme)}/{self.value}.svg"


__all__ = [
    "Icons",
    "LangIcons",
    "NlFluentIcons",
]
