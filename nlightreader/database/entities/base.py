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
    )
    content_id: Mapped[str] = mapped_column(
        UnicodeText,
        nullable=False,
    )
    catalog_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )


class TranslatedContentModelBase(ModelBase):
    __abstract__ = True

    title: Mapped[str | None] = mapped_column(UnicodeText)

    language: Mapped[str | None] = mapped_column(UnicodeText)
    translator: Mapped[str | None] = mapped_column(
        UnicodeText,
        nullable=True,
    )
