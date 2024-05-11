import logging

from PySide6.QtCore import Qt, QSize, Slot, Signal, QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QListWidgetItem, QTreeWidgetItem
from qfluentwidgets import FluentIcon

from data.ui.widgets.info import Ui_Form
from nlightreader.consts.enums import Nl, LIB_LISTS
from nlightreader.consts.files import NlFluentIcons
from nlightreader.contexts import ReadMarkMenu
from nlightreader.dialogs import FormRate, FormCharacter
from nlightreader.items import Manga, Character, Chapter, HistoryNote
from nlightreader.utils import (
    Database,
    FileManager,
    get_catalog,
    get_status,
    get_language_icon,
    translate,
    Worker,
    description_to_html,
)
from nlightreader.utils.html_video import start_html_video
from nlightreader.windows.Reader import ReaderWindow


class FormInfo(QWidget):
    opened_related_manga = Signal(Manga)
    setup_done = Signal()
    setup_error = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.shikimori_btn.setIcon(NlFluentIcons.SHIKIMORI.qicon())

        self.setObjectName("FormInfo")

        self.ui.lib_list_box.addItems([translate("Form", i.capitalize()) for i in LIB_LISTS])
        self.ui.items_tree.doubleClicked.connect(self.open_reader)
        self.ui.characters_list.doubleClicked.connect(self.open_character)
        self.ui.related_list.doubleClicked.connect(self.open_related_manga)
        self.ui.shikimori_btn.clicked.connect(self.open_rate)
        self.ui.add_btn.clicked.connect(self.add_to_favorites)
        self.ui.lib_list_box.currentIndexChanged.connect(self.change_lib_list)
        self.ui.items_tree.customContextMenuRequested.connect(self.on_context_menu)

        self.ui.scrollArea.resizeEvent = self.scroll_area_resize_event

        self.db: Database = Database()
        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(3)
        self.catalog = None
        self.manga = None
        self.related_mangas: list[Manga] = []
        self.related_characters: list[Character] = []
        self.chapters: list[Chapter] = []
        self.sorted_chapters = {}
        self.manga_pixmap = None
        self.reader_window = None
        self.rate_window = None
        self.character_window = None

    def on_context_menu(self, pos):
        context_target = self.ui.items_tree

        def set_as_read_all():
            history_notes = []
            for i in range(selected_item.parent().indexOfChild(selected_item) + 1):
                chapter = self.sorted_chapters[list(self.sorted_chapters.keys())[top_item_id]][i]
                history_notes.append(HistoryNote(chapter, self.manga, True))
                item = selected_item.parent().child(i)
                item.setIcon(0, FluentIcon.ACCEPT_MEDIUM.qicon())
            self.db.add_history_notes(history_notes)

        def set_as_read():
            self.db.add_history_note(HistoryNote(selected_chapter, self.manga, True))
            selected_item.setIcon(0, FluentIcon.ACCEPT_MEDIUM.qicon())

        def remove_read_state():
            self.db.del_history_note(selected_chapter)
            selected_item.setIcon(0, QIcon())

        menu = ReadMarkMenu()
        selected_item = context_target.itemAt(pos)
        if not selected_item or not selected_item.parent():
            return
        top_item_id = self.ui.items_tree.indexOfTopLevelItem(selected_item.parent())
        selected_chapter = self.sorted_chapters[list(self.sorted_chapters.keys())[top_item_id]][
            selected_item.parent().indexOfChild(selected_item)
        ]
        if not self.db.check_complete_chapter(selected_chapter):
            menu.set_mode(0)
        else:
            if self.db.get_complete_status(selected_chapter):
                menu.set_mode(1)
            else:
                menu.set_mode(2)
        menu.set_as_read.triggered.connect(set_as_read)
        menu.set_as_read_all.triggered.connect(set_as_read_all)
        menu.remove_read_state.triggered.connect(remove_read_state)
        menu.exec(context_target.mapToGlobal(pos))

    def resizeEvent(self, event):
        if not self.catalog or not self.manga or not self.manga_pixmap:
            return
        self.update_manga_preview()

    def scroll_area_resize_event(self, event):
        self.ui.scrollAreaWidgetContents.setFixedWidth(event.size().width())

    def sort_chapters(self):
        self.sorted_chapters.clear()
        for ch in self.chapters:
            if ch.language in self.sorted_chapters:
                self.sorted_chapters[ch.language].append(ch)
            else:
                self.sorted_chapters.update({ch.language: [ch]})

    def _get_selected_chapter(self) -> Chapter | None:
        selected_item = self.ui.items_tree.currentItem()
        if not selected_item.parent():
            return
        top_item_id = self.ui.items_tree.indexOfTopLevelItem(selected_item.parent())
        return self.sorted_chapters[list(self.sorted_chapters.keys())[top_item_id]][
            selected_item.parent().indexOfChild(selected_item)
        ]

    def get_current_manga(self):
        return self.catalog.get_manga(self.related_mangas[self.ui.related_list.currentIndex().row()])

    def setup(self, manga):
        def info_setup():
            try:
                self.catalog = get_catalog(manga.catalog_id)()
                self.manga = self.catalog.get_manga(manga)
                self.db.add_manga(self.manga)
            except Exception as e:
                logging.error(e)
                self.setup_error.emit()

        Worker(target=info_setup, callback=self.update_additional_info).start(pool=self.thread_pool)

    def update_add_button_icon(self):
        if self.ui.add_btn.isChecked():
            self.ui.add_btn.setIcon(FluentIcon.REMOVE_FROM)
        else:
            self.ui.add_btn.setIcon(FluentIcon.ADD_TO)

    def update_additional_info(self):
        self.ui.lib_frame.setVisible(not self.catalog.is_primary)
        self.ui.shikimori_frame.setVisible(self.catalog.is_primary)
        self.set_info()
        if self.db.check_manga_library(self.manga):
            self.ui.lib_list_box.setCurrentIndex(self.db.get_manga_library_list(self.manga).value)
            self.ui.add_btn.setChecked(True)
        else:
            self.ui.add_btn.setChecked(False)
        self.update_add_button_icon()
        self.update_manga_preview()
        Worker(target=self.get_chapters, callback=self.update_chapters).start(pool=self.thread_pool)
        Worker(target=self.get_relations, callback=self.update_relations).start(pool=self.thread_pool)
        Worker(target=self.get_characters, callback=self.update_characters).start(pool=self.thread_pool)
        self.setup_done.emit()

    @Slot()
    def open_rate(self):
        self.rate_window = FormRate(self.manga, parent=self)
        self.rate_window.exec()

    @Slot()
    def open_character(self):
        character = self.catalog.get_character(self.related_characters[self.ui.characters_list.currentIndex().row()])
        self.character_window = FormCharacter(character, self.manga.catalog_id, parent=self)
        self.character_window.show()

    def update_manga_preview(self):
        self.ui.image.clear()
        if not self.manga_pixmap:
            self.manga_pixmap = FileManager.get_manga_preview(self.manga, self.catalog)
        image_size = QSize(self.width() // 5, self.height() // 2)
        pixmap = self.manga_pixmap.scaled(
            image_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.ui.image_frame.setFixedWidth(pixmap.width())
        self.ui.image.setPixmap(pixmap)

    def set_info(self):
        self.ui.name_label.setText(self.manga.name)
        self.ui.russian_label.setText(self.manga.russian)
        self.ui.status_label.setVisible(bool(self.manga.status))
        self.ui.status_label.setText(f"{translate('Other', 'Status')}: {get_status(self.manga.status)}")
        self.ui.volumes_label.setVisible(bool(self.manga.volumes))
        self.ui.chapters_label.setVisible(bool(self.manga.chapters))
        self.ui.volumes_label.setText(f"{translate('Other', 'Volumes')}: {self.manga.volumes}")
        self.ui.chapters_label.setText(f"{translate('Other', 'Chapters')}: {self.manga.chapters}")
        self.ui.catalog_score_label.setVisible(bool(self.manga.score))
        self.ui.catalog_score_label.setText(f"{translate('Other', 'Rating')}: {self.manga.score}")
        # self.ui.description_frame.setVisible(bool(self.manga.get_description()))
        self.ui.description_text.setHtml(description_to_html(self.manga.get_description()))

    @Slot()
    def add_to_favorites(self):
        if self.db.check_manga_library(self.manga):
            self.db.rem_manga_library(self.manga)
        else:
            lib_list = Nl.LibList(self.ui.lib_list_box.currentIndex())
            self.db.add_manga_library(self.manga, lib_list)
        self.update_add_button_icon()

    @Slot()
    def change_lib_list(self):
        if self.db.check_manga_library(self.manga):
            lib_list = Nl.LibList(self.ui.lib_list_box.currentIndex())
            self.db.add_manga_library(self.manga, lib_list)

    def get_chapters(self):
        self.chapters = self.catalog.get_chapters(self.manga)
        self.chapters.reverse()
        self.sort_chapters()
        self.db.add_chapters(self.chapters, self.manga)

    def update_chapters(self):
        self.ui.items_tree.clear()
        self.ui.items_frame.setVisible(bool(self.chapters))
        for lang in self.sorted_chapters:
            lang_item = QTreeWidgetItem([translate("NlLanguage", lang.to_full_str())])
            lang_item.setIcon(0, QIcon(get_language_icon(lang)))
            self.ui.items_tree.addTopLevelItem(lang_item)
            for chapter in self.sorted_chapters[lang]:
                ch_item = QTreeWidgetItem([chapter.get_name()])
                if self.db.check_complete_chapter(chapter):
                    if self.db.get_complete_status(chapter):
                        ch_item.setIcon(0, FluentIcon.ACCEPT_MEDIUM.qicon())
                lang_item.addChild(ch_item)
            if len(self.sorted_chapters) == 1:
                lang_item.setExpanded(True)

    def get_relations(self):
        self.related_mangas = self.catalog.get_relations(self.manga)

    def update_relations(self):
        self.ui.related_list.clear()
        self.ui.related_frame.setVisible(bool(self.related_mangas))
        for manga in self.related_mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.related_list.addItem(item)

    def get_characters(self):
        self.related_characters = self.catalog.get_characters(self.manga)

    def update_characters(self):
        self.ui.characters_list.clear()
        self.ui.characters_frame.setVisible(bool(self.related_characters))
        for character in self.related_characters:
            item = QListWidgetItem(character.get_name())
            self.ui.characters_list.addItem(item)

    @Slot()
    def open_reader(self):
        try:
            if self.reader_window is not None:
                self.reader_window.close()
        except RuntimeError:
            pass
        finally:
            selected_chapter = self._get_selected_chapter()
            if selected_chapter:
                if hasattr(selected_chapter, "url"):
                    start_html_video(self.manga, selected_chapter)
                    return
                self.reader_window = ReaderWindow()
                self.reader_window.setup(
                    self.manga,
                    self.chapters,
                    self.chapters.index(selected_chapter) + 1,
                )

    @Slot()
    def open_related_manga(self):
        self.opened_related_manga.emit(self.get_current_manga())
