class Manga:
    def __init__(self, manga_id, catalog_id, name, russian, kind, description, score):
        self.id = manga_id
        self.catalog_id = catalog_id
        self.name = name
        self.russian = russian
        self.kind = kind
        self.description = description
        self.score = score

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
    def __init__(self, data: dict):
        self.id: str = str(data.get('id'))
        self.name = data.get('name')
        self.russian = data.get('russian')
        self.kind = data.get('kind')

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name


class RequestForm:
    def __init__(self):
        self.limit: int = 50
        self.search: str = ''
        self.page: int = 1
        self.offset = lambda: (self.page - 1) * 50
        self.genres: [Genre] = []
        self.order = ''
        self.kinds = []
        self.mylist = 'planned'

    def clear(self):
        self.limit: int = 50
        self.search: str = ''
        self.page: int = 1
        # self.offset: int = (self.page - 1) * 50
        self.genres: [Genre] = []
        self.order = ''
        self.kinds = []
        self.mylist = 'planned'


class User:
    def __init__(self, user_id, nickname, avatar):
        self.id = user_id
        self.nickname = nickname
        self.avatar = avatar


class Order:
    def __init__(self, data: dict):
        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.russian: str = data.get('russian')

    def get_name(self):
        if self.russian:
            return self.russian
        return self.name


class Kind:
    def __init__(self, data: dict):
        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.russian: str = data.get('russian')

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
