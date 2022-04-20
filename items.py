class Manga:
    def __init__(self, manga: dict):
        self.id: int = manga.get('id')
        self.name: str = manga.get('name')
        self.russian: str = manga.get('russian')
        self.kind: str = manga.get('kind')
        self.description: str = manga.get('description')
        self.score: float = manga.get('score')
        if self.score:
            self.score: float = float(self.score)
        self.shikimori_id = manga.get('shikimori_id')

    def get_name(self) -> str:
        if self.russian:
            return self.russian
        return self.name


class Chapter:
    def __init__(self, chapter: dict):
        self.id: int = chapter.get('id')
        self.vol: int = chapter.get('vol')
        self.ch: int = chapter.get('ch')
        self.title: str = chapter.get('title')

    def get_name(self) -> str:
        if self.title:
            return f'{self.vol}-{self.ch} {self.title}'
        return f'{self.vol}-{self.ch}'


class Image:
    def __init__(self, page: dict):
        self.id: int = page.get('id')
        self.page: int = page.get('page')
        self.width: int = page.get('width')
        self.height: int = page.get('height')
        self.img: str = page.get('img')


class Genre:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.name = data.get('name')
        self.russian = data.get('russian')
        self.kind = data.get('kind')
