from PySide6.QtCore import QLocale, QTranslator
from PySide6.QtWidgets import QApplication


class NlightTranslator(QTranslator):
    def __init__(self, locale: QLocale = None, parent=None) -> None:
        super().__init__(parent=parent)
        self.load(locale or QLocale())

    def load(self, locale: QLocale) -> None:
        super().load(f":/i18n/{locale.language().name}.qm")


def translate(context, string):
    return QApplication.translate(context, string, None)


__all__ = [
    "NlightTranslator",
    "translate",
]
