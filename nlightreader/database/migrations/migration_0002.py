from datetime import datetime
from typing import override

from sqlalchemy import Column, DateTime, inspect, text
from sqlalchemy.orm import Session
from sqlalchemy.sql.ddl import CreateColumn

from .base import Migration


class TimestampMigration(Migration):
    version = 2

    TABLES = (
        "manga",
        "chapters",
        "chapter_history",
        "library",
    )

    @override
    def is_applicable(self, session: Session) -> bool:
        inspector = inspect(session.bind)

        for table in self.TABLES:
            columns = {
                column["name"] for column in inspector.get_columns(table)
            }

            if "created_at" not in columns and "updated_at" not in columns:
                return True

        return False

    @override
    def upgrade(self, session: Session) -> None:
        created_at_ddl = CreateColumn(
            Column(
                "created_at",
                DateTime(timezone=True),
                default=datetime.now,
            ),
        ).compile(bind=session.bind)

        updated_at_ddl = CreateColumn(
            Column(
                "updated_at",
                DateTime(timezone=True),
                default=datetime.now,
                onupdate=datetime.now,
            ),
        ).compile(bind=session.bind)

        for table in self.TABLES:
            session.execute(
                text(f"ALTER TABLE {table} ADD COLUMN {created_at_ddl}"),
            )
            session.execute(
                text(f"ALTER TABLE {table} ADD COLUMN {updated_at_ddl}"),
            )
