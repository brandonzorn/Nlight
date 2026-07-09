from PySide6.QtCore import QLocale, QObject, QTranslator
from PySide6.QtWidgets import QApplication


class AppTranslator(QTranslator):
    def __init__(self, locale: QLocale, parent: QObject | None = None) -> None:
        super().__init__(parent=parent)
        self._load(locale)

    def _load(self, locale: QLocale) -> None:
        super().load(f":/i18n/{locale.language().name}.qm")


def translate(context: str, string: str) -> str:
    return QApplication.translate(context, string, None)


__all__ = [
    "AppTranslator",
    "translate",
]
