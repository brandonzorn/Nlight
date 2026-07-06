import logging
from typing import override

from PySide6.QtCore import QPoint, QSize, Qt, QThreadPool, Signal, Slot
from PySide6.QtGui import QIcon, QResizeEvent
from PySide6.QtWidgets import QListWidgetItem, QTreeWidgetItem, QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.info import Ui_InfoPage
from nlightreader.consts.colors import ItemsIcons
from nlightreader.consts.files import NlFluentIcons
from nlightreader.core.enums import LIB_LISTS, LibList
from nlightreader.items import HistoryNote
from nlightreader.models import Chapter, Character, Manga
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.database import Database
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.kodik_server import start_html_video
from nlightreader.utils.text_formatter import description_to_html
from nlightreader.utils.threads import Worker
from nlightreader.utils.translator import translate
from nlightreader.utils.utils import get_language_icon
from nlightreader.widgets.contexts import ReadMarkMenu, ReadMarkMode
from nlightreader.widgets.dialogs import CharacterInfoDialog, RateDialog
from nlightreader.widgets.items import ChapterTreeItem
from nlightreader.windows.reader_window import ReaderWindow

logger = logging.getLogger(__name__)


class InfoPage(QWidget):
    opened_related_manga = Signal(Manga)
    setup_done = Signal()
    setup_error = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_InfoPage()
        self.ui.setupUi(self)

        self.ui.shikimoriButton.setIcon(
            NlFluentIcons.SHIKIMORI.qicon(),
        )

        self.ui.libraryListComboBox.addItems(
            [translate("Form", i.capitalize()) for i in LIB_LISTS],
        )
        self.ui.itemsTree.doubleClicked.connect(
            self.open_reader,
        )
        self.ui.charactersList.doubleClicked.connect(
            self.open_character_dialog,
        )
        self.ui.relatedList.doubleClicked.connect(
            self.open_related_manga,
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

        self.ui.scrollArea.resizeEvent = self.scroll_area_resize_event

        self.__db: Database = Database()
        self.__thread_pool = QThreadPool()
        self.__thread_pool.setMaxThreadCount(3)
        self._catalog: AbstractCatalog | None = None
        self._manga = None
        self.__related_mangas: list[Manga] = []
        self.__related_characters: list[Character] = []
        self.__chapters: list[Chapter] = []
        self.__sorted_chapters = {}
        self._manga_pixmap = None
        self.__reader_window = None

    def on_context_menu(self, position: QPoint) -> None:
        context_target = self.ui.itemsTree

        def set_as_read_all() -> None:
            history_notes = []
            chapters_by_lang: list[Chapter] = self.__sorted_chapters[
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
        selected_item = context_target.itemAt(position)
        if not selected_item or not isinstance(selected_item, ChapterTreeItem):
            return
        selected_chapter = selected_item.chapter
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
    def resizeEvent(self, event: QResizeEvent) -> None:
        if not self._catalog or not self._manga or not self._manga_pixmap:
            return
        self.update_manga_preview()
        super().resizeEvent(event)

    def scroll_area_resize_event(self, event: QResizeEvent) -> None:
        self.ui.scrollAreaWidgetContents.setFixedWidth(
            event.size().width(),
        )

    def sort_chapters(self) -> None:
        self.__sorted_chapters.clear()
        for chapter in self.__chapters:
            ch_lang = chapter.language
            if ch_lang not in self.__sorted_chapters:
                self.__sorted_chapters[ch_lang] = {}
            if chapter.translator not in self.__sorted_chapters[ch_lang]:
                self.__sorted_chapters[ch_lang][chapter.translator] = []
            (
                self.__sorted_chapters[ch_lang][chapter.translator].append(
                    chapter,
                )
            )

    def _get_selected_chapter(self) -> Chapter | None:
        selected_item = self.ui.itemsTree.currentItem()
        if not isinstance(selected_item, ChapterTreeItem):
            return None
        return selected_item.chapter

    def get_selected_related_title(self) -> Manga:
        current_index = self.ui.relatedList.currentIndex().row()
        return self._catalog.get_manga(self.__related_mangas[current_index])

    def setup(self, manga: Manga) -> None:
        def info_setup() -> None:
            try:
                self._catalog = get_catalog_by_id(manga.catalog_id)
                self._manga = self._catalog.get_manga(manga)
                self.__db.add_manga(self._manga)
            except Exception as e:
                logger.error(e)
                self.setup_error.emit()

        Worker(
            target=info_setup,
            callback=self.update_additional_info,
        ).start(pool=self.__thread_pool)

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
        self.update_manga_preview()
        Worker(
            target=self.get_chapters,
            callback=self.update_chapters,
        ).start(pool=self.__thread_pool)

        Worker(
            target=self.get_relations,
            callback=self.update_relations,
        ).start(pool=self.__thread_pool)

        Worker(
            target=self.get_characters,
            callback=self.update_characters,
        ).start(pool=self.__thread_pool)

        self.setup_done.emit()

    @Slot()
    def open_rate_dialog(self) -> None:
        RateDialog(self._manga, parent=self).exec()

    @Slot()
    def open_character_dialog(self) -> None:
        current_index = self.ui.charactersList.currentIndex().row()
        character = self._catalog.get_character(
            self.__related_characters[current_index],
        )
        CharacterInfoDialog(character, parent=self).exec()

    def update_manga_preview(self) -> None:
        self.ui.imageLabel.clear()
        if not self._manga_pixmap:
            self._manga_pixmap = FileManager.get_manga_preview(
                self._manga,
                self._catalog,
            )
        image_size = QSize(self.width() // 5, self.height() // 2)
        pixmap = self._manga_pixmap.scaled(
            image_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.ui.previewWidget.setFixedWidth(pixmap.width())
        self.ui.imageLabel.setPixmap(pixmap)

    def set_info(self) -> None:
        self.ui.name_label.setText(self._manga.name)
        self.ui.russian_label.setText(self._manga.russian)
        self.ui.status_label.setVisible(bool(self._manga.status))
        self.ui.status_label.setText(
            f"{translate('Other', 'Status')}: "
            f"{translate('Status', self._manga.status.to_str())}",
        )
        self.ui.volumes_label.setVisible(bool(self._manga.volumes))
        self.ui.chapters_label.setVisible(bool(self._manga.chapters))
        self.ui.volumes_label.setText(
            f"{translate('Other', 'Volumes')}: {self._manga.volumes}",
        )
        self.ui.chapters_label.setText(
            f"{translate('Other', 'Chapters')}: {self._manga.chapters}",
        )
        self.ui.catalog_score_label.setVisible(bool(self._manga.score))
        self.ui.catalog_score_label.setText(
            f"{translate('Other', 'Rating')}: {self._manga.score}",
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
        self.__chapters = self._catalog.get_chapters(self._manga)
        self.__chapters.reverse()
        self.sort_chapters()
        self.__db.add_chapters(self.__chapters, self._manga)

    def update_chapters(self) -> None:
        self.ui.itemsTree.clear()
        self.ui.itemsWidget.setVisible(bool(self.__chapters))
        for lang, translators in self.__sorted_chapters.items():
            lang_item = QTreeWidgetItem(
                [translate("NlLanguage", lang.to_str())],
            )
            lang_item.setIcon(0, QIcon(get_language_icon(lang)))
            self.ui.itemsTree.addTopLevelItem(lang_item)

            for translator, chapters in translators.items():
                translator_item = lang_item
                if translator is not None:
                    translator_item = QTreeWidgetItem([translator])
                    lang_item.addChild(translator_item)

                for chapter in chapters:
                    ch_item = ChapterTreeItem(chapter)
                    if self.__db.check_complete_chapter(chapter):
                        if self.__db.get_complete_status(chapter):
                            ch_item.setIcon(0, ItemsIcons.READ.qicon())
                        else:
                            ch_item.setIcon(0, ItemsIcons.UNREAD.qicon())
                    translator_item.addChild(ch_item)

            if len(self.__sorted_chapters) == 1:
                lang_item.setExpanded(True)

    def get_relations(self) -> None:
        self.__related_mangas = self._catalog.get_relations(self._manga)

    def update_relations(self) -> None:
        self.ui.relatedList.clear()
        self.ui.relatedWidget.setVisible(bool(self.__related_mangas))
        for manga in self.__related_mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.relatedList.addItem(item)

    def get_characters(self) -> None:
        self.__related_characters = self._catalog.get_characters(self._manga)

    def update_characters(self) -> None:
        self.ui.charactersList.clear()
        self.ui.charactersWidget.setVisible(bool(self.__related_characters))
        for character in self.__related_characters:
            item = QListWidgetItem(character.get_name())
            self.ui.charactersList.addItem(item)

    @Slot()
    def open_reader(self) -> None:
        try:
            if self.__reader_window is not None:
                self.__reader_window.close()
        except RuntimeError:
            pass
        finally:
            selected_chapter = self._get_selected_chapter()
            if selected_chapter:
                if hasattr(selected_chapter, "url"):
                    start_html_video(self._manga, selected_chapter)
                    return
                self.__reader_window = ReaderWindow()
                self.__reader_window.setup(
                    self._manga,
                    self.__chapters,
                    self.__chapters.index(selected_chapter) + 1,
                )

    @Slot()
    def open_related_manga(self) -> None:
        self.opened_related_manga.emit(self.get_selected_related_title())


__all__ = ["InfoPage"]
