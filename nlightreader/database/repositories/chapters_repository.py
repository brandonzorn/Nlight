from database.entities import ChapterEntity
from database.mappers.chapter_mapper import ChapterMapper
from models import Chapter

from .base_repository import BaseRepository


class ChaptersRepository(BaseRepository[ChapterEntity]):
    entity = ChapterEntity
    _mapper = ChapterMapper

    def save(self, chapter: Chapter, manga_id: str) -> None:
        self._merge(self._mapper.to_entity(chapter, manga_id))

    def save_many(self, chapters: list[Chapter], manga_id: str) -> None:
        for chapter in chapters:
            self.save(chapter, manga_id)

    def delete(self, chapter: Chapter) -> None:
        entity = self._get(chapter.id)
        if entity is None:
            return
        self._remove(entity)

    def get_model(self, chapter_id: str) -> Chapter | None:
        entity = self._get(chapter_id)
        if entity is None:
            return None
        return self._mapper.to_model(entity)

    def get_all_models(self) -> list[Chapter]:
        return [self._mapper.to_model(entity) for entity in self._all()]
