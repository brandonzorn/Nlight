from database import db
from static import *
from items import *
import os


class Desu:
    def __init__(self):
        self.mangas = []
        self.manga_favorites = []
        self.chapters = []
        self.manga: Manga = Manga({})
        self.chapter: Chapter = Chapter({})
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

    def get_chapters(self, html):
        self.chapters = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return
            chapters = html.json().get('response').get('chapters').get('list')
            if chapters:
                for i in chapters:
                    self.db.add_chapters(i, self.manga.id, chapters[::-1].index(i))
        self.chapters = self.db.get_chapters(self.manga.id)
        self.chapters.reverse()

    def download_all(self, main_window):
        wd = os.getcwd()
        chapters = self.chapters
        manga_id = self.manga.id
        for i in chapters:
            chapter_id = i.id
            current_url = f'https://desu.me/manga/api/{manga_id}/chapter/{chapter_id}'
            html = get_html(current_url)
            images = html.json().get('response').get('pages').get('list')
            if images:
                for x in images:
                    self.db.add_images(x, chapter_id, images.index(x))
            for j in images:
                if main_window.isHidden():
                    return
                page = j.get('page')
                if not os.path.exists(f'{wd}/Desu/images/{manga_id}/{chapter_id}/{page}.jpg'):
                    os.makedirs(f'{wd}/Desu/images/{manga_id}/{chapter_id}', exist_ok=True)
                    img = get_html(images[page - 1].get('img'))
                    with open(f'{wd}/Desu/images/{manga_id}/{chapter_id}/{page}.jpg', 'wb') as f:
                        f.write(img.content)

    def get_manga(self) -> list:
        return [i.get_name() for i in self.mangas]

    def get_manga_favorites(self) -> list:
        return [i.get_name() for i in self.manga_favorites]

    def get_preview(self) -> str:
        wd = os.getcwd()
        if not os.path.exists(f'{wd}/Desu/images/{self.manga.id}/preview.jpg'):
            os.makedirs(f'{wd}/Desu/images/{self.manga.id}', exist_ok=True)
            img = get_html(f'https://desu.me/data/manga/covers/preview/{self.manga.id}.jpg')
            with open(f'{wd}/Desu/images/{self.manga.id}/preview.jpg', 'wb') as f:
                f.write(img.content)
        return f'{wd}/Desu/images/{self.manga.id}/preview.jpg'
