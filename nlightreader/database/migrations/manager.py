from sqlalchemy import insert
from sqlalchemy.orm import Session

from nlightreader.database.entities import SchemaVersionEntity

from .migration_0001 import InitialMigration
from .migration_0002 import TimestampMigration


class MigrationManager:
    def __init__(self) -> None:
        self._migrations = (
            InitialMigration(),
            TimestampMigration(),
        )

    def migrate(self, session: Session) -> None:
        entity = session.get(SchemaVersionEntity, 1)
        if not entity:
            session.execute(
                insert(SchemaVersionEntity).values(id=1, version=0),
            )
            session.commit()

        for migration in self._migrations:
            entity = session.get(SchemaVersionEntity, 1)
            if not entity:
                break
            if entity.version >= migration.version:
                continue
            if migration.is_applicable(session):
                migration.upgrade(session)
            migration.upgrade_scheme(session)
            session.commit()
