from .chapters_service import ChaptersService
from .history_service import HistoryService
from .library_service import LibraryService
from .manga_service import MangaService


class Database:
    manga = MangaService()
    chapters = ChaptersService()
    library = LibraryService()
    history = HistoryService()


__all__ = ["Database"]
