from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

Entity = TypeVar("Entity")


class BaseRepository[Entity]:
    entity: type[Entity]

    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, entity: Entity) -> None:
        self._session.add(entity)

    def add_all(self, entities: list[Entity]) -> None:
        self._session.add_all(entities)

    def merge(self, entity: Entity) -> None:
        self._session.merge(entity)

    def remove(self, entity: Entity) -> None:
        self._session.delete(entity)

    def exists(self, pk: int | str) -> bool:
        return self.get(pk) is not None

    def get(self, pk: int | str) -> Entity | None:
        return self._session.get(self.entity, pk)

    def all(self) -> list[Entity]:
        return list(self._session.scalars(select(self.entity)))

    def find(self, *criteria: tuple) -> list[Entity]:
        stmt = select(self.entity).where(*criteria)
        return list(self._session.scalars(stmt))
