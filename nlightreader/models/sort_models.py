from nlightreader.models.base_model import NamedBaseModel


class Kind(NamedBaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ):
        super().__init__(content_id, catalog_id, name, russian)


class Order(NamedBaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ):
        super().__init__(content_id, catalog_id, name, russian)


class Genre(NamedBaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ):
        super().__init__(content_id, catalog_id, name, russian)


class Status(NamedBaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
    ):
        super().__init__(content_id, catalog_id, name, russian)
