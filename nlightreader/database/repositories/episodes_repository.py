from nlightreader.database.entities import EpisodeEntity
from nlightreader.database.mappers.episode_mapper import EpisodeMapper
from nlightreader.models import Episode

from .base_repository import BaseRepository


class EpisodesRepository(BaseRepository[EpisodeEntity]):
    entity = EpisodeEntity

    @staticmethod
    def _to_entity(episode: Episode, anime_id: str | None) -> EpisodeEntity:
        return EpisodeMapper.to_entity(episode, anime_id)

    def save(self, episode: Episode, anime_id: str) -> None:
        self.add(self._to_entity(episode, anime_id))

    def save_many(self, episodes: list[Episode], anime_id: str) -> None:
        entities = [self._to_entity(episode, anime_id) for episode in episodes]
        self.add_all(entities)

    def delete(self, episode: Episode) -> None:
        self.remove(self._to_entity(episode, None))

    def get_model(self, episode_id: str) -> Episode | None:
        entity = self.get(episode_id)
        if entity is None:
            return None
        return EpisodeMapper.to_model(entity)

    def get_all_models(self) -> list[Episode]:
        return [EpisodeMapper.to_model(entity) for entity in self.all()]
