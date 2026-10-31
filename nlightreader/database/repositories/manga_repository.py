from sqlalchemy import select

from database.entities import MangaEntity
from database.mappers.manga_mapper import MangaMapper
from database.repositories.base_repository import BaseRepository
from models import Manga


class MangaRepository(BaseRepository[MangaEntity]):
    entity = MangaEntity
    _mapper = MangaMapper

    def save(self, manga: Manga) -> None:
        entity = self._mapper.to_entity(manga)
        self._merge(entity)

    def save_many(self, mangas: list[Manga]) -> None:
        for manga in mangas:
            self.save(manga)

    def get_model(self, manga_id: str) -> Manga | None:
        entity = self._get(manga_id)
        if entity is None:
            return None

        return self._mapper.to_model(entity)

    def get_all_models(self) -> list[Manga]:
        return [self._mapper.to_model(entity) for entity in self._all()]

    def by_catalog(self, catalog_id: int) -> list[Manga]:
        entities = self._session.scalars(
            select(MangaEntity).where(MangaEntity.catalog_id == catalog_id),
        )
        return [self._mapper.to_model(entity) for entity in entities]
