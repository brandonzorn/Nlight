from PySide6.QtGui import QColor
from qfluentwidgets import FluentIcon


class ItemsIcons:
    READ = FluentIcon.ACCEPT_MEDIUM
    UNREAD = FluentIcon.ACCEPT_MEDIUM.colored(
        lightColor=QColor("RED"),
        darkColor=QColor("RED"),
    )


__all__ = [
    "ItemsIcons",
]
