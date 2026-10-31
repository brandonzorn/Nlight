from database.repositories import ChaptersRepository
from database.session import Session
from models import Chapter


class ChaptersService:
    @staticmethod
    def save(chapter: Chapter, manga_id: str) -> None:
        with Session() as session:
            repo = ChaptersRepository(session)
            repo.save(chapter, manga_id)
            session.commit()

    @staticmethod
    def save_many(chapters: list[Chapter], manga_id: str) -> None:
        with Session() as session:
            repo = ChaptersRepository(session)
            repo.save_many(chapters, manga_id)
            session.commit()

    @staticmethod
    def delete(chapter: Chapter) -> None:
        with Session() as session:
            repo = ChaptersRepository(session)
            repo.delete(chapter)
            session.commit()

    @staticmethod
    def get_by_id(chapter_id: str) -> Chapter | None:
        with Session() as session:
            repo = ChaptersRepository(session)
            return repo.get_model(chapter_id)

    @staticmethod
    def exists(chapter_id: str) -> bool:
        with Session() as session:
            repo = ChaptersRepository(session)
            return repo.exists(chapter_id)
