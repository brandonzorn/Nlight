from nlightreader.models.base_model import NamedBaseModel


class Character(NamedBaseModel):
    def __init__(
        self,
        content_id: str,
        catalog_id: int,
        name: str,
        russian: str,
        description: str,
        role: str,
    ):
        super().__init__(content_id, catalog_id, name, russian)
        self.description = description
        self.role = role

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        if not isinstance(description, str):
            raise TypeError(
                f"Description must be a string got {type(description)}",
            )
        self.__description = description

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role: str):
        if not isinstance(role, str):
            raise TypeError(f"Role must be a string got {type(role)}")
        self.__role = role
