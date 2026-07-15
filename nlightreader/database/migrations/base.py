from abc import ABC, abstractmethod

from sqlalchemy import update
from sqlalchemy.orm import Session

from nlightreader.database.entities import SchemaVersionEntity


class Migration(ABC):
    version: int

    @abstractmethod
    def is_applicable(self, session: Session) -> bool:
        pass

    @abstractmethod
    def upgrade(self, session: Session) -> None:
        pass

    def upgrade_scheme(self, session: Session) -> None:
        session.execute(
            update(SchemaVersionEntity)
            .where(SchemaVersionEntity.id == 1)
            .values(version=self.version),
        )
