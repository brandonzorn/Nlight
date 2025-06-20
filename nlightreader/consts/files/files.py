from enum import Enum

from qfluentwidgets import FluentIconBase, getIconColor, Theme


class LangIcons:
    Gb = ":/lang_icons/icons/lang/gb.svg"
    Ru = ":/lang_icons/icons/lang/ru.svg"
    Jp = ":/lang_icons/icons/lang/jp.svg"
    Ua = ":/lang_icons/icons/lang/ua.svg"


class Icons:
    App = ":/png_white/icons/icon.png"


class NlFluentIcons(FluentIconBase, Enum):
    """Custom icons"""

    SHIKIMORI = "shikimori"

    def path(self, theme=Theme.AUTO):
        return (
            f":/actions_{getIconColor(theme)}"
            f"/icons/buttons/svg_24dp_{getIconColor(theme)}"
            f"/actions/{self.value}.svg"
        )


__all__ = [
    "Icons",
    "LangIcons",
    "NlFluentIcons",
]
