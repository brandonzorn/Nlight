from database import db
from items import *


class Desu:
    def __init__(self):
        self.mangas = []
        self.manga_favorites = []
        self.db = db

    def get_content(self, html):
        self.mangas = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return None
            for i in html.json().get('response'):
                self.mangas.append(Manga(i))
                self.db.add_manga(i)

    def get_content_favorites(self):
        self.manga_favorites = []
        for i in self.db.get_manga_library():
            self.manga_favorites.append(i)

    def get_manga(self) -> list:
        return [i.get_name() for i in self.mangas]

    def get_manga_favorites(self) -> list:
        return [i.get_name() for i in self.manga_favorites]
