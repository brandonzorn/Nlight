from sqlalchemy import ForeignKey, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column

from database.entities.base import TranslatedContentModelBase


class ChapterEntity(TranslatedContentModelBase):
    __tablename__ = "chapters"

    vol: Mapped[str | None] = mapped_column(UnicodeText)
    ch: Mapped[str | None] = mapped_column(UnicodeText)

    manga_id: Mapped[str | None] = mapped_column(
        ForeignKey("manga.id", ondelete="CASCADE"),
        nullable=False,
    )
