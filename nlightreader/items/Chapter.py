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
