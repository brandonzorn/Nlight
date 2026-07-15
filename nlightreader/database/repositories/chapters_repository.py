from nlightreader.database.entities import ChapterEntity
from nlightreader.database.mappers.chapter_mapper import ChapterMapper
from nlightreader.models import Chapter

from .base_repository import BaseRepository


class ChaptersRepository(BaseRepository[ChapterEntity]):
    entity = ChapterEntity

    def save(self, chapter: Chapter, manga_id: str) -> None:
        entity = ChapterMapper.to_entity(chapter, manga_id)
        self.add(entity)

    def save_many(self, chapters: list[Chapter], manga_id: str) -> None:
        for chapter in chapters:
            self.save(chapter, manga_id)

    def delete(self, chapter: Chapter) -> None:
        entity = ChapterMapper.to_entity(chapter, None)
        self.remove(entity)

    def get_model(self, chapter_id: str) -> Chapter | None:
        entity = self.get(chapter_id)
        if entity is None:
            return None
        return ChapterMapper.to_model(entity)

    def get_all_models(self) -> list[Chapter]:
        return [ChapterMapper.to_model(entity) for entity in self.all()]
