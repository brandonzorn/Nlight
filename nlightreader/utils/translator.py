from PySide6.QtCore import QLocale, QTranslator
from PySide6.QtWidgets import QApplication


class NlightTranslator(QTranslator):
    def __init__(self, locale: QLocale = None, parent=None):
        super().__init__(parent=parent)
        self.load(locale or QLocale())

    def load(self, locale: QLocale):
        super().load(f":/translations/i18n/{locale.name()}.qm")


def translate(context, string):
    """
    Translates a string using the current translation context.

    Args:
        context: The context in which the string appears.
        string: The string to be translated.

    Returns:
        A translated version of the input string.
    """
    return QApplication.translate(context, string, None)


__all__ = [
    "NlightTranslator",
    "translate",
]
