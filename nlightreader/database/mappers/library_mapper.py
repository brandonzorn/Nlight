from typing import Never

from nlightreader.core.enums import LibList
from nlightreader.database.entities import LibraryEntity


class LibraryMapper:
    @staticmethod
    def to_entity(
        manga_id: str,
        library_list: LibList | None,
    ) -> LibraryEntity:
        return LibraryEntity(manga_id=manga_id, list=library_list)

    @staticmethod
    def to_model() -> Never:
        raise NotImplementedError
