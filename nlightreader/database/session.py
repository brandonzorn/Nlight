from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from consts.paths import APP_DATA_PATH
from database.entities.base import Base
from database.migrations import MigrationManager

DB_FILE_PATH = APP_DATA_PATH / "data.db"
engine = create_engine(f"sqlite:///{DB_FILE_PATH}")

Base.metadata.create_all(engine)

Session = sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)

with Session() as session:
    MigrationManager().migrate(session)
