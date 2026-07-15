from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nlightreader.database.entities.base import Base
from nlightreader.database.entities.manga_entity import MangaEntity


class LibraryEntity(Base):
    __tablename__ = "library"

    manga_id: Mapped[str] = mapped_column(
        ForeignKey(
            "manga.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
    list: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    manga: Mapped[MangaEntity] = relationship(MangaEntity)
