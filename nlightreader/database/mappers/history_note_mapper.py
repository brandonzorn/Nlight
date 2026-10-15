from database.entities import HistoryNoteEntity
from database.mappers.chapter_mapper import ChapterMapper
from database.mappers.manga_mapper import MangaMapper
from items import HistoryNote


class HistoryNoteMapper:
    @staticmethod
    def to_entity(model: HistoryNote) -> HistoryNoteEntity:
        return HistoryNoteEntity(**model.to_dict())

    @staticmethod
    def to_model(entity: HistoryNoteEntity) -> HistoryNote:
        return HistoryNote(
            manga=MangaMapper.to_model(entity.manga),
            chapter=ChapterMapper.to_model(entity.chapter),
            is_completed=entity.is_completed,
        )
