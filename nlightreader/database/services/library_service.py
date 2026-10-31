from core.enums import LibList
from database.repositories import LibraryRepository
from database.session import Session
from items.other_items import LibraryRecord
from models import Manga


class LibraryService:
    @staticmethod
    def save(manga_id: str, lib_list: LibList = LibList.PLANNED) -> None:
        with Session() as session:
            repo = LibraryRepository(session)
            repo.save(manga_id, lib_list)
            session.commit()

    @staticmethod
    def remove(manga_id: str) -> None:
        with Session() as session:
            repo = LibraryRepository(session)
            repo.delete(manga_id)
            session.commit()

    @staticmethod
    def get(manga_id: str) -> LibraryRecord | None:
        with Session() as session:
            repo = LibraryRepository(session)
            return repo.get_by_manga(manga_id)

    @staticmethod
    def get_by_library_list(library_list: LibList) -> list[Manga]:
        with Session() as session:
            repo = LibraryRepository(session)
            return repo.get_by_lib_list(library_list)

    @staticmethod
    def exists(manga_id: str) -> bool:
        with Session() as session:
            repo = LibraryRepository(session)
            return repo.exists(manga_id)
