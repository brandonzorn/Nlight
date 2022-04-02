import sqlite3
import os

from const import lib_lists_en
from items import Chapter, Image, Manga


class Database:
    def __init__(self):
        self.wd = os.getcwd()
        if not os.path.exists(f'{self.wd}/Desu/data.db'):
            os.makedirs(f'{self.wd}/Desu', exist_ok=True)
        self.con = sqlite3.connect(f'{self.wd}/Desu/data.db')
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS manga (id INTEGER PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        name STRING, russian STRING, kind STRING, description TEXT, score FLOAT);""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS chapters (id INTEGER PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        vol STRING, ch STRING, title STRING, manga_id INTEGER, index_n INTEGER);""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        page INTEGER, width INTEGER, height INTEGER, img STRING, chapter_id INTEGER, index_n INTEGER);""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        list STRING)""")
        self.con.commit()

    def add_manga(self, data: dict):
        self.cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?, ?);",
                         (data.get('id'), data.get('name'), data.get('russian'),
                          data.get('kind'), data.get('description'), data.get('score')))
        self.con.commit()

    def add_chapters(self, data: dict, manga_id: int, index: int):
        self.cur.execute("INSERT INTO chapters VALUES(?, ?, ?, ?, ?, ?);",
                         (data.get('id'), data.get('vol'), data.get('ch'), data.get('title'), manga_id, index))
        self.con.commit()

    def get_chapters(self, manga_id: int) -> list:
        a = self.cur.execute(f"SELECT * FROM chapters WHERE manga_id = {manga_id} ORDER by index_n").fetchall()
        return [Chapter({'id': i[0], 'vol': i[1], 'ch': i[2], 'title': i[3]}) for i in a[::-1]]

    def add_images(self, data: dict, chapter_id: int, index: int):
        self.cur.execute("INSERT INTO images VALUES(?, ?, ?, ?, ?, ?, ?);",
                         (data.get('id'), data.get('page'), data.get('width'),
                          data.get('height'), data.get('img'), chapter_id, index))
        self.con.commit()

    def get_images(self, chapter_id: int) -> list:
        a = self.cur.execute(f"SELECT * FROM images WHERE chapter_id = {chapter_id} ORDER by index_n").fetchall()
        return [Image({'id': i[0], 'page': i[1], 'width': i[2], 'height': i[3], 'img': i[4]}) for i in a]

    def add_manga_library(self, manga_id: int, lib_list: str = "planned"):
        self.cur.execute(f"INSERT INTO library VALUES(?, ?);", (manga_id, lib_list))
        self.con.commit()

    def get_manga_library(self, lib_list) -> [Manga]:
        a = self.cur.execute(f"SELECT id FROM library WHERE list = '{lib_list}';").fetchall()
        manga = []
        for i in a[::-1]:
            x = self.cur.execute(f"SELECT * FROM manga WHERE id = {i[0]}").fetchall()[0]
            manga.append(Manga({'id': x[0], 'name': x[1], 'russian': x[2], 'kind': x[3],
                                'description': x[4], 'score': x[5]}))
        return manga

    def check_manga_library(self, manga_id: int) -> bool:
        a = self.cur.execute(f"SELECT list FROM library WHERE id = {manga_id};").fetchall()
        self.con.commit()
        if a and a[0][0] in lib_lists_en:
            return True
        return False

    def rem_manga_library(self, manga_id: int):
        self.cur.execute(f"DELETE FROM library WHERE id = {manga_id};")
        self.con.commit()


db = Database()
