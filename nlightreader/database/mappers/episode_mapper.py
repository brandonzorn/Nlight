from nlightreader.core.enums import Language
from nlightreader.database.entities import EpisodeEntity
from nlightreader.models import Episode


class EpisodeMapper:
    @staticmethod
    def to_entity(model: Episode, anime_id: str | None) -> EpisodeEntity:
        return EpisodeEntity(
            id=model.id,
            content_id=str(model.content_id),
            catalog_id=model.catalog_id,
            season_number=model.season_number,
            episode_number=model.episode_number,
            title=model.title,
            url=model.url,
            language=model.language.to_str(),
            anime_id=anime_id,
            translator=model.translator,
        )

    @staticmethod
    def to_model(entity: EpisodeEntity) -> Episode:
        return Episode(
            content_id=str(entity.content_id),
            catalog_id=entity.catalog_id,
            season_number=entity.season_number,
            episode_number=entity.episode_number,
            title=entity.title or "",
            url=entity.url,
            language=Language.from_str(entity.language or ""),
            translator=entity.translator,
        )
