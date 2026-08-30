from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.database.entities.base import Base
from nlightreader.database.migrations import MigrationManager

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
