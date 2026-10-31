from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

Entity = TypeVar("Entity")


class BaseRepository[Entity]:
    entity: type[Entity]

    def __init__(self, session: Session) -> None:
        self._session = session

    def _add(self, entity: Entity) -> None:
        self._session.add(entity)

    def _add_many(self, entities: list[Entity]) -> None:
        self._session.add_all(entities)

    def _merge(self, entity: Entity) -> None:
        self._session.merge(entity)

    def _merge_many(self, entities: list[Entity]) -> None:
        self._session.merge_all(entities)

    def _remove(self, entity: Entity) -> None:
        self._session.delete(entity)

    def _remove_many(self, entities: list[Entity]) -> None:
        self._session.delete_all(entities)

    def _get(self, pk: int | str) -> Entity | None:
        return self._session.get(self.entity, pk)

    def exists(self, pk: int | str) -> bool:
        return self._get(pk) is not None

    def _all(self) -> list[Entity]:
        return list(self._session.scalars(select(self.entity)))

    def _find(self, *criteria: tuple) -> list[Entity]:
        stmt = select(self.entity).where(*criteria)
        return list(self._session.scalars(stmt))
