from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nlightreader.database.entities.base import Base
from nlightreader.database.entities.chapter_entity import ChapterEntity
from nlightreader.database.entities.manga_entity import MangaEntity


class HistoryNoteEntity(Base):
    __tablename__ = "chapter_history"

    manga_id: Mapped[str] = mapped_column(
        ForeignKey(
            "manga.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    chapter_id: Mapped[str] = mapped_column(
        ForeignKey(
            "chapters.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    is_completed: Mapped[bool | None] = mapped_column(Boolean, nullable=True)

    manga: Mapped[MangaEntity] = relationship(MangaEntity)
    chapter: Mapped[ChapterEntity] = relationship(ChapterEntity)
