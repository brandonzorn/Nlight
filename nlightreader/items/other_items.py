from nlightreader.consts.enums import Nl
from nlightreader.models import Chapter, Manga


class HistoryNote:
    def __init__(self, chapter: Chapter, manga: Manga, is_completed: bool):
        self.chapter = chapter
        self.manga = manga
        self.is_completed = is_completed

    def get_name(self):
        return f"{self.manga.get_name()}: {self.chapter.get_name()}"

    def to_dict(self) -> dict:
        return {
            "manga_id": self.manga.id,
            "chapter_id": self.chapter.id,
            "is_completed": self.is_completed,
        }


class UserRate:
    def __init__(
        self,
        rate_id,
        user_id,
        target_id,
        score: int,
        status: Nl.LibList,
        chapters,
    ):
        self.id = rate_id
        self.user_id = user_id
        self.target_id = target_id
        self.score = score
        self.status = status
        self.chapters = chapters


class User:
    def __init__(self, user_id, nickname, avatar):
        self.id = user_id
        self.nickname = nickname
        self.avatar = avatar


__all__ = [
    "HistoryNote",
    "UserRate",
    "User",
]
