from core.enums import LibList
from database.entities import LibraryEntity
from items.other_items import LibraryRecord


class LibraryMapper:
    @staticmethod
    def to_entity(
        manga_id: str,
        library_list: LibList | None,
    ) -> LibraryEntity:
        return LibraryEntity(manga_id=manga_id, list=library_list)

    @staticmethod
    def to_model(entity: LibraryEntity) -> LibraryRecord:
        return LibraryRecord(
            manga_id=entity.manga_id,
            library_list=LibList(entity.list),
        )
