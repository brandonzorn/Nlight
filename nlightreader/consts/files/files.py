from enum import Enum

from qfluentwidgets import FluentIconBase, Theme, getIconColor

import nlight_res_rc


class LangIcons:
    Gb = ":/lang_icons/data/icons/lang/gb.svg"
    Ru = ":/lang_icons/data/icons/lang/ru.svg"
    Jp = ":/lang_icons/data/icons/lang/jp.svg"
    Ua = ":/lang_icons/data/icons/lang/ua.svg"


class Translations:
    En = ""
    Ru = ":/translations/data/translations/ru/ru.qm"
    Uk = ":/translations/data/translations/uk/uk.qm"


class Icons:
    App = ":/png_white/data/icons/icon.png"


class NlFluentIcons(FluentIconBase, Enum):
    """ Custom icons """

    SHIKIMORI = "shikimori"

    def path(self, theme=Theme.AUTO):
        return (f":/actions_{getIconColor(theme)}"
                f"/data/icons/buttons/svg_24dp_{getIconColor(theme)}/actions/{self.value}.svg")
