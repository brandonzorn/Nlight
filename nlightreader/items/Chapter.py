class Chapter:
    def __init__(self, content_id: str, catalog_id: int, vol: str, ch: str, title: str, language: str):
        self.id = f'|{catalog_id}|_|{content_id}|'
        self.content_id = content_id
        self.catalog_id = catalog_id
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
