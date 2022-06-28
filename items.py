class Manga:
    def __init__(self, manga: dict):
        self.id: str = str(manga.get('id'))
        self.catalog_id: int = manga.get('catalog_id')
        self.name: str = manga.get('name')
        self.russian: str = manga.get('russian')
        self.kind: str = manga.get('kind')
        self.description: str = manga.get('description')
        self.score: float = manga.get('score')
        if self.score:
            self.score: float = float(self.score)
        else:
            self.score = float(0)

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name


class Chapter:
    def __init__(self, chapter: dict):
        self.id: str = str(chapter.get('id'))
        self.vol: str = chapter.get('vol')
        self.ch: str = chapter.get('ch')
        self.title: str = chapter.get('title')
        self.language = chapter.get('language')

    def get_name(self) -> str:
        if not self.vol and not self.ch:
            return self.title
        if self.title:
            return f'{self.vol}-{self.ch} {self.title}'
        return f'{self.vol}-{self.ch}'


class Image:
    def __init__(self, page: dict):
        self.id: str = str(page.get('id'))
        self.page: int = page.get('page')
        if self.page:
            self.page = int(self.page)
        self.width: int = page.get('width')
        self.height: int = page.get('height')
        self.img: str = page.get('img')
        self.is_text: bool = page.get('is_text')


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
    def __init__(self):
        self.id = 0
        self.nickname: str = "Войти"
        self.avatar = None
        self.locale = None


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
