from sqlalchemy import Float, Integer, UnicodeText
from sqlalchemy.orm import Mapped, mapped_column

from nlightreader.database.entities.base import ModelBase


class MangaEntity(ModelBase):
    __tablename__ = "manga"

    name: Mapped[str | None] = mapped_column(UnicodeText)
    russian: Mapped[str | None] = mapped_column(UnicodeText)

    kind: Mapped[str | None] = mapped_column(UnicodeText)
    description: Mapped[str | None] = mapped_column(UnicodeText)

    score: Mapped[float | int] = mapped_column(Float, default=0)
    status: Mapped[str | None] = mapped_column(UnicodeText)

    volumes: Mapped[int] = mapped_column(Integer, default=0)
    chapters: Mapped[int] = mapped_column(Integer, default=0)

    preview_url: Mapped[str | None] = mapped_column(UnicodeText)
