from abc import ABC


class ParserItems(ABC):
    ORDERS: tuple[dict[str, str], ...] = ()
    KINDS: tuple[dict[str, str], ...] = ()
    GENRES: tuple[dict[str, str], ...] = ()


__all__ = ["ParserItems"]
