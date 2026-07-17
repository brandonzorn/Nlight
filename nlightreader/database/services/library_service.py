from nlightreader.core.enums import LibList
from nlightreader.database.repositories import LibraryRepository
from nlightreader.database.session import Session
from nlightreader.items.other_items import LibraryRecord
from nlightreader.models import Manga


class LibraryService:
    def save(self, manga_id: str, lib_list: LibList = LibList.planned) -> None:
        with Session() as session:
            repo = LibraryRepository(session)
            repo.save(manga_id, lib_list)
            session.commit()

    def remove(self, manga_id: str) -> None:
        with Session() as session:
            repo = LibraryRepository(session)
            repo.delete(manga_id)
            session.commit()

    def get(self, manga_id: str) -> LibraryRecord | None:
        with Session() as session:
            repo = LibraryRepository(session)
            return repo.get_by_manga(manga_id)

    def get_by_library_list(self, library_list: LibList) -> list[Manga]:
        with Session() as session:
            repo = LibraryRepository(session)
            return repo.get_by_lib_list(library_list)

    def exists(self, manga_id: str) -> bool:
        with Session() as session:
            repo = LibraryRepository(session)
            return repo.exists(manga_id)
