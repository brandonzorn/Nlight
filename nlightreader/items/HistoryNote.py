from nlightreader.items import Chapter, Manga


class HistoryNote:
    def __init__(self, note_id, chapter: Chapter, manga: Manga, is_completed: bool):
        self.id = note_id
        self.chapter = chapter
        self.manga = manga
        self.is_completed = is_completed

    def get_name(self):
        return f'{self.manga.get_name()}: {self.chapter.get_name()}'
