class Manga:
    def __init__(self, manga_id, catalog_id, name, russian, kind, description, score):
        self.id = manga_id
        self.catalog_id = catalog_id
        self.name = name
        self.russian = russian
        self.kind = kind
        self.description = description
        self.score = score
        self.volumes = 0
        self.chapters = 0

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name


class Chapter:
    def __init__(self, chapter_id: str, vol: str, ch: str, title: str, language: str):
        self.id = chapter_id
        self.vol = vol
        self.ch = ch
        self.title = title
        self.language = language

    def get_name(self) -> str:
        if not self.vol and not self.ch:
            return self.title
        if self.title:
            return f'{self.vol}-{self.ch} {self.title}'
        return f'{self.vol}-{self.ch}'


class Image:
    def __init__(self, image_id: str, page: int, img: str):
        self.id = image_id
        self.page = page
        self.img = img


class Genre:
    def __init__(self, genre_id, name, russian, kind):
        self.id: str = genre_id
        self.name = name
        self.russian = russian
        self.kind = kind

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name


class RequestForm:
    def __init__(self):
        self.limit: int = 50
        self.search: str = ''
        self.page: int = 1
        self.genres: list[Genre] = []
        self.order: Order = Order('', '', '')
        self.kinds: list[Kind] = []
        self.mylist = 'planned'

    @property
    def offset(self):
        return (self.page - 1) * 50

    def clear(self):
        self.limit = 50
        self.search = ''
        self.page = 1
        self.genres = []
        self.order = Order('', '', '')
        self.kinds = []
        self.mylist = 'planned'


class User:
    def __init__(self, user_id, nickname, avatar):
        self.id = user_id
        self.nickname = nickname
        self.avatar = avatar


class UserRate:
    def __init__(self, rate_id, user_id, target_id, score, status, chapters):
        self.id = rate_id
        self.user_id = user_id
        self.target_id = target_id
        self.score = score
        self.status = status
        self.chapters = chapters


class Order:
    def __init__(self, order_id, name, russian):
        self.id: str = order_id
        self.name: str = name
        self.russian: str = russian

    def get_name(self):
        if self.russian:
            return self.russian
        return self.name


class Kind:
    def __init__(self, kind_id, name, russian):
        self.id: str = kind_id
        self.name: str = name
        self.russian: str = russian

    def get_name(self):
        if self.russian:
            return self.russian
        return self.name


class HistoryNote:
    def __init__(self, note_id, chapter: Chapter, manga: Manga, is_completed: bool):
        self.id = note_id
        self.chapter = chapter
        self.manga = manga
        self.is_completed = is_completed

    def get_name(self):
        return f'{self.manga.get_name()}: {self.chapter.get_name()}'
