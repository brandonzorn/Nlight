from abc import ABC
from typing import Any


class ParserItems(ABC):
    ORDERS: tuple[dict[str, Any], ...] = ()
    KINDS: tuple[dict[str, Any], ...] = ()
    GENRES: tuple[dict[str, Any], ...] = ()


__all__ = ["ParserItems"]
