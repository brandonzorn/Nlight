from static import *


class Desu:
    def __init__(self):
        self.manga = []
        self.manga_mylist = []
        self.chapters = []
        self.images = []
        self.manga_id = 0
        self.chapter_id = 0
        self.start()

    @staticmethod
    def start():
        wd = os.getcwd()
        if not os.path.exists(f'{wd}/Desu/data.db'):
            os.makedirs(f'{wd}/Desu', exist_ok=True)
            con = sqlite3.connect(f'{wd}/Desu/data.db')
            cur = con.cursor()
            cur.execute("""CREATE TABLE manga (id INTEGER PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
             name STRING, russian STRING, kind STRING, description TEXT, favorites STRING, score FLOAT);""")
            cur.execute("""CREATE TABLE chapters (id INTEGER PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
            vol STRING, ch STRING, title STRING, manga_id INTEGER, index_n INTEGER);""")
            cur.execute("""CREATE TABLE images (id INTEGER PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
            page INTEGER, width INTEGER, height INTEGER, img STRING, chapter_id INTEGER, index_n INTEGER);""")
            con.commit()
            con.close()

    def get_content(self, html):
        self.manga = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return None
            for i in html.json().get('response'):
                self.manga.append(i)
                manga_add(i)

    def get_content_favorites(self):
        self.manga_mylist = []
        for i in manga_favorites_get():
            self.manga_mylist.append(i)

    def get_chapters(self, html):
        self.chapters = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return
            chapters = html.json().get('response').get('chapters').get('list')
            if chapters:
                for i in chapters:
                    chapters_add(i, self.manga_id, chapters[::-1].index(i))
        self.chapters = chapters_get(self.manga_id)

    def get_images(self, html):
        self.images = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return
            images = html.json().get('response').get('pages').get('list')
            for i in images:
                images_add(i, self.chapter_id, images.index(i))
        self.images = images_get(self.chapter_id)

    def download(self, form):
        wd = os.getcwd()
        images = self.images
        manga_id = self.manga_id
        chapter_id = self.chapter_id
        for i in images:
            if form.isHidden() or chapter_id != self.chapter_id:
                return
            page = i.get('page')
            if not os.path.exists(f'{wd}/Desu/images/{manga_id}/{chapter_id}/{page}.jpg'):
                img = get_html(images[page - 1].get('img'))
                with open(f'{wd}/Desu/images/{manga_id}/{chapter_id}/{page}.jpg', 'wb') as f:
                    f.write(img.content)

    def download_all(self, main_window):
        wd = os.getcwd()
        chapters = self.chapters
        manga_id = self.manga_id
        for i in chapters[::-1]:
            chapter_id = i.get('id')
            current_url = f'https://desu.me/manga/api/{manga_id}/chapter/{chapter_id}'
            html = get_html(current_url)
            images = html.json().get('response').get('pages').get('list')
            if images:
                for x in images:
                    images_add(x, chapter_id, images.index(x))
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
        a = []
        for i in self.manga:
            if i.get('russian') == '':
                a.append(i.get('name'))
            else:
                a.append(i.get('russian'))
        return a

    def get_manga_favorites(self) -> list:
        a = []
        for i in self.manga_mylist:
            if i.get('russian') == '':
                a.append(i.get('name'))
            else:
                a.append(i.get('russian'))
        return a

    def get_images_pages(self) -> int:
        if not self.images:
            return 1
        return self.images[-1].get('page')

    def get_chapter(self, index: int) -> list:
        return [self.chapters[index].get("vol"), self.chapters[index].get("ch"), self.chapters[index].get("title")]

    def get_preview(self) -> str:
        wd = os.getcwd()
        if not os.path.exists(f'{wd}/Desu/images/{self.manga_id}/preview.jpg'):
            os.makedirs(f'{wd}/Desu/images/{self.manga_id}', exist_ok=True)
            img = get_html(f'https://desu.me/data/manga/covers/preview/{self.manga_id}.jpg')
            with open(f'{wd}/Desu/images/{self.manga_id}/preview.jpg', 'wb') as f:
                f.write(img.content)
        return f'{wd}/Desu/images/{self.manga_id}/preview.jpg'

    def get_image(self, page: int) -> str:
        wd = os.getcwd()
        if not os.path.exists(f'{wd}/Desu/images/{self.manga_id}/{self.chapter_id}/{page}.jpg'):
            os.makedirs(f'{wd}/Desu/images/{self.manga_id}/{self.chapter_id}', exist_ok=True)
            img = get_html(self.images[page - 1].get('img'))
            with open(f'{wd}/Desu/images/{self.manga_id}/{self.chapter_id}/{page}.jpg', 'wb') as f:
                f.write(img.content)
        return f'{wd}/Desu/images/{self.manga_id}/{self.chapter_id}/{page}.jpg'
