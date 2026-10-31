from sqlalchemy import ForeignKey, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column

from database.entities.base import TranslatedContentModelBase


class EpisodeEntity(TranslatedContentModelBase):
    __tablename__ = "episodes"

    season_number: Mapped[int] = mapped_column(UnicodeText)
    episode_number: Mapped[int] = mapped_column(UnicodeText)

    url: Mapped[str | None] = mapped_column(UnicodeText)

    anime_id: Mapped[str] = mapped_column(
        ForeignKey("manga.id", ondelete="CASCADE"),
        nullable=False,
    )
