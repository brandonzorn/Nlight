from nlightreader.models.base_model import NamedBaseModel


class Kind(NamedBaseModel):
    pass


class Order(NamedBaseModel):
    pass


class Genre(NamedBaseModel):
    pass


class Status(NamedBaseModel):
    pass


__all__ = [
    "Kind",
    "Order",
    "Genre",
    "Status",
]
