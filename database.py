import os
import sqlite3
from threading import Lock

from const import lib_lists_en
from items import Chapter, Image, Manga, HistoryNote
from utils import singleton, with_lock_thread


@singleton
class Database:

    lock = Lock()

    def __init__(self):
        self.__wd = os.getcwd()
        if not os.path.exists(f'{self.__wd}/Desu/data.db'):
            os.makedirs(f'{self.__wd}/Desu', exist_ok=True)
        self.__con = sqlite3.connect(f'{self.__wd}/Desu/data.db', check_same_thread=False)
        self.__cur = self.__con.cursor()
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS manga (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        catalog_id INTEGER, name STRING, russian STRING, kind STRING, description TEXT, score FLOAT);""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS chapters (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        vol STRING, ch STRING, title STRING, language STRING, manga_id INTEGER, index_n INTEGER);""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS images (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        page INTEGER, img STRING, chapter_id INTEGER);""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS library (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        list STRING)""")
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS chapter_history
        (chapter_id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL, manga_id STRING NOT NULL, is_completed BOOLEAN)""")
        self.__con.commit()

    @with_lock_thread(lock)
    def add_mangas(self, mangas: list[Manga]):
        for manga in mangas:
            self.__cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?, ?, ?);",
                               (manga.id, manga.catalog_id, manga.name, manga.russian, manga.kind, manga.description,
                                manga.score))
        self.__con.commit()

    def get_manga(self, manga_id):
        x = self.__cur.execute(f"SELECT * FROM manga WHERE id = '{manga_id}'").fetchone()
        return Manga(x[0], x[1], x[2], x[3], x[4], x[5], x[6])

    @with_lock_thread(lock)
    def add_chapters(self, chapters: list[Chapter], manga: Manga):
        for chapter in chapters:
            index = chapters[::-1].index(chapter)
            self.__cur.execute("INSERT INTO chapters VALUES(?, ?, ?, ?, ?, ?, ?);",
                               (chapter.id, chapter.vol, chapter.ch, chapter.title, chapter.language, manga.id, index))
        self.__con.commit()

    def get_chapter(self, chapter_id):
        a = self.__cur.execute(f"SELECT * FROM chapters WHERE id = '{chapter_id}'").fetchone()
        return Chapter(a[0], a[1], a[2], a[3], a[4])

    @with_lock_thread(lock)
    def get_chapters(self, manga: Manga) -> list[Chapter]:
        a = self.__cur.execute(f"SELECT * FROM chapters WHERE manga_id = '{manga.id}' ORDER by index_n").fetchall()
        return [Chapter(i[0], i[1], i[2], i[3], i[4]) for i in a[::-1]]

    @with_lock_thread(lock)
    def add_images(self, images: list[Image], chapter: Chapter):
        for image in images:
            self.__cur.execute("INSERT INTO images VALUES(?, ?, ?, ?);",
                               (image.id, image.page, image.img, chapter.id))
        self.__con.commit()

    @with_lock_thread(lock)
    def get_images(self, chapter: Chapter) -> list[Image]:
        a = self.__cur.execute(f"SELECT * FROM images WHERE chapter_id = '{chapter.id}' ORDER by page").fetchall()
        return [Image(i[0], i[1], i[2]) for i in a]

    @with_lock_thread(lock)
    def add_manga_library(self, manga: Manga, lib_list: str = "planned"):
        self.__cur.execute(f"INSERT INTO library VALUES(?, ?);", (manga.id, lib_list))
        self.__con.commit()

    @with_lock_thread(lock)
    def get_manga_library(self, lib_list) -> list[Manga]:
        a = self.__cur.execute(f"SELECT id FROM library WHERE list = '{lib_list}';").fetchall()
        manga = []
        for i in a[::-1]:
            x = self.__cur.execute(f"SELECT * FROM manga WHERE id = '{i[0]}'").fetchall()[0]
            manga.append(Manga(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
        return manga

    @with_lock_thread(lock)
    def check_manga_library(self, manga: Manga):
        a = self.__cur.execute(f"SELECT list FROM library WHERE id = '{manga.id}';").fetchall()
        if a and a[0][0] in lib_lists_en:
            return a[0][0]

    @with_lock_thread(lock)
    def rem_manga_library(self, manga: Manga):
        self.__cur.execute(f"DELETE FROM library WHERE id = '{manga.id}';")
        self.__con.commit()

    @with_lock_thread(lock)
    def check_complete_chapter(self, chapter: Chapter):
        a = self.__cur.execute(
            f"SELECT is_completed FROM chapter_history WHERE chapter_id = '{chapter.id}';").fetchall()
        return bool(a)

    @with_lock_thread(lock)
    def get_complete_status(self, chapter: Chapter):
        a = self.__cur.execute(
            f"SELECT is_completed FROM chapter_history WHERE chapter_id = '{chapter.id}';").fetchall()
        return bool(a[0][0])

    @with_lock_thread(lock)
    def add_history_note(self, manga: Manga, chapter: Chapter, is_completed: bool):
        self.__cur.execute(f"INSERT INTO chapter_history VALUES(?, ?, ?);", (chapter.id, manga.id, is_completed))
        self.__con.commit()

    @with_lock_thread(lock)
    def get_history_notes(self) -> list[HistoryNote]:
        notes = []
        a = self.__cur.execute(f"SELECT * FROM chapter_history;").fetchall()
        for i in a:
            chapter = self.get_chapter(i[0])
            manga = self.get_manga(i[1])
            is_completed = bool(i[2])
            notes.append(HistoryNote(0, chapter, manga, is_completed))
        return notes

    @with_lock_thread(lock)
    def del_history_note(self, chapter: Chapter):
        self.__cur.execute(f"DELETE FROM chapter_history WHERE chapter_id = '{chapter.id}';")
        self.__con.commit()
