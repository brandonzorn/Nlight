from sqlalchemy import delete

from database.entities import HistoryNoteEntity
from database.mappers.history_note_mapper import HistoryNoteMapper
from database.repositories.base_repository import BaseRepository
from items import HistoryNote


class HistoryRepository(BaseRepository[HistoryNoteEntity]):
    entity = HistoryNoteEntity
    _mapper = HistoryNoteMapper

    def save(self, note: HistoryNote) -> None:
        entity = self._mapper.to_entity(note)
        self._merge(entity)

    def save_many(self, notes: list[HistoryNote]) -> None:
        for note in notes:
            self.save(note)

    def get_model(self, chapter_id: str) -> HistoryNote | None:
        entity = self._get(chapter_id)
        if entity is None:
            return None
        return HistoryNoteMapper.to_model(entity)

    def get_all_models(self) -> list[HistoryNote]:
        return [HistoryNoteMapper.to_model(entity) for entity in self._all()]

    def delete_by_chapter(self, chapter_id: str) -> None:
        entity = self._get(chapter_id)
        if entity is None:
            return
        self._remove(entity)

    def delete_by_manga(self, manga_id: str) -> None:
        self._session.execute(
            delete(HistoryNoteEntity).where(
                HistoryNoteEntity.manga_id == manga_id,
            ),
        )
