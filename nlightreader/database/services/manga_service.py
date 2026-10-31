from database.repositories import MangaRepository
from database.session import Session
from models import Manga


class MangaService:
    @staticmethod
    def save(manga: Manga) -> None:
        with Session() as session:
            repo = MangaRepository(session)
            repo.save(manga)
            session.commit()

    @staticmethod
    def get_by_id(manga_id: str) -> Manga | None:
        with Session() as session:
            repo = MangaRepository(session)
            return repo.get_model(manga_id)
