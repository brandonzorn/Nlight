import logging

from PySide6.QtCore import QSize, Qt, QThreadPool, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidgetItem, QTreeWidgetItem, QWidget
from qfluentwidgets import FluentIcon

from data.ui.widgets.info import Ui_Form
from nlightreader.consts.colors import ItemsIcons
from nlightreader.consts.enums import LIB_LISTS, Nl
from nlightreader.consts.files import NlFluentIcons
from nlightreader.contexts import ReadMarkMenu
from nlightreader.dialogs import FormCharacter, FormRate
from nlightreader.items import HistoryNote
from nlightreader.models import Chapter, Character, Manga
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.catalog_manager import get_catalog_by_id
from nlightreader.utils.database import Database
from nlightreader.utils.file_manager import FileManager
from nlightreader.utils.html_video import start_html_video
from nlightreader.utils.text_formatter import description_to_html
from nlightreader.utils.threads import Worker
from nlightreader.utils.translator import translate
from nlightreader.utils.utils import get_language_icon
from nlightreader.widgets.NlightWidgets import ChapterTreeItem
from nlightreader.windows.Reader import ReaderWindow


class FormInfo(QWidget):
    opened_related_manga = Signal(Manga)
    setup_done = Signal()
    setup_error = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.shikimori_btn.setIcon(
            NlFluentIcons.SHIKIMORI.qicon(),
        )

        self.setObjectName("FormInfo")

        self.ui.lib_list_box.addItems(
            [translate("Form", i.capitalize()) for i in LIB_LISTS],
        )
        self.ui.items_tree.doubleClicked.connect(
            self.open_reader,
        )
        self.ui.characters_list.doubleClicked.connect(
            self.open_character,
        )
        self.ui.related_list.doubleClicked.connect(
            self.open_related_manga,
        )
        self.ui.shikimori_btn.clicked.connect(
            self.open_rate,
        )
        self.ui.add_btn.clicked.connect(
            self.add_to_favorites,
        )
        self.ui.lib_list_box.currentIndexChanged.connect(
            self.change_lib_list,
        )
        self.ui.items_tree.customContextMenuRequested.connect(
            self.on_context_menu,
        )

        self.ui.scrollArea.resizeEvent = self.scroll_area_resize_event

        self.__db: Database = Database()
        self.__thread_pool = QThreadPool()
        self.__thread_pool.setMaxThreadCount(3)
        self.__catalog: AbstractCatalog | None = None
        self.__manga = None
        self.__related_mangas: list[Manga] = []
        self.__related_characters: list[Character] = []
        self.__chapters: list[Chapter] = []
        self.__sorted_chapters = {}
        self.__manga_pixmap = None
        self.__reader_window = None
        self.__rate_window = None
        self.__character_window = None

    def on_context_menu(self, pos):
        context_target = self.ui.items_tree

        def set_as_read_all():
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
                    HistoryNote(chapter, self.__manga, True),
                )
                item = selected_item.parent().child(i)
                item.setIcon(
                    0,
                    FluentIcon.ACCEPT_MEDIUM.qicon(),
                )
            self.__db.add_history_notes(history_notes)

        def set_as_read():
            self.__db.add_history_note(
                HistoryNote(selected_chapter, self.__manga, True),
            )
            selected_item.setIcon(
                0,
                FluentIcon.ACCEPT_MEDIUM.qicon(),
            )

        def remove_read_state():
            self.__db.del_history_note(selected_chapter)
            selected_item.setIcon(0, QIcon())

        menu = ReadMarkMenu()
        selected_item = context_target.itemAt(pos)
        if not selected_item or not isinstance(selected_item, ChapterTreeItem):
            return
        selected_chapter = selected_item.chapter
        if not self.__db.check_complete_chapter(selected_chapter):
            menu.set_mode(0)
        else:
            if self.__db.get_complete_status(selected_chapter):
                menu.set_mode(1)
            else:
                menu.set_mode(2)
        menu.set_as_read.triggered.connect(set_as_read)
        menu.set_as_read_all.triggered.connect(set_as_read_all)
        menu.remove_read_state.triggered.connect(remove_read_state)
        menu.exec(context_target.mapToGlobal(pos))

    def resizeEvent(self, event):
        if not self.__catalog or not self.__manga or not self.__manga_pixmap:
            return
        self.update_manga_preview()

    def scroll_area_resize_event(self, event):
        self.ui.scrollAreaWidgetContents.setFixedWidth(
            event.size().width(),
        )

    def sort_chapters(self):
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
        selected_item = self.ui.items_tree.currentItem()
        if not isinstance(selected_item, ChapterTreeItem):
            return
        return selected_item.chapter

    def get_selected_related_title(self):
        return self.__catalog.get_manga(
            self.__related_mangas[self.ui.related_list.currentIndex().row()],
        )

    def setup(self, manga):
        def info_setup():
            try:
                self.__catalog = get_catalog_by_id(manga.catalog_id)
                self.__manga = self.__catalog.get_manga(manga)
                self.__db.add_manga(self.__manga)
            except Exception as e:
                logging.error(e)
                self.setup_error.emit()

        Worker(
            target=info_setup,
            callback=self.update_additional_info,
        ).start(pool=self.__thread_pool)

    def update_add_button_icon(self):
        if self.ui.add_btn.isChecked():
            self.ui.add_btn.setIcon(FluentIcon.REMOVE_FROM)
        else:
            self.ui.add_btn.setIcon(FluentIcon.ADD_TO)

    def update_additional_info(self):
        self.ui.lib_frame.setVisible(not self.__catalog.is_primary)
        self.ui.shikimori_frame.setVisible(self.__catalog.is_primary)
        self.set_info()
        if self.__db.check_manga_library(self.__manga):
            self.ui.lib_list_box.setCurrentIndex(
                self.__db.get_manga_library_list(self.__manga).value,
            )
            self.ui.add_btn.setChecked(True)
        else:
            self.ui.add_btn.setChecked(False)
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
    def open_rate(self):
        self.__rate_window = FormRate(self.__manga, parent=self)
        self.__rate_window.exec()

    @Slot()
    def open_character(self):
        character = self.__catalog.get_character(
            self.__related_characters[
                self.ui.characters_list.currentIndex().row()
            ],
        )
        self.__character_window = FormCharacter(
            character,
            self.__manga.catalog_id,
            parent=self,
        )
        self.__character_window.show()

    def update_manga_preview(self):
        self.ui.image.clear()
        if not self.__manga_pixmap:
            self.__manga_pixmap = FileManager.get_manga_preview(
                self.__manga,
                self.__catalog,
            )
        image_size = QSize(self.width() // 5, self.height() // 2)
        pixmap = self.__manga_pixmap.scaled(
            image_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.ui.image_frame.setFixedWidth(pixmap.width())
        self.ui.image.setPixmap(pixmap)

    def set_info(self):
        self.ui.name_label.setText(self.__manga.name)
        self.ui.russian_label.setText(self.__manga.russian)
        self.ui.status_label.setVisible(bool(self.__manga.status))
        self.ui.status_label.setText(
            f"{translate('Other', 'Status')}: "
            f"{translate('Status', self.__manga.status.to_str())}",
        )
        self.ui.volumes_label.setVisible(bool(self.__manga.volumes))
        self.ui.chapters_label.setVisible(bool(self.__manga.chapters))
        self.ui.volumes_label.setText(
            f"{translate('Other', 'Volumes')}: {self.__manga.volumes}",
        )
        self.ui.chapters_label.setText(
            f"{translate('Other', 'Chapters')}: {self.__manga.chapters}",
        )
        self.ui.catalog_score_label.setVisible(bool(self.__manga.score))
        self.ui.catalog_score_label.setText(
            f"{translate('Other', 'Rating')}: {self.__manga.score}",
        )
        # self.ui.description_frame.setVisible(bool(self.__manga.get_description()))
        self.ui.description_text.setHtml(
            description_to_html(self.__manga.get_description()),
        )

    @Slot()
    def add_to_favorites(self):
        if self.__db.check_manga_library(self.__manga):
            self.__db.rem_manga_library(self.__manga)
        else:
            lib_list = Nl.LibList(self.ui.lib_list_box.currentIndex())
            self.__db.add_manga_library(self.__manga, lib_list)
        self.update_add_button_icon()

    @Slot()
    def change_lib_list(self):
        if self.__db.check_manga_library(self.__manga):
            lib_list = Nl.LibList(self.ui.lib_list_box.currentIndex())
            self.__db.add_manga_library(self.__manga, lib_list)

    def get_chapters(self):
        self.__chapters = self.__catalog.get_chapters(self.__manga)
        self.__chapters.reverse()
        self.sort_chapters()
        self.__db.add_chapters(self.__chapters, self.__manga)

    def update_chapters(self):
        self.ui.items_tree.clear()
        self.ui.items_frame.setVisible(bool(self.__chapters))
        for lang, translators in self.__sorted_chapters.items():
            lang_item = QTreeWidgetItem(
                [translate("NlLanguage", lang.to_str())],
            )
            lang_item.setIcon(0, QIcon(get_language_icon(lang)))
            self.ui.items_tree.addTopLevelItem(lang_item)

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
                            ch_item.setIcon(0, ItemsIcons.UNREAD)
                    translator_item.addChild(ch_item)

            if len(self.__sorted_chapters) == 1:
                lang_item.setExpanded(True)

    def get_relations(self):
        self.__related_mangas = self.__catalog.get_relations(self.__manga)

    def update_relations(self):
        self.ui.related_list.clear()
        self.ui.related_frame.setVisible(bool(self.__related_mangas))
        for manga in self.__related_mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.related_list.addItem(item)

    def get_characters(self):
        self.__related_characters = self.__catalog.get_characters(self.__manga)

    def update_characters(self):
        self.ui.characters_list.clear()
        self.ui.characters_frame.setVisible(bool(self.__related_characters))
        for character in self.__related_characters:
            item = QListWidgetItem(character.get_name())
            self.ui.characters_list.addItem(item)

    @Slot()
    def open_reader(self):
        try:
            if self.__reader_window is not None:
                self.__reader_window.close()
        except RuntimeError:
            pass
        finally:
            selected_chapter = self._get_selected_chapter()
            if selected_chapter:
                if hasattr(selected_chapter, "url"):
                    start_html_video(self.__manga, selected_chapter)
                    return
                self.__reader_window = ReaderWindow()
                self.__reader_window.setup(
                    self.__manga,
                    self.__chapters,
                    self.__chapters.index(selected_chapter) + 1,
                )

    @Slot()
    def open_related_manga(self):
        self.opened_related_manga.emit(self.get_selected_related_title())
