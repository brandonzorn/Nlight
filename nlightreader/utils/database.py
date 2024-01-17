import sqlalchemy
import platformdirs

from nlightreader.consts import APP_NAME, Nl
from nlightreader.items import Chapter, Manga, HistoryNote
from nlightreader.utils.decorators import singleton


@singleton
class Database:
    def __init__(self):
        db_file_path = f"{platformdirs.user_data_dir()}/{APP_NAME}/data.db"
        self.__engine = sqlalchemy.create_engine(f"sqlite:///{db_file_path}")
        self._metadata = sqlalchemy.MetaData()

        self._manga = sqlalchemy.Table(
            "manga", self._metadata,
            sqlalchemy.Column("id", sqlalchemy.String, primary_key=True, nullable=False),
            sqlalchemy.Column("content_id", sqlalchemy.String, nullable=False),
            sqlalchemy.Column("catalog_id", sqlalchemy.Integer, nullable=False),
            sqlalchemy.Column("name", sqlalchemy.String),
            sqlalchemy.Column("russian", sqlalchemy.String),
            sqlalchemy.Column("kind", sqlalchemy.String),
            sqlalchemy.Column("description", sqlalchemy.Text),
            sqlalchemy.Column("score", sqlalchemy.Float),
            sqlalchemy.Column("status", sqlalchemy.String),
            sqlalchemy.Column("volumes", sqlalchemy.Integer),
            sqlalchemy.Column("chapters", sqlalchemy.Integer),
            sqlalchemy.Column("preview_url", sqlalchemy.String),
        )

        self._chapters = sqlalchemy.Table(
            "chapters", self._metadata,
            sqlalchemy.Column("id", sqlalchemy.String, primary_key=True, nullable=False),
            sqlalchemy.Column("content_id", sqlalchemy.String, nullable=False),
            sqlalchemy.Column("catalog_id", sqlalchemy.Integer, nullable=False),
            sqlalchemy.Column("vol", sqlalchemy.String),
            sqlalchemy.Column("ch", sqlalchemy.String),
            sqlalchemy.Column("title", sqlalchemy.String),
            sqlalchemy.Column("language", sqlalchemy.String),
            sqlalchemy.Column("manga_id", sqlalchemy.String),
        )

        self._library = sqlalchemy.Table(
            "library", self._metadata,
            sqlalchemy.Column("manga_id", sqlalchemy.String, primary_key=True, nullable=False),
            sqlalchemy.Column("list", sqlalchemy.Integer, nullable=False),
        )

        self._chapter_history = sqlalchemy.Table(
            "chapter_history", self._metadata,
            sqlalchemy.Column("manga_id", sqlalchemy.String, primary_key=True, nullable=False),
            sqlalchemy.Column("chapter_id", sqlalchemy.String, nullable=False, unique=True),
            sqlalchemy.Column("is_completed", sqlalchemy.Boolean, nullable=True),
        )

        self._metadata.create_all(self.__engine)

        migrate1 = ("preview_url", "manga", "STRING",)
        self.add_column_migration(*migrate1)

    def add_column_migration(self, column, table, params):
        inspector = sqlalchemy.inspect(self.__engine)
        columns = inspector.get_columns(table)
        columns_names = [column["name"] for column in columns]
        if column in columns_names:
            return
        with self.__engine.connect() as conn:
            conn.execute(sqlalchemy.text(f"ALTER TABLE {table} ADD {column} {params};"))
            conn.commit()

    def add_manga(self, manga: Manga):
        manga_insert = self._manga.insert().values(
            [
                {
                    "id": manga.id, "content_id": manga.content_id, "catalog_id": manga.catalog_id, "name": manga.name,
                    "russian": manga.russian, "kind": manga.kind.name, "description": manga.descriptions_to_str(),
                    "score": manga.score, "status": manga.status, "volumes": manga.volumes, "chapters": manga.chapters,
                    "preview_url": manga.preview_url,
                },
            ],
        )
        with self.__engine.connect() as conn:
            conn.execute(manga_insert)
            conn.commit()

    def add_mangas(self, mangas: list[Manga]):
        if not mangas:
            return
        manga_insert = self._manga.insert().values(
            [
                {
                    "id": manga.id, "content_id": manga.content_id, "catalog_id": manga.catalog_id, "name": manga.name,
                    "russian": manga.russian, "kind": manga.kind.name, "description": manga.descriptions_to_str(),
                    "score": manga.score, "status": manga.status, "volumes": manga.volumes, "chapters": manga.chapters,
                    "preview_url": manga.preview_url,
                } for manga in mangas
            ],
        )
        with self.__engine.connect() as conn:
            conn.execute(manga_insert)
            conn.commit()

    @staticmethod
    def _make_manga(manga_data) -> Manga:
        content_id = manga_data[1]
        catalog_id = manga_data[2]
        name = manga_data[3]
        russian = manga_data[4]
        manga = Manga(content_id, catalog_id, name, russian)
        manga.kind = Nl.MangaKind.from_str(manga_data[5])
        manga.set_description_from_str(manga_data[6])
        manga.score = manga_data[7]
        manga.status = manga_data[8]
        manga.volumes = manga_data[9]
        manga.chapters = manga_data[10]
        manga.preview_url = manga_data[11]
        return manga

    def get_manga(self, manga_id: str):
        select_manga = sqlalchemy.select(self._manga).where(self._manga.c.id == manga_id)
        with self.__engine.connect() as conn:
            select_manga_result = conn.execute(select_manga)
        x = select_manga_result.fetchone()
        return self._make_manga(x)

    def add_chapters(self, chapters: list[Chapter], manga: Manga):
        if not chapters or not manga:
            return
        chapters_insert = self._chapters.insert().values(
            [
                {
                    "id": chapter.id, "content_id": chapter.content_id, "catalog_id": chapter.catalog_id,
                    "vol": chapter.vol, "ch": chapter.ch, "title": chapter.title, "language": chapter.language.name,
                    "manga_id": manga.id,
                } for chapter in chapters
            ],
        )
        with self.__engine.connect() as conn:
            conn.execute(chapters_insert)
            conn.commit()

    def get_chapter(self, chapter_id: str):
        select_chapter = sqlalchemy.select(self._chapters).where(self._chapters.c.id == chapter_id)
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter)
        a = select_chapter_result.fetchone()
        content_id = a[1]
        catalog_id = a[2]
        vol = a[3]
        ch = a[4]
        title = a[5]
        language = Nl.Language.from_str(a[6])

        chapter = Chapter(content_id, catalog_id, vol, ch, title)
        chapter.language = language
        return chapter

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        select_chapters = sqlalchemy.select(self._chapters).where(self._chapters.c.manga_id == manga.id)
        with self.__engine.connect() as conn:
            select_chapters_result = conn.execute(select_chapters)
        a = select_chapters_result.fetchall()
        chapters = []
        for i in a[::-1]:
            chapter = Chapter(i[1], i[2], i[3], i[4], i[5])
            chapter.language = Nl.Language.from_str(a[6])
            chapters.append(chapter)
        return chapters

    def add_manga_library(self, manga: Manga, lib_list: Nl.LibList = Nl.LibList.planned):
        manga_library_insert = self._library.insert().values(
            [
                {"manga_id": manga.id, "list": lib_list.value},
            ],
        )
        with self.__engine.connect() as conn:
            conn.execute(manga_library_insert)
            conn.commit()

    def get_manga_library(self, lib_list: Nl.LibList) -> list[Manga]:
        select_manga_library = sqlalchemy.select(self._manga).join(
            self._library, self._manga.c.id == self._library.c.manga_id).where(self._library.c.list == lib_list.value)
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.fetchall()
        return [self._make_manga(data) for data in a[::-1]]

    def get_manga_library_list(self, manga: Manga) -> Nl.LibList:
        select_manga_library = sqlalchemy.select(self._library.c.list).where(self._library.c.manga_id == manga.id)
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.fetchone()
        return Nl.LibList(a[0])

    def check_manga_library(self, manga: Manga) -> bool:
        select_manga_library = sqlalchemy.select(self._library.c.list).where(self._library.c.manga_id == manga.id)
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.fetchone()
        return bool(a)

    def rem_manga_library(self, manga: Manga):
        delete_manga_library = sqlalchemy.delete(self._library).where(
            self._library.c.manga_id == manga.id)
        with self.__engine.connect() as conn:
            conn.execute(delete_manga_library)
            conn.commit()

    def check_complete_chapter(self, chapter: Chapter):
        select_chapter_history = sqlalchemy.select(self._chapter_history.c.is_completed).where(
            self._chapter_history.c.chapter_id == chapter.id)
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter_history)
        a = select_chapter_result.fetchall()
        return bool(a)

    def get_complete_status(self, chapter: Chapter):
        select_chapter_history = sqlalchemy.select(self._chapter_history.c.is_completed).where(
            self._chapter_history.c.chapter_id == chapter.id)
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter_history)
        a = select_chapter_result.fetchall()
        return bool(a[0][0])

    def add_history_note(self, note: HistoryNote):
        history_note_insert = self._chapter_history.insert().values(
            [
                {"manga_id": note.manga.id, "chapter_id": note.chapter.id, "is_completed": note.is_completed},
            ],
        )
        with self.__engine.connect() as conn:
            conn.execute(history_note_insert)
            conn.commit()

    def add_history_notes(self, history_notes: list[HistoryNote]):
        if not history_notes:
            return
        history_notes_insert = self._chapter_history.insert().values(
            [
                {"manga_id": note.manga.id, "chapter_id": note.chapter.id, "is_completed": note.is_completed}
                for note in history_notes
            ],
        )
        with self.__engine.connect() as conn:
            conn.execute(history_notes_insert)
            conn.commit()

    def get_history_notes(self) -> list[HistoryNote]:
        select_chapter_history = sqlalchemy.select(self._chapter_history)
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter_history)
        a = select_chapter_result.fetchall()
        notes = []
        for i in a:
            manga = self.get_manga(i[0])
            chapter = self.get_chapter(i[1])
            is_completed = bool(i[2])
            notes.append(HistoryNote(chapter, manga, is_completed))
        return notes

    def del_history_notes(self, manga: Manga):
        delete_history_notes = sqlalchemy.delete(self._chapter_history).where(
            self._chapter_history.c.manga_id == manga.id)
        with self.__engine.connect() as conn:
            conn.execute(delete_history_notes)
            conn.commit()

    def del_history_note(self, chapter: Chapter):
        delete_history_note = sqlalchemy.delete(self._chapter_history).where(
            self._chapter_history.c.chapter_id == chapter.id)
        with self.__engine.connect() as conn:
            conn.execute(delete_history_note)
            conn.commit()
