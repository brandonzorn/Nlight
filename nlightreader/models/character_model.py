from typing import override

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
    ) -> None:
        super().__init__(content_id, catalog_id, name, russian)
        self.__description = description
        self.__role = role

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        if not isinstance(description, str):
            msg = f"Description must be a string, got {type(description)}"
            raise TypeError(msg)
        self.__description = description

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str) -> None:
        if not isinstance(role, str):
            msg = f"Role must be a string, got {type(role)}"
            raise TypeError(msg)
        self.__role = role

    @override
    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "description": self.__description,
                "role": self.__role,
            },
        )
        return data


__all__ = ["Character"]
