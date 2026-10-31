from core.enums import LibList
from database.entities import LibraryEntity
from database.mappers.library_mapper import LibraryMapper
from database.mappers.manga_mapper import MangaMapper
from database.repositories.base_repository import BaseRepository
from items.other_items import LibraryRecord
from models import Manga


class LibraryRepository(BaseRepository[LibraryEntity]):
    entity = LibraryEntity
    _mapper = LibraryMapper

    def save(self, manga_id: str, library_list: LibList) -> None:
        entity = self._mapper.to_entity(manga_id, library_list)
        self._merge(entity)

    def delete(self, manga_id: str) -> None:
        entity = self._get(manga_id)
        if entity is None:
            return
        self._remove(entity)

    def get_by_manga(self, manga_id: str) -> LibraryRecord | None:
        entity = self._get(manga_id)
        if entity is None:
            return None
        return LibraryMapper.to_model(entity)

    def get_by_lib_list(self, lib_list: LibList) -> list[Manga]:
        return [
            MangaMapper.to_model(entity.manga)
            for entity in self._find(LibraryEntity.list == lib_list.value)
        ]
