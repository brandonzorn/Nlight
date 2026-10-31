from database.repositories import HistoryRepository
from database.session import Session
from items import HistoryNote


class HistoryService:
    @staticmethod
    def save(note: HistoryNote) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.save(note)
            session.commit()

    @staticmethod
    def save_many(notes: list[HistoryNote]) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.save_many(notes)
            session.commit()

    @staticmethod
    def delete_by_chapter(chapter_id: str) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.delete_by_chapter(chapter_id)
            session.commit()

    @staticmethod
    def delete_by_manga(manga_id: str) -> None:
        with Session() as session:
            repo = HistoryRepository(session)
            repo.delete_by_manga(manga_id)
            session.commit()

    @staticmethod
    def exists(chapter_id: str) -> bool:
        with Session() as session:
            repo = HistoryRepository(session)
            return repo.exists(chapter_id)

    @staticmethod
    def is_completed(chapter_id: str) -> bool:
        with Session() as session:
            repo = HistoryRepository(session)
            model = repo.get_model(chapter_id)
            if not model:
                return False
            return model.is_completed

    @staticmethod
    def get_by_id(chapter_id: str) -> HistoryNote | None:
        with Session() as session:
            repo = HistoryRepository(session)
            return repo.get_model(chapter_id)

    @staticmethod
    def get_all() -> list[HistoryNote]:
        with Session() as session:
            repo = HistoryRepository(session)
            return repo.get_all_models()
