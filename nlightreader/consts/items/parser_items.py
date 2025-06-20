from abc import ABC


class ParserItems(ABC):
    ORDERS: list[dict[str, str]] = []
    KINDS: list[dict[str, str]] = []
    GENRES: list[dict[str, str]] = []


__all__ = [
    "ParserItems",
]
