from nlightreader.database.repositories import EpisodesRepository
from nlightreader.database.session import Session
from nlightreader.models import Episode


class EpisodesService:
    def save(self, episode: Episode, manga_id: str) -> None:
        with Session() as session:
            repo = EpisodesRepository(session)
            repo.save(episode, manga_id)
            session.commit()

    def save_many(self, episodes: list[Episode], manga_id: str) -> None:
        with Session() as session:
            repo = EpisodesRepository(session)
            repo.save_many(episodes, manga_id)
            session.commit()

    def delete(self, episode: Episode) -> None:
        with Session() as session:
            repo = EpisodesRepository(session)
            repo.delete(episode)
            session.commit()

    def get_by_id(self, episode_id: str) -> Episode | None:
        with Session() as session:
            repo = EpisodesRepository(session)
            return repo.get_model(episode_id)

    def exists(self, episode_id: str) -> bool:
        with Session() as session:
            repo = EpisodesRepository(session)
            return repo.exists(episode_id)
