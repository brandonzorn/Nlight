from PySide6.QtCore import QFile, QTextStream


def read_file(file: QFile):
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    return stream.readAll()


class Styles:
    default_widgets = read_file(QFile(u":/styles/data/styles/default/widget_default.qss"))

    dark_icons = read_file(QFile(u":/styles/data/styles/dark/icons_dark.qss"))
    dark_widgets = read_file(QFile(u":/styles/data/styles/dark/widget_dark.qss"))
    Dark = dark_icons + default_widgets + dark_widgets

    light_icons = read_file(QFile(u":/styles/data/styles/light/icons_light.qss"))
    light_widgets = read_file(QFile(u":/styles/data/styles/light/widget_light.qss"))
    Light = light_icons + default_widgets + light_widgets


class LangIcons:
    Gb = u":/lang_icons/data/icons/lang/gb.svg"
    Ru = u":/lang_icons/data/icons/lang/ru.svg"
    Jp = u":/lang_icons/data/icons/lang/jp.svg"
    Ua = u":/lang_icons/data/icons/lang/ua.svg"


class Translations:
    En = ""
    Ru = u":/translations/data/translations/ru/ru_RU.qm"
    Uk = u":/translations/data/translations/uk/uk_UA.qm"


class Icons:
    App = u":/png_white/data/icons/icon.png"
