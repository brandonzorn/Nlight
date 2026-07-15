from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from nlightreader.database.entities.base import Base


class SchemaVersionEntity(Base):
    __tablename__ = "schema_version"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True,
        default=0,
    )


__all__ = ["SchemaVersionEntity"]
