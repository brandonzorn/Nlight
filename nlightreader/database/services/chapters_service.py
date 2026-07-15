from nlightreader.database.repositories import ChaptersRepository
from nlightreader.database.session import Session
from nlightreader.models import Chapter


class ChaptersService:
    def save(self, chapter: Chapter, manga_id: str) -> None:
        with Session() as session:
            repo = ChaptersRepository(session)
            repo.save(chapter, manga_id)
            session.commit()

    def save_many(self, chapters: list[Chapter], manga_id: str) -> None:
        with Session() as session:
            repo = ChaptersRepository(session)
            repo.save_many(chapters, manga_id)
            session.commit()

    def delete(self, chapter: Chapter) -> None:
        with Session() as session:
            repo = ChaptersRepository(session)
            repo.delete(chapter)
            session.commit()

    def get_by_id(self, chapter_id: str) -> Chapter | None:
        with Session() as session:
            repo = ChaptersRepository(session)
            return repo.get_model(chapter_id)

    def exists(self, chapter_id: str) -> bool:
        with Session() as session:
            repo = ChaptersRepository(session)
            return repo.exists(chapter_id)
