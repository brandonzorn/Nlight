from sqlalchemy import select

from nlightreader.database.entities import MangaEntity
from nlightreader.database.mappers.manga_mapper import MangaMapper
from nlightreader.database.repositories.base_repository import (
    BaseRepository,
)
from nlightreader.models import Manga


class MangaRepository(BaseRepository[MangaEntity]):
    entity = MangaEntity

    def save(self, manga: Manga) -> None:
        entity = MangaMapper.to_entity(manga)
        self.add(entity)

    def get_model(self, manga_id: str) -> Manga | None:
        entity = self.get(manga_id)

        if entity is None:
            return None

        return MangaMapper.to_model(entity)

    def save_many(self, mangas: list[Manga]) -> None:
        for manga in mangas:
            self.save(manga)

    def get_all_models(self) -> list[Manga]:
        return [MangaMapper.to_model(entity) for entity in self.all()]

    def by_catalog(self, catalog_id: int) -> list[Manga]:
        entities = self._session.scalars(
            select(MangaEntity).where(MangaEntity.catalog_id == catalog_id),
        )

        return [MangaMapper.to_model(entity) for entity in entities]
