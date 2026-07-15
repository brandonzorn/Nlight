from nlightreader.database.repositories import MangaRepository
from nlightreader.database.session import Session
from nlightreader.models import Manga


class MangaService:
    def save(self, manga: Manga) -> None:
        with Session() as session:
            repo = MangaRepository(session)
            repo.save(manga)
            session.commit()

    def get_by_id(self, manga_id: str) -> Manga | None:
        with Session() as session:
            repo = MangaRepository(session)
            return repo.get_model(manga_id)
