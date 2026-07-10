from nlightreader.models.base_model import NamedContentModel


class Kind(NamedContentModel):
    pass


class Order(NamedContentModel):
    pass


class Genre(NamedContentModel):
    pass


class Status(NamedContentModel):
    pass


__all__ = [
    "Kind",
    "Order",
    "Genre",
    "Status",
]
