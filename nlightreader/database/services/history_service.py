from nlightreader.database.repositories import HistoryRepository
from nlightreader.database.session import Session
from nlightreader.items import HistoryNote


class HistoryService:
    def save(self, note: HistoryNote) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.save(note)
            session.commit()

    def save_many(self, notes: list[HistoryNote]) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.save_many(notes)
            session.commit()

    def delete_by_chapter(self, chapter_id: str) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.delete_by_chapter(chapter_id)
            session.commit()

    def delete_by_manga(self, manga_id: str) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.delete_by_manga(manga_id)
            session.commit()

    def exists(self, chapter_id: str) -> bool:
        with Session() as session:
            repo = HistoryRepository(session)
            return repo.exists(chapter_id)

    def is_completed(self, chapter_id: str) -> bool:
        with Session() as session:
            repo = HistoryRepository(session)
            model = repo.get_model(chapter_id)
            if not model:
                return False
            return model.is_completed

    def get_by_id(self, chapter_id: str) -> HistoryNote | None:
        with Session() as session:
            repo = HistoryRepository(session)
            return repo.get_model(chapter_id)

    def get_all(self) -> list[HistoryNote]:
        with Session() as session:
            repo = HistoryRepository(session)
            return repo.get_all_models()
