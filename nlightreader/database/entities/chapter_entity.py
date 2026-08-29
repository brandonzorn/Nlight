from sqlalchemy import ForeignKey, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column

from nlightreader.database.entities.base import ModelBase


class ChapterEntity(ModelBase):
    __tablename__ = "chapters"

    vol: Mapped[str | None] = mapped_column(UnicodeText)
    ch: Mapped[str | None] = mapped_column(UnicodeText)
    title: Mapped[str | None] = mapped_column(UnicodeText)

    language: Mapped[str | None] = mapped_column(UnicodeText)

    manga_id: Mapped[str | None] = mapped_column(
        ForeignKey("manga.id", ondelete="CASCADE"),
        nullable=False,
    )
    translator: Mapped[str | None] = mapped_column(UnicodeText)
