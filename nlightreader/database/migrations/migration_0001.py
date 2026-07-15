from typing import override

from sqlalchemy import inspect, text
from sqlalchemy.orm import Session

from .base import Migration


class InitialMigration(Migration):
    version = 1

    @override
    def is_applicable(self, session: Session) -> bool:
        inspector = inspect(session.bind)

        manga_columns = [c["name"] for c in inspector.get_columns("manga")]
        chapters_columns = [
            c["name"] for c in inspector.get_columns("chapters")
        ]

        return bool(
            "preview_url" not in manga_columns
            and "translator" not in chapters_columns,
        )

    @override
    def upgrade(self, session: Session) -> None:
        session.execute(
            text(
                """ALTER TABLE manga ADD COLUMN preview_url TEXT""",
            ),
        )
        session.execute(
            text(
                """ALTER TABLE chapters ADD COLUMN translator TEXT""",
            ),
        )
