from typing import override

from core.enums import Language
from models.base_model import TranslatedContentModel


class Chapter(TranslatedContentModel):
    def __init__(
        self,
        *,
        content_id: str,
        catalog_id: int,
        volume_number: str | None,
        chapter_number: str | None,
        title: str | None,
        language: Language = Language.UNDEFINED,
        translator: str | None = None,
    ) -> None:
        super().__init__(content_id, catalog_id, title, language, translator)
        self._volume_number = volume_number
        self._chapter_number = chapter_number

    @property
    def volume_number(self) -> str | None:
        return self._volume_number

    @property
    def chapter_number(self) -> str | None:
        return self._chapter_number

    def get_name(self) -> str:
        parts = []
        for p in [self._volume_number, self._chapter_number]:
            if p is None or p.strip() == "":
                continue
            parts.append(p)
        vol_ch_name = "-".join(parts)
        if vol_ch_name and self._title:
            return f"{vol_ch_name} {self._title}"
        return vol_ch_name or (self._title or "")

    @override
    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "vol": self._volume_number,
                "ch": self._chapter_number,
            },
        )
        return data


__all__ = ["Chapter"]
