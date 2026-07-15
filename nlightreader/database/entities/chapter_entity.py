from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from nlightreader.database.entities.base import Base


class ChapterEntity(Base):
    __tablename__ = "chapters"

    id: Mapped[str] = mapped_column(Text, primary_key=True)
    content_id: Mapped[str] = mapped_column(Text, nullable=False)
    catalog_id: Mapped[int] = mapped_column(Integer, nullable=False)

    vol: Mapped[str | None] = mapped_column(Text)
    ch: Mapped[str | None] = mapped_column(Text)
    title: Mapped[str | None] = mapped_column(Text)

    language: Mapped[str | None] = mapped_column(Text)

    manga_id: Mapped[str | None] = mapped_column(
        ForeignKey(
            "manga.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    translator: Mapped[str | None] = mapped_column(Text)
