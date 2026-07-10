from typing import override

from nlightreader.models.base_model import NamedContentModel


class Character(NamedContentModel):
    description: str
    role: str

    @override
    def to_dict(self) -> dict:
        return self.model_dump()


__all__ = ["Character"]
