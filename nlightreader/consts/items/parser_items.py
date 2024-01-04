from abc import ABC


class ParserItems(ABC):
    GENRES: list[dict[str, str]] = []
    ORDERS: list[dict[str, str]] = []
    KINDS: list[dict[str, str]] = []
