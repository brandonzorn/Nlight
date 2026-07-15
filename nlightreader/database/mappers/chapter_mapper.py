from nlightreader.core.enums import Language
from nlightreader.database.entities import ChapterEntity
from nlightreader.models import Chapter


class ChapterMapper:
    @staticmethod
    def to_entity(model: Chapter, manga_id: str | None) -> ChapterEntity:
        return ChapterEntity(
            id=model.id,
            content_id=str(model.content_id),
            catalog_id=model.catalog_id,
            vol=model.volume_number,
            ch=model.chapter_number,
            title=model.title,
            language=model.language.to_str(),
            manga_id=manga_id,
            translator=model.translator,
        )

    @staticmethod
    def to_model(entity: ChapterEntity) -> Chapter:
        return Chapter(
            content_id=str(entity.content_id),
            catalog_id=entity.catalog_id,
            volume_number=entity.vol,
            chapter_number=entity.ch,
            title=entity.title or "",
            language=Language.from_str(entity.language or ""),
            translator=entity.translator,
        )
