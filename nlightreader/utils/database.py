import os
import sqlite3
from threading import Lock

from nlightreader.consts import APP_NAME, LibList
from nlightreader.items import Chapter, Manga, HistoryNote
from nlightreader.utils.decorators import with_lock_thread, singleton


@singleton
class Database:

    lock = Lock()

    def __init__(self):
        self.__con = sqlite3.connect(f'{os.getcwd()}/{APP_NAME}/data.db', check_same_thread=False)
        self.__cur = self.__con.cursor()
        self.__cur.execute(
            """CREATE TABLE IF NOT EXISTS manga (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        content_id STRING NOT NULL, catalog_id INTEGER NOT NULL, name STRING, russian STRING, kind STRING,
        description TEXT, score FLOAT, status STRING, volumes INTEGER, chapters INTEGER);
            """)
        self.__cur.execute(
            """CREATE TABLE IF NOT EXISTS chapters (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        content_id STRING NOT NULL, catalog_id INTEGER NOT NULL, vol STRING, ch STRING, title STRING, language STRING,
        manga_id INTEGER, index_n INTEGER);
            """)
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS library
        (manga_id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL, list INTEGER NOT NULL)
            """)
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS chapter_history
        (manga_id STRING NOT NULL, chapter_id STRING NOT NULL UNIQUE ON CONFLICT REPLACE, is_completed BOOLEAN)
            """)
        self.__con.commit()

    @with_lock_thread(lock)
    def add_manga(self, manga: Manga):
        self.__cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                           (manga.id, manga.content_id, manga.catalog_id, manga.name, manga.russian, manga.kind,
                            manga.description, manga.score, manga.status, manga.volumes, manga.chapters))
        self.__con.commit()

    @with_lock_thread(lock)
    def add_mangas(self, mangas: list[Manga]):
        for manga in mangas:
            self.__cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                               (manga.id, manga.content_id, manga.catalog_id, manga.name, manga.russian, manga.kind,
                                manga.description, manga.score, manga.status, manga.volumes, manga.chapters))
        self.__con.commit()

    def get_manga(self, manga_id: str):
        x = self.__cur.execute(f"SELECT * FROM manga WHERE id = '{manga_id}'").fetchone()
        content_id = x[1]
        catalog_id = x[2]
        name = x[3]
        russian = x[4]
        manga = Manga(content_id, catalog_id, name, russian)
        manga.kind = x[5]
        manga.description = x[6]
        manga.score = x[7]
        manga.status = x[8]
        manga.volumes = x[9]
        manga.chapters = x[10]
        return manga

    @with_lock_thread(lock)
    def add_chapters(self, chapters: list[Chapter], manga: Manga):
        for chapter in chapters:
            index = chapters[::-1].index(chapter)
            self.__cur.execute("INSERT INTO chapters VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);",
                               (chapter.id, chapter.content_id, chapter.catalog_id, chapter.vol, chapter.ch,
                                chapter.title, chapter.language, manga.id, index))
        self.__con.commit()

    def get_chapter(self, chapter_id: str):
        a = self.__cur.execute(f"SELECT * FROM chapters WHERE id = '{chapter_id}'").fetchone()
        content_id = a[1]
        catalog_id = a[2]
        vol = a[3]
        ch = a[4]
        title = a[5]
        language = a[6]
        return Chapter(content_id, catalog_id, vol, ch, title, language)

    @with_lock_thread(lock)
    def get_chapters(self, manga: Manga) -> list[Chapter]:
        a = self.__cur.execute(f"SELECT * FROM chapters WHERE manga_id = '{manga.id}' ORDER by index_n").fetchall()
        return [Chapter(i[1], i[2], i[3], i[4], i[5], a[6]) for i in a[::-1]]

    @with_lock_thread(lock)
    def add_manga_library(self, manga: Manga, lib_list: LibList = LibList.planned):
        self.__cur.execute(f"INSERT INTO library VALUES(?, ?);", (manga.id, lib_list.value))
        self.__con.commit()

    @with_lock_thread(lock)
    def get_manga_library(self, lib_list: LibList) -> list[Manga]:
        a = self.__cur.execute(f"SELECT manga_id FROM library WHERE list = '{lib_list.value}';").fetchall()
        mangas = []
        for i in a[::-1]:
            mangas.append(self.get_manga(i[0]))
        return mangas

    @with_lock_thread(lock)
    def check_manga_library(self, manga: Manga) -> LibList:
        a = self.__cur.execute(f"SELECT list FROM library WHERE manga_id = '{manga.id}';").fetchall()
        if a and a[0]:
            return LibList(a[0][0])

    @with_lock_thread(lock)
    def rem_manga_library(self, manga: Manga):
        self.__cur.execute(f"DELETE FROM library WHERE manga_id = '{manga.id}';")
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
    def add_history_note(self, note: HistoryNote):
        self.__cur.execute(f"INSERT INTO chapter_history VALUES(?, ?, ?);",
                           (note.manga.id, note.chapter.id, note.is_completed))
        self.__con.commit()

    @with_lock_thread(lock)
    def add_history_notes(self, history_notes: list[HistoryNote]):
        for note in history_notes:
            self.__cur.execute(f"INSERT INTO chapter_history VALUES(?, ?, ?);",
                               (note.manga.id, note.chapter.id, note.is_completed))
        self.__con.commit()

    @with_lock_thread(lock)
    def get_history_notes(self) -> list[HistoryNote]:
        notes = []
        a = self.__cur.execute(f"SELECT * FROM chapter_history;").fetchall()
        for i in a:
            manga = self.get_manga(i[0])
            chapter = self.get_chapter(i[1])
            is_completed = bool(i[2])
            notes.append(HistoryNote(chapter, manga, is_completed))
        return notes

    @with_lock_thread(lock)
    def del_history_notes(self, manga: Manga):
        self.__cur.execute(f"DELETE FROM chapter_history WHERE manga_id = '{manga.id}';")
        self.__con.commit()

    @with_lock_thread(lock)
    def del_history_note(self, chapter: Chapter):
        self.__cur.execute(f"DELETE FROM chapter_history WHERE chapter_id = '{chapter.id}';")
        self.__con.commit()
