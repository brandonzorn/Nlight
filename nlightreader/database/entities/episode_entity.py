from sqlalchemy import ForeignKey, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column

from nlightreader.database.entities.base import ModelBase


class EpisodeEntity(ModelBase):
    __tablename__ = "episodes"

    season_number: Mapped[int] = mapped_column(UnicodeText)
    episode_number: Mapped[int] = mapped_column(UnicodeText)
    title: Mapped[str | None] = mapped_column(UnicodeText)

    url: Mapped[str | None] = mapped_column(UnicodeText)

    language: Mapped[str | None] = mapped_column(UnicodeText)

    anime_id: Mapped[str | None] = mapped_column(
        ForeignKey("manga.id", ondelete="CASCADE"),
        nullable=False,
    )
    translator: Mapped[str | None] = mapped_column(UnicodeText, nullable=True)
