from PySide6.QtCore import QLocale, QObject, QTranslator


class AppTranslator(QTranslator):
    def __init__(self, locale: QLocale, parent: QObject | None = None) -> None:
        super().__init__(parent=parent)
        self._load(locale)

    def _load(self, locale: QLocale) -> None:
        super().load(f":/i18n/{locale.language().name}.qm")


__all__ = ["AppTranslator"]
