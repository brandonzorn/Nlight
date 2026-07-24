from collections import defaultdict
import logging
from typing import override

from PySide6.QtCore import QPoint, QSize, QThreadPool, qtTrId, Signal, Slot
from PySide6.QtGui import QIcon, QPixmap, QResizeEvent
from PySide6.QtWidgets import QTreeWidgetItem, QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.info import Ui_InfoPage
from nlightreader.consts.colors import ItemsIcons
from nlightreader.consts.files import NlFluentIcons
from nlightreader.core.enums import Language, LIB_LISTS, LibList
from nlightreader.items import HistoryNote
from nlightreader.models import Chapter, Character, Manga
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.database import Database
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.kodik_server import start_html_video
from nlightreader.utils.text_formatter import description_to_html
from nlightreader.utils.threads import Worker
from nlightreader.utils.utils import get_language_icon
from nlightreader.widgets.contexts import ReadMarkMenu, ReadMarkMode
from nlightreader.widgets.dialogs import CharacterInfoDialog, RateDialog
from nlightreader.widgets.items import (
    GroupTreeItem,
    ModelListItem,
    ModelTreeItem,
)
from nlightreader.windows.reader_window import ReaderWindow

logger = logging.getLogger(__name__)


class InfoPage(QWidget):
    opened_related_manga = Signal(Manga)
    setup_done = Signal()
    setup_error = Signal()

    def __init__(self, manga: Manga) -> None:
        super().__init__()
        self.ui = Ui_InfoPage()
        self.ui.setupUi(self)

        self.ui.scrollArea.enableTransparentBackground()

        self.ui.shikimoriButton.setIcon(
            NlFluentIcons.SHIKIMORI.qicon(),
        )

        self.ui.libraryListComboBox.addItems(
            [qtTrId(f"library-list.{i.capitalize()}") for i in LIB_LISTS],
        )
        self.ui.itemsTree.itemDoubleClicked.connect(
            self.open_reader,
        )
        self.ui.charactersList.doubleClicked.connect(
            self.open_character_dialog,
        )
        self.ui.relatedList.doubleClicked.connect(
            self._open_related_manga,
        )
        self.ui.shikimoriButton.clicked.connect(
            self.open_rate_dialog,
        )
        self.ui.addButton.clicked.connect(
            self.add_to_favorites,
        )
        self.ui.libraryListComboBox.currentIndexChanged.connect(
            self.change_lib_list,
        )
        self.ui.itemsTree.customContextMenuRequested.connect(
            self.on_context_menu,
        )

        self.__db: Database = Database()
        self._thread_pool = QThreadPool()
        self._thread_pool.setMaxThreadCount(3)
        self._workers: list[Worker] = []

        self._manga: Manga = manga
        self._catalog = get_catalog_by_id(self._manga.catalog_id)

        self._related_mangas: list[Manga] = []
        self._related_characters: list[Character] = []
        self._chapters: list[Chapter] = []

        self._grouped_chapters: dict[Language, dict[str | None, list]] = (
            defaultdict(lambda: defaultdict(list))
        )
        self._manga_pixmap = QPixmap()
        self._reader_window = None

    def on_context_menu(self, position: QPoint) -> None:
        context_target = self.ui.itemsTree

        def set_as_read_all() -> None:
            history_notes = []
            chapters_by_lang: list[Chapter] = self._grouped_chapters[
                selected_chapter.language
            ][selected_chapter.translator]
            for i, chapter in enumerate(
                chapters_by_lang[
                    : chapters_by_lang.index(
                        selected_chapter,
                    )
                    + 1
                ],
            ):
                history_notes.append(
                    HistoryNote(chapter, self._manga, True),
                )
                item = selected_item.parent().child(i)
                item.setIcon(
                    0,
                    FluentIcon.ACCEPT_MEDIUM.qicon(),
                )
            self.__db.add_history_notes(history_notes)

        def set_as_read() -> None:
            self.__db.add_history_note(
                HistoryNote(selected_chapter, self._manga, True),
            )
            selected_item.setIcon(
                0,
                FluentIcon.ACCEPT_MEDIUM.qicon(),
            )

        def remove_read_state() -> None:
            self.__db.del_history_note(selected_chapter)
            selected_item.setIcon(0, QIcon())

        menu = ReadMarkMenu()
        selected_item: ModelTreeItem = context_target.itemAt(position)
        if not isinstance(selected_item, ModelTreeItem):
            return
        selected_chapter: Chapter = selected_item.model
        if not self.__db.check_complete_chapter(selected_chapter):
            menu.set_mode(ReadMarkMode.SET_AS_READ)
        elif self.__db.get_complete_status(selected_chapter):
            menu.set_mode(ReadMarkMode.REMOVE_ONLY)
        else:
            menu.set_mode(ReadMarkMode.ALL)
        menu.set_as_read.triggered.connect(set_as_read)
        menu.set_as_read_all.triggered.connect(set_as_read_all)
        menu.remove_read_state.triggered.connect(remove_read_state)
        menu.exec(context_target.mapToGlobal(position))

    @override
    def deleteLater(self, /) -> None:
        self._delete_reader_window()
        super().deleteLater()

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        if event.oldSize().width() != event.size().width():
            self._update_manga_preview_size()

    def _group_chapters(self) -> None:
        self._grouped_chapters.clear()
        for chapter in self._chapters:
            self._grouped_chapters[chapter.language][
                chapter.translator
            ].append(chapter)

    def setup(self) -> None:
        def info_setup() -> None:
            try:
                self._manga = self._catalog.get_manga(self._manga)
                self._fetch_manga_preview()
            except Exception as e:
                logger.error(e)
                self.setup_error.emit()
            finally:
                if self._manga is not None:
                    self.__db.add_manga(self._manga)

        worker = Worker(
            target=info_setup,
            callback=self.update_additional_info,
        )
        self._workers.append(worker)
        worker.start(pool=self._thread_pool)

    def update_add_button_icon(self) -> None:
        if self.ui.addButton.isChecked():
            self.ui.addButton.setIcon(FluentIcon.REMOVE_FROM)
        else:
            self.ui.addButton.setIcon(FluentIcon.ADD_TO)

    def update_additional_info(self) -> None:
        self.ui.libraryWidget.setVisible(not self._catalog.is_primary)
        self.ui.shikimoriWidget.setVisible(self._catalog.is_primary)
        self.set_info()
        if self.__db.check_manga_library(self._manga):
            self.ui.libraryListComboBox.setCurrentIndex(
                self.__db.get_manga_library_list(self._manga).value,
            )
            self.ui.addButton.setChecked(True)
        else:
            self.ui.addButton.setChecked(False)
        self.update_add_button_icon()
        self._set_image()
        chapters_worker = Worker(
            target=self.get_chapters,
            callback=self.update_chapters,
        )
        self._workers.append(chapters_worker)
        chapters_worker.start(pool=self._thread_pool)

        relations_worker = Worker(
            target=self.get_relations,
            callback=self.update_relations,
        )
        self._workers.append(relations_worker)
        relations_worker.start(pool=self._thread_pool)

        characters_worker = Worker(
            target=self.get_characters,
            callback=self.update_characters,
        )
        self._workers.append(characters_worker)
        characters_worker.start(pool=self._thread_pool)

        self.setup_done.emit()

    @Slot()
    def open_rate_dialog(self) -> None:
        RateDialog(self._manga, parent=self).exec()

    @Slot()
    def open_character_dialog(self) -> None:
        current_item: ModelListItem = self.ui.charactersList.currentItem()
        if not isinstance(current_item, ModelListItem):
            return
        character = self._catalog.get_character(current_item.model)
        CharacterInfoDialog(character, parent=self).exec()

    def _fetch_manga_preview(self) -> None:
        self._manga_pixmap = FileManager.get_manga_preview(
            self._manga,
            self._catalog,
        )

    def _set_image(self) -> None:
        self.ui.imageLabel.setImage(self._manga_pixmap)
        self._update_manga_preview_size()

    def _update_manga_preview_size(self) -> None:
        w = self.width() // 5
        image_size = QSize(w, int(w * 1.5))
        self.ui.previewWidget.setFixedWidth(image_size.width())
        self.ui.imageLabel.setScaledSize(image_size)

    def set_info(self) -> None:
        self.ui.name_label.setText(self._manga.name)
        self.ui.russian_label.setText(self._manga.russian)
        self.ui.status_label.setVisible(bool(self._manga.status))
        self.ui.status_label.setText(
            f"{self.tr('Status')}: "
            f"{qtTrId(f'status.{self._manga.status.to_str()}')}",
        )
        self.ui.volumes_label.setVisible(bool(self._manga.volumes))
        self.ui.chapters_label.setVisible(bool(self._manga.chapters))
        self.ui.volumes_label.setText(
            f"{self.tr('Volumes')}: {self._manga.volumes}",
        )
        self.ui.chapters_label.setText(
            f"{self.tr('Chapters')}: {self._manga.chapters}",
        )
        self.ui.catalog_score_label.setVisible(bool(self._manga.score))
        self.ui.catalog_score_label.setText(
            f"{self.tr('Rating')}: {self._manga.score}",
        )
        self.ui.descriptionTextEdit.setHtml(
            description_to_html(self._manga.get_description() or ""),
        )

    @Slot()
    def add_to_favorites(self) -> None:
        if self.__db.check_manga_library(self._manga):
            self.__db.rem_manga_library(self._manga)
        else:
            lib_list = LibList(self.ui.libraryListComboBox.currentIndex())
            self.__db.add_manga_library(self._manga, lib_list)
        self.update_add_button_icon()

    @Slot()
    def change_lib_list(self) -> None:
        if self.__db.check_manga_library(self._manga):
            lib_list = LibList(self.ui.libraryListComboBox.currentIndex())
            self.__db.add_manga_library(self._manga, lib_list)

    def get_chapters(self) -> None:
        try:
            self._chapters = self._catalog.get_chapters(self._manga)
        except NotImplementedError:
            logger.warning(
                "get_chapters is not implemented for %s",
                self._catalog.CATALOG_NAME,
            )
            self._chapters.clear()
            return
        self._chapters.reverse()
        self._group_chapters()
        self.__db.add_chapters(self._chapters, self._manga)

    def update_chapters(self) -> None:
        self.ui.itemsTree.clear()
        self.ui.itemsWidget.setVisible(bool(self._chapters))
        for lang, translators in self._grouped_chapters.items():
            lang_item = GroupTreeItem(
                qtTrId(f"language.{lang.to_str()}"),
                icon=QIcon(get_language_icon(lang)),
            )
            self.ui.itemsTree.addTopLevelItem(lang_item)

            for translator, chapters in translators.items():
                translator_item = lang_item
                if translator is not None:
                    translator_item = GroupTreeItem(translator)
                    lang_item.addChild(translator_item)

                for chapter in chapters:
                    ch_item = ModelTreeItem(chapter)
                    if self.__db.check_complete_chapter(chapter):
                        if self.__db.get_complete_status(chapter):
                            ch_item.setIcon(0, ItemsIcons.READ.qicon())
                        else:
                            ch_item.setIcon(0, ItemsIcons.UNREAD)
                    translator_item.addChild(ch_item)

            if len(self._grouped_chapters) == 1:
                lang_item.setExpanded(True)

    def get_relations(self) -> None:
        try:
            self._related_mangas = self._catalog.get_relations(
                self._manga,
            )
        except NotImplementedError:
            logger.warning(
                "get_relations is not implemented for %s",
                self._catalog.CATALOG_NAME,
            )
            self._related_mangas.clear()

    def update_relations(self) -> None:
        self.ui.relatedList.clear()
        self.ui.relatedWidget.setVisible(bool(self._related_mangas))
        for manga in self._related_mangas:
            item = ModelListItem(manga)
            self.ui.relatedList.addItem(item)

    def get_characters(self) -> None:
        try:
            self._related_characters = self._catalog.get_characters(
                self._manga,
            )
        except NotImplementedError:
            logger.warning(
                "get_characters is not implemented for %s",
                self._catalog.CATALOG_NAME,
            )
            self._related_characters.clear()

    def update_characters(self) -> None:
        self.ui.charactersList.clear()
        self.ui.charactersWidget.setVisible(bool(self._related_characters))
        for character in self._related_characters:
            item = ModelListItem(character)
            self.ui.charactersList.addItem(item)

    def _delete_reader_window(self) -> None:
        if self._reader_window is not None:
            self._reader_window.close()
            self._reader_window.deleteLater()
            self._reader_window = None

    @Slot(QTreeWidgetItem)
    def open_reader(self, item: QTreeWidgetItem) -> None:
        if not isinstance(item, ModelTreeItem):
            return
        try:
            self._delete_reader_window()
        finally:
            selected_chapter: Chapter = item.model
            if hasattr(selected_chapter, "url"):
                start_html_video(self._manga, selected_chapter)
                return
            selected_group = self._grouped_chapters[selected_chapter.language][
                selected_chapter.translator
            ]
            self._reader_window = ReaderWindow(self._manga, selected_group)
            self._reader_window.setup(
                selected_group.index(selected_chapter) + 1,
            )

    @Slot()
    def _open_related_manga(self) -> None:
        self.opened_related_manga.emit(self.ui.relatedList.currentItem().model)


__all__ = ["InfoPage"]
