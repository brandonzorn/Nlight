from enum import Enum

from qfluentwidgets import FluentIconBase, Theme, getIconColor

import nlight_res_rc

from PySide6.QtCore import QFile, QTextStream


def read_file(file: QFile):
    file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    stream = QTextStream(file)
    return stream.readAll()


class Styles:
    default_widgets = read_file(QFile(":/styles/data/styles/default/widget_default.qss"))

    dark_icons = read_file(QFile(":/styles/data/styles/dark/icons_dark.qss"))
    dark_widgets = read_file(QFile(":/styles/data/styles/dark/widget_dark.qss"))
    Dark = dark_icons + default_widgets + dark_widgets

    light_icons = read_file(QFile(":/styles/data/styles/light/icons_light.qss"))
    light_widgets = read_file(QFile(":/styles/data/styles/light/widget_light.qss"))
    Light = light_icons + default_widgets + light_widgets


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
