from PySide6.QtCore import QFile, QTextStream


def read_file(file: QFile):
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    return stream.readAll()


class Styles:
    Dark = read_file(QFile(u":/styles/data/styles/dark/widget_dark.qss")) +\
           read_file(QFile(u":/styles/data/styles/dark/icons_dark.qss"))

    Light = read_file(QFile(u":/styles/data/styles/light/widget_light.qss")) +\
            read_file(QFile(u":/styles/data/styles/light/icons_light.qss"))


class Fonts:
    SegoeUI = u":/fonts/data/fonts/SegoeUI.ttf"


class LangIcons:
    Gb = u":/lang_icons/data/icons/lang/gb.svg"
    Ru = u":/lang_icons/data/icons/lang/ru.svg"
    Jp = u":/lang_icons/data/icons/lang/jp.svg"
    Ua = u":/lang_icons/data/icons/lang/ua.svg"


class Translations:
    En = ""
    Ru = u":/translations/data/translations/ru/ru.qm"
    Uk = u":/translations/data/translations/uk/uk.qm"


class Icons:
    App = u":/png_white/data/icons/icon.png"
