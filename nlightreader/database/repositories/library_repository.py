from typing import override

from nlightreader.core.enums import LibList
from nlightreader.database.entities import LibraryEntity
from nlightreader.database.mappers.library_mapper import LibraryMapper
from nlightreader.database.mappers.manga_mapper import MangaMapper
from nlightreader.database.repositories.base_repository import (
    BaseRepository,
)
from nlightreader.models import Manga


class LibraryRepository(BaseRepository[LibraryEntity]):
    entity = LibraryEntity

    def save(self, manga_id: str, library_list: LibList) -> None:
        entity = LibraryMapper.to_entity(
            manga_id,
            library_list,
        )
        self.add(entity)

    def delete(self, manga_id: str) -> None:
        entity = self.get(manga_id)
        if entity is None:
            return
        self.remove(entity)

    def get_by_manga(self, manga_id: str) -> LibList | None:
        entity = self.get(manga_id)
        if entity is None:
            return None
        return LibList(entity.list)

    def get_by_lib_list(self, lib_list: LibList) -> list[Manga]:
        return [
            MangaMapper.to_model(entity.manga)
            for entity in self.find(LibraryEntity.list == lib_list.value)
        ]

    @override
    def exists(self, pk: int | str) -> bool:
        return super().exists(pk)
