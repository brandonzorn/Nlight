from database.entities import EpisodeEntity
from database.mappers.episode_mapper import EpisodeMapper
from models import Episode

from .base_repository import BaseRepository


class EpisodesRepository(BaseRepository[EpisodeEntity]):
    entity = EpisodeEntity
    _mapper = EpisodeMapper

    def save(self, episode: Episode, anime_id: str) -> None:
        self._merge(self._mapper.to_entity(episode, anime_id))

    def save_many(self, episodes: list[Episode], anime_id: str) -> None:
        for episode in episodes:
            self.save(episode, anime_id)

    def delete(self, episode: Episode) -> None:
        entity = self._get(episode.id)
        if entity is None:
            return
        self._remove(entity)

    def get_model(self, chapter_id: str) -> Episode | None:
        entity = self._get(chapter_id)
        if entity is None:
            return None
        return self._mapper.to_model(entity)

    def get_all_models(self) -> list[Episode]:
        return [self._mapper.to_model(entity) for entity in self._all()]
