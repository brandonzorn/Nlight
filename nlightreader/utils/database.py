from typing import Any

import sqlalchemy
from sqlalchemy.dialects.sqlite import insert

from nlightreader.consts.paths import APP_DATA_PATH
from nlightreader.core.enums import Language, LibList, MangaKind, MangaStatus
from nlightreader.core.utils.decorators import singleton
from nlightreader.items import HistoryNote
from nlightreader.models import Chapter, Manga


@singleton
class Database:
    def __init__(self) -> None:
        db_file_path = APP_DATA_PATH / "data_v2.db"
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
                "descriptions",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "score",
                sqlalchemy.Float,
                nullable=False,
            ),
            sqlalchemy.Column(
                "status",
                sqlalchemy.Integer,
            ),
            sqlalchemy.Column(
                "kind",
                sqlalchemy.Integer,
            ),
            sqlalchemy.Column(
                "volumes_number",
                sqlalchemy.Integer,
                nullable=False,
            ),
            sqlalchemy.Column(
                "chapters_number",
                sqlalchemy.Integer,
                nullable=False,
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
                "volume_number",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "chapter_number",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "title",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "language",
                sqlalchemy.Integer,
            ),
            sqlalchemy.Column(
                "manga_id",
                sqlalchemy.Text,
            ),
            sqlalchemy.Column(
                "translator",
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
                "list_id",
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
            ),
        )

        self._metadata.create_all(self.__engine)

    def add_column_migration(
        self,
        column: str,
        table: str,
        params: str,
    ) -> None:
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

    def add_manga(self, manga: Manga) -> None:
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

    def add_mangas(self, mangas: list[Manga]) -> None:
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
    def _make_manga(manga_data: dict[str, Any]) -> Manga:
        manga = Manga(
            content_id=manga_data["content_id"],
            catalog_id=manga_data["catalog_id"],
            name=manga_data["name"],
            russian=manga_data["russian"],
        )
        manga.kind = MangaKind(manga_data["kind"])
        manga.set_description_from_str(manga_data["descriptions"])
        manga.score = manga_data["score"]
        manga.status = MangaStatus(manga_data["status"])
        manga.volumes_number = manga_data["volumes_number"]
        manga.chapters_number = manga_data["chapters_number"]
        manga.preview_url = manga_data["preview_url"]
        return manga

    def get_manga(self, manga_id: str) -> Manga:
        select_manga = sqlalchemy.select(
            self._manga,
        ).where(
            self._manga.c.id == manga_id,
        )
        with self.__engine.connect() as conn:
            select_manga_result = conn.execute(select_manga)
        x = select_manga_result.first()
        return self._make_manga(x._asdict())

    def add_chapters(self, chapters: list[Chapter], manga: Manga) -> None:
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
    def __make_chapter(chapter_data: dict[str, Any]) -> Chapter:
        content_id = chapter_data["content_id"]
        catalog_id = chapter_data["catalog_id"]

        vol_raw = chapter_data["volume_number"]
        ch_raw = chapter_data["chapter_number"]
        title = chapter_data["title"]

        language = Language(chapter_data["language"])

        translator = chapter_data["translator"]

        return Chapter(
            content_id=content_id,
            catalog_id=catalog_id,
            volume_number=vol_raw,
            chapter_number=ch_raw,
            title=title,
            language=language,
            translator=translator,
        )

    def get_chapter(self, chapter_id: str) -> Chapter:
        select_chapter = sqlalchemy.select(
            self._chapters,
        ).where(
            self._chapters.c.id == chapter_id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter)
        a = select_chapter_result.first()
        return self.__make_chapter(a._asdict())

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        select_chapters = sqlalchemy.select(self._chapters).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            select_chapters_result = conn.execute(select_chapters)
        a = select_chapters_result.all()
        chapters = []
        for i in a[::-1]:
            chapters.append(
                self.__make_chapter(i._asdict()),
            )
        return chapters

    def add_manga_library(
        self,
        manga: Manga,
        library_list: LibList = LibList.planned,
    ) -> None:
        lib_manga_data = {"manga_id": manga.id, "list_id": library_list.value}
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

    def get_manga_library(self, lib_list: LibList) -> list[Manga]:
        select_manga_library = (
            sqlalchemy.select(
                self._manga,
            )
            .join(
                self._library,
                self._manga.c.id == self._library.c.manga_id,
            )
            .filter_by(
                list_id=lib_list.value,
            )
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.all()
        return [self._make_manga(data._asdict()) for data in a[::-1]]

    def get_manga_library_list(self, manga: Manga) -> LibList:
        select_manga_library = sqlalchemy.select(
            self._library.c.list_id,
        ).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.first()._asdict()
        return LibList(a["list_id"])

    def check_manga_library(self, manga: Manga) -> bool:
        select_manga_library = sqlalchemy.select(
            self._library.c.list_id,
        ).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_manga_library)
        a = select_chapter_result.first()
        return bool(a)

    def rem_manga_library(self, manga: Manga) -> None:
        delete_manga_library = sqlalchemy.delete(self._library).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            conn.execute(delete_manga_library)
            conn.commit()

    def check_complete_chapter(self, chapter: Chapter) -> bool:
        select_chapter_history = sqlalchemy.select(
            self._chapter_history.c.is_completed,
        ).filter_by(
            chapter_id=chapter.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter_history)
        a = select_chapter_result.all()
        return bool(a)

    def get_complete_status(self, chapter: Chapter) -> bool:
        select_chapter_history = sqlalchemy.select(
            self._chapter_history.c.is_completed,
        ).filter_by(
            chapter_id=chapter.id,
        )
        with self.__engine.connect() as conn:
            select_chapter_result = conn.execute(select_chapter_history)
        a = select_chapter_result.all()
        return bool(a[0][0])

    def add_history_note(self, note: HistoryNote) -> None:
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

    def add_history_notes(self, history_notes: list[HistoryNote]) -> None:
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
        a = select_chapter_result.all()
        notes = []
        for i in a:
            manga = self.get_manga(i[0])
            chapter = self.get_chapter(i[1])
            is_completed = bool(i[2])
            notes.append(HistoryNote(chapter, manga, is_completed))
        return notes

    def del_history_notes(self, manga: Manga) -> None:
        delete_history_notes = sqlalchemy.delete(
            self._chapter_history,
        ).filter_by(
            manga_id=manga.id,
        )
        with self.__engine.connect() as conn:
            conn.execute(delete_history_notes)
            conn.commit()

    def del_history_note(self, chapter: Chapter) -> None:
        delete_history_note = sqlalchemy.delete(
            self._chapter_history,
        ).filter_by(
            chapter_id=chapter.id,
        )
        with self.__engine.connect() as conn:
            conn.execute(delete_history_note)
            conn.commit()


__all__ = ["Database"]
