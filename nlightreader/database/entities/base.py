from datetime import datetime

from sqlalchemy import DateTime, Integer, UnicodeText
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now,
        onupdate=datetime.now,
    )


class ModelBase(Base):
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        UnicodeText,
        primary_key=True,
        sqlite_on_conflict_primary_key="REPLACE",
    )
    content_id: Mapped[str] = mapped_column(
        UnicodeText,
        nullable=False,
    )
    catalog_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
