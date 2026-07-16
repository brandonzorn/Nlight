from typing import override

from sqlalchemy import inspect, text
from sqlalchemy.orm import Session

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
        for table in self.TABLES:
            session.execute(
                text(
                    f"""
                    ALTER TABLE {table}
                    ADD COLUMN created_at DATETIME
                    DEFAULT NULL
                    """,
                ),
            )

            session.execute(
                text(
                    f"""
                    ALTER TABLE {table}
                    ADD COLUMN updated_at DATETIME
                    DEFAULT NULL
                    """,
                ),
            )
