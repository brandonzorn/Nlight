import logging

import sqlalchemy
from sqlalchemy.dialects.sqlite import insert

from nlightreader.consts.enums import Nl
from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.items import HistoryNote
from nlightreader.models import Chapter, Manga
from nlightreader.utils.decorators import singleton


@singleton
class Database:
    def __init__(self):
        db_file_path = APP_DATA_PATH / "data.db"
        self.__engine = sqlalchemy.create_engine(f"sqlite:///{db_file_path}")
        self._metadata = sqlalchemy.MetaData()

        self._manga = sqlalchemy.Table(
            "manga",
            self._metadata,
            sqlalchemy.Column(
                "id",
                sqlalchemy.Text,
                primary_key=True,
                nullable=False,
            ),
            sqlalchemy.Column(
                "content_id",
                sqlalchemy.Text,
                nullable=False,
            ),
            sqlalchemy.Column(
                "catalog_id",
                sqlalchemy.Integer,
                nullable=False,
            ),
            sqlalchemy.Column(
                "name",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "russian",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "kind",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "description",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "score",
                sqlalchemy.Float,
            ),
            sqlalchemy.Column(
                "status",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "volumes",
                sqlalchemy.Integer,
            ),
            sqlalchemy.Column(
                "chapters",
                sqlalchemy.Integer,
            ),
            sqlalchemy.Column(
                "preview_url",
                sqlalchemy.Text,
            ),
        )

        self._chapters = sqlalchemy.Table(
            "chapters",
            self._metadata,
            sqlalchemy.Column(
                "id",
                sqlalchemy.Text,
                primary_key=True,
                nullable=False,
            ),
            sqlalchemy.Column(
                "content_id",
                sqlalchemy.Text,
                nullable=False,
            ),
            sqlalchemy.Column(
                "catalog_id",
                sqlalchemy.Integer,
                nullable=False,
            ),
            sqlalchemy.Column(
                "vol",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "ch",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "title",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "language",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "manga_id",
                sqlalchemy.Text,
            ),
        )

        self._library = sqlalchemy.Table(
            "library",
            self._metadata,
            sqlalchemy.Column(
                "manga_id",
                sqlalchemy.Text,
                primary_key=True,
                nullable=False,
            ),
            sqlalchemy.Column(
                "list",
                sqlalchemy.Integer,
                nullable=False,
            ),
        )

        self._chapter_history = sqlalchemy.Table(
            "chapter_history",
            self._metadata,
            sqlalchemy.Column(
                "manga_id",
                sqlalchemy.Text,
                nullable=False,
            ),
            sqlalchemy.Column(
                "chapter_id",
                sqlalchemy.Text,
                primary_key=True,
                nullable=False,
            ),
            sqlalchemy.Column(
                "is_completed",
                sqlalchemy.Boolean,
                nullable=True,
            ),
        )

        self._metadata.create_all(self.__engine)

        migrate1 = ("preview_url", "manga", "TEXT")
        self.add_column_migration(*migrate1)

    def add_column_migration(self, column, table, params):
        inspector = sqlalchemy.inspect(self.__engine)
        columns = inspector.get_columns(table)
        columns_names = [column["name"] for column in columns]
        if column in columns_names:
            return
        with self.__engine.connect() as conn:
            conn.execute(
                sqlalchemy.text(f"ALTER TABLE {table} ADD {column} {params};"),
            )
            conn.commit()

    def add_manga(self, manga: Manga):
        manga_data = manga.to_dict()
        manga_insert = (
            insert(
                self._manga,
            )
            .values(
                [manga_data],
            )
            .on_conflict_do_update(
                index_elements=["id"],
                set_=manga_data,
            )
        )
        with self.__engine.connect() as conn:
            conn.execute(manga_insert)
            conn.commit()

    def add_mangas(self, mangas: list[Manga]):
        if not mangas:
            return
        with self.__engine.connect() as conn:
            for manga in mangas:
                manga_data = manga.to_dict()
                manga_insert = (
                    insert(
                        self._manga,
                    )
                    .values(
                        manga_data,
                    )
                    .on_conflict_do_update(
                        index_elements=["id"],
                        set_=manga_data,
                    )
                )
                conn.execute(manga_insert)
            conn.commit()

    @staticmethod
    def _make_manga(manga_data) -> Manga:
        content_id = str(manga_data[1])
        catalog_id = manga_data[2]
        name = manga_data[3]
        russian = manga_data[4]
        manga = Manga(content_id, catalog_id, name, russian)
        manga.kind = Nl.MangaKind.from_str(manga_data[5])
        manga.set_description_from_str(manga_data[6])
        manga.score = manga_data[7]
        manga.status = Nl.MangaStatus.from_str(manga_data[8])
        manga.volumes = manga_data[9]

        chapters = manga_data[10]
        if not isinstance(chapters, int):
            logging.warning(f"Chapters must be int got {type(chapters)}")
            chapters = 0
        manga.chapters = chapters
        manga.preview_url = manga_data[11]
        return manga

    def get_manga(self, manga_id: str):
        select_manga = sqlalchemy.select(
            self._manga,
        ).where(
            self._manga.c.id == manga_id,
        )
        with self.__engine.connect() as conn:
            select_manga_result = conn.execute(select_manga)
        x = select_manga_result.fetchone()
        return self._make_manga(x)

    def add_chapters(self, chapters: list[Chapter], manga: Manga):
        if not chapters or not manga:
            return
        with self.__engine.connect() as conn:
            for chapter in chapters:
                chapter_data = chapter.to_dict() | {
                    "manga_id": manga.id,
                }
                chapters_insert = (
                    insert(
                        self._chapters,
                    )
                    .values(
                        [chapter_data],
                    )
                    .on_conflict_do_update(
                        index_elements=["id"],
                        set_=chapter_data,
                    )
                )
                conn.execute(chapters_insert)
            conn.commit()

    @staticmethod
    def __make_chapter(chapter_data) -> Chapter:
        content_id = str(chapter_data[1])
        catalog_id = chapter_data[2]

        vol_raw = chapter_data[3]
        vol = str(vol_raw) if vol_raw is not None else vol_raw

        ch_raw = chapter_data[4]
        ch = str(ch_raw) if ch_raw is not None else ch_raw

        title = chapter_data[5]
        language = Nl.Language.from_str(chapter_data[6])

        return Chapter(
            content_id,
            catalog_id,
            vol,
            ch,
            title,
            language,
        )

    def get_chapter(self, chapter_id: str):
        select_chapter = sqlalchemy.select(
            self._chapters,
        ).where(
            self._chapters.c.id == chapter_id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter)
        a = select_chapter_result.fetchone()
        return self.__make_chapter(a)

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        select_chapters = sqlalchemy.select(self._chapters).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            select_chapters_result = conn.execute(select_chapters)
        a = select_chapters_result.fetchall()
        chapters = []
        for i in a[::-1]:
            chapters.append(
                self.__make_chapter(i),
            )
        return chapters

    def add_manga_library(
        self,
        manga: Manga,
        lib_list: Nl.LibList = Nl.LibList.planned,
    ):
        lib_manga_data = {"manga_id": manga.id, "list": lib_list.value}
        manga_library_insert = (
            insert(
                self._library,
            )
            .values(
                [lib_manga_data],
            )
            .on_conflict_do_update(
                index_elements=["manga_id"],
                set_=lib_manga_data,
            )
        )
        with self.__engine.connect() as conn:
            conn.execute(manga_library_insert)
            conn.commit()

    def get_manga_library(self, lib_list: Nl.LibList) -> list[Manga]:
        select_manga_library = (
            sqlalchemy.select(
                self._manga,
            )
            .join(
                self._library,
                self._manga.c.id == self._library.c.manga_id,
            )
            .filter_by(
                list=lib_list.value,
            )
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.fetchall()
        return [self._make_manga(data) for data in a[::-1]]

    def get_manga_library_list(self, manga: Manga) -> Nl.LibList:
        select_manga_library = sqlalchemy.select(
            self._library.c.list,
        ).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.fetchone()
        return Nl.LibList(a[0])

    def check_manga_library(self, manga: Manga) -> bool:
        select_manga_library = sqlalchemy.select(
            self._library.c.list,
        ).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.fetchone()
        return bool(a)

    def rem_manga_library(self, manga: Manga):
        delete_manga_library = sqlalchemy.delete(self._library).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            conn.execute(delete_manga_library)
            conn.commit()

    def check_complete_chapter(self, chapter: Chapter):
        select_chapter_history = sqlalchemy.select(
            self._chapter_history.c.is_completed,
        ).filter_by(
            chapter_id=chapter.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter_history)
        a = select_chapter_result.fetchall()
        return bool(a)

    def get_complete_status(self, chapter: Chapter):
        select_chapter_history = sqlalchemy.select(
            self._chapter_history.c.is_completed,
        ).filter_by(
            chapter_id=chapter.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter_history)
        a = select_chapter_result.fetchall()
        return bool(a[0][0])

    def add_history_note(self, note: HistoryNote):
        note_data = note.to_dict()
        history_note_insert = (
            insert(
                self._chapter_history,
            )
            .values(
                [note_data],
            )
            .on_conflict_do_update(
                index_elements=["chapter_id"],
                set_=note_data,
            )
        )
        with self.__engine.connect() as conn:
            conn.execute(history_note_insert)
            conn.commit()

    def add_history_notes(self, history_notes: list[HistoryNote]):
        if not history_notes:
            return
        with self.__engine.connect() as conn:
            for note in history_notes:
                note_data = note.to_dict()
                history_notes_insert = (
                    insert(
                        self._chapter_history,
                    )
                    .values(
                        [note_data],
                    )
                    .on_conflict_do_update(
                        index_elements=["chapter_id"],
                        set_=note_data,
                    )
                )
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
        delete_history_notes = sqlalchemy.delete(
            self._chapter_history,
        ).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            conn.execute(delete_history_notes)
            conn.commit()

    def del_history_note(self, chapter: Chapter):
        delete_history_note = sqlalchemy.delete(
            self._chapter_history,
        ).filter_by(
            chapter_id=chapter.id,
        )
        with self.__engine.connect() as conn:
            conn.execute(delete_history_note)
            conn.commit()


__all__ = [
    "Database",
]
