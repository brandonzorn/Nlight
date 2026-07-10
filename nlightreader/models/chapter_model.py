from typing import override

from nlightreader.core.enums import Language
from nlightreader.models.base_model import ContentModel


class Chapter(ContentModel):
    title: str | None
    volume_number: str | None = None
    chapter_number: str | None = None
    language: Language = Language.UNDEFINED
    translator: str | None = None

    def get_name(self) -> str:
        if not self.volume_number and not self.chapter_number:
            if not self.title:
                return f"No data {self.content_id}"
            return self.title

        vol_ch_name = f"{self.volume_number}-{self.chapter_number}"
        if self.title:
            return f"{vol_ch_name} {self.title}"
        return vol_ch_name

    @override
    def to_dict(self) -> dict:
        return self.model_dump()


__all__ = ["Chapter"]
