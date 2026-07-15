from nlightreader.core.enums import MangaKind, MangaStatus
from nlightreader.database.entities import MangaEntity
from nlightreader.models import Manga


class MangaMapper:
    @staticmethod
    def to_entity(model: Manga) -> MangaEntity:
        return MangaEntity(
            id=model.id,
            content_id=model.content_id,
            catalog_id=model.catalog_id,
            name=model.name,
            russian=model.russian,
            kind=model.kind.to_str(),
            description=model.get_description(),
            score=model.score,
            status=model.status.to_str(),
            volumes=model.volumes_number,
            chapters=model.chapters_number,
            preview_url=model.preview_url,
        )

    @staticmethod
    def to_model(entity: MangaEntity) -> Manga:
        manga = Manga(
            content_id=str(entity.content_id),
            catalog_id=entity.catalog_id,
            name=str(entity.name or ""),
            russian=str(entity.russian or ""),
        )

        manga.kind = MangaKind.from_str(entity.kind)
        manga.status = MangaStatus.from_str(entity.status)

        manga.score = entity.score
        manga.volumes = entity.volumes
        manga.chapters = entity.chapters
        manga.preview_url = entity.preview_url

        manga.set_description_from_str(entity.description or "")

        return manga
