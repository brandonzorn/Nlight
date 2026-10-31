from database.repositories import EpisodesRepository
from database.session import Session
from models import Episode


class EpisodesService:
    @staticmethod
    def save(episode: Episode, manga_id: str) -> None:
        with Session() as session:
            repo = EpisodesRepository(session)
            repo.save(episode, manga_id)
            session.commit()

    @staticmethod
    def save_many(episodes: list[Episode], manga_id: str) -> None:
        with Session() as session:
            repo = EpisodesRepository(session)
            repo.save_many(episodes, manga_id)
            session.commit()

    @staticmethod
    def delete(episode: Episode) -> None:
        with Session() as session:
            repo = EpisodesRepository(session)
            repo.delete(episode)
            session.commit()

    @staticmethod
    def get_by_id(episode_id: str) -> Episode | None:
        with Session() as session:
            repo = EpisodesRepository(session)
            return repo.get_model(episode_id)

    @staticmethod
    def exists(episode_id: str) -> bool:
        with Session() as session:
            repo = EpisodesRepository(session)
            return repo.exists(episode_id)
