from typing import override

from core.enums import Language
from models.base_model import TranslatedContentModel


class Episode(TranslatedContentModel):
    def __init__(
        self,
        *,
        content_id: str,
        catalog_id: int,
        season_number: int,
        episode_number: int,
        title: str | None,
        url: str | None,
        language: Language = Language.UNDEFINED,
        translator: str | None = None,
    ) -> None:
        super().__init__(content_id, catalog_id, title, language, translator)
        self._season_number = season_number
        self._episode_number = episode_number

        self._url = url

    @property
    def url(self) -> str | None:
        return self._url

    @property
    def season_number(self) -> int:
        return self._season_number

    @property
    def episode_number(self) -> int:
        return self._episode_number

    def get_name(self) -> str:
        parts = []
        for p in [self._season_number, self._episode_number]:
            if p is None or p == 0:
                continue
            parts.append(str(p))
        num_name = "-".join(parts)

        if num_name and self._title:
            return f"{num_name} {self._title}"
        return num_name or (self._title or "")

    @override
    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "season_number": self._season_number,
                "episode_number": self._episode_number,
            },
        )
        return data


__all__ = ["Episode"]
