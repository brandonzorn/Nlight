from sqlalchemy import delete

from nlightreader.database.entities import HistoryNoteEntity
from nlightreader.database.mappers.history_note_mapper import (
    HistoryNoteMapper,
)
from nlightreader.database.repositories.base_repository import (
    BaseRepository,
)
from nlightreader.items import HistoryNote


class HistoryRepository(BaseRepository[HistoryNoteEntity]):
    entity = HistoryNoteEntity

    def save(self, note: HistoryNote) -> None:
        entity = HistoryNoteMapper.to_entity(note)
        self.merge(entity)

    def save_many(self, notes: list[HistoryNote]) -> None:
        for note in notes:
            self.merge(HistoryNoteMapper.to_entity(note))

    def get_model(self, chapter_id: str) -> HistoryNote | None:
        entity = self.get(chapter_id)
        if entity is None:
            return None
        return HistoryNoteMapper.to_model(entity)

    def get_all_models(self) -> list[HistoryNote]:
        return [HistoryNoteMapper.to_model(entity) for entity in self.all()]

    def delete_by_chapter(self, chapter_id: str) -> None:
        entity = self.get(chapter_id)
        if entity is not None:
            self.remove(entity)

    def delete_by_manga(self, manga_id: str) -> None:
        self._session.scalars(
            delete(HistoryNoteEntity).where(
                HistoryNoteEntity.manga_id == manga_id,
            ),
        )
