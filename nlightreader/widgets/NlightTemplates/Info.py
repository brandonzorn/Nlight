from PySide6.QtCore import Qt, QSize, Slot, Signal, QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QListWidgetItem, QTreeWidgetItem
from qfluentwidgets import FluentIcon

from data.ui.widgets.info import Ui_Form
from nlightreader.consts import lib_lists_en, ItemsColors, Nl
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
from nlightreader.windows.Reader import ReaderWindow


class FormInfo(QWidget):
    opened_related_manga = Signal(Manga)
    setup_done = Signal()
    setup_error = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.shikimori_btn.setIcon(QIcon(":/actions_black/data/icons/buttons/svg_24dp_black/actions/shikimori.svg"))

        self.setObjectName("FormInfo")

        self.ui.lib_list_box.addItems([translate("Form", i.capitalize()) for i in lib_lists_en])
        self.ui.items_tree.doubleClicked.connect(self.open_reader)
        self.ui.characters_list.doubleClicked.connect(self.open_character)
        self.ui.related_list.doubleClicked.connect(self.open_related_manga)
        self.ui.shikimori_btn.clicked.connect(self.open_rate)
        self.ui.add_btn.clicked.connect(self.add_to_favorites)
        self.ui.lib_list_box.currentIndexChanged.connect(self.change_lib_list)
        self.ui.items_tree.customContextMenuRequested.connect(self.on_context_menu)
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
                chapter = self.sorted_chapters[selected_item.parent().text(0)][i]
                history_notes.append(HistoryNote(chapter, self.manga, True))
                item = selected_item.parent().child(i)
                item.setBackground(0, ItemsColors.READ)
            self.db.add_history_notes(history_notes)

        def set_as_read():
            self.db.add_history_note(HistoryNote(selected_chapter, self.manga, True))
            selected_item.setBackground(0, ItemsColors.READ)

        def remove_read_state():
            self.db.del_history_note(selected_chapter)
            selected_item.setBackground(0, ItemsColors.EMPTY)

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

    def resizeEvent(self, a0):
        if not self.catalog or not self.manga or not self.manga_pixmap:
            return
        self.update_manga_preview()

    def sort_chapters(self):
        self.sorted_chapters.clear()
        for ch in self.chapters:
            if ch.language in self.sorted_chapters:
                self.sorted_chapters[ch.language].append(ch)
            else:
                self.sorted_chapters.update({ch.language: [ch]})

    def _get_selected_chapter(self):
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
                print(e)
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
        self.get_chapters()
        self.get_characters()
        self.get_relations()
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
        def get_chapters():
            self.chapters = self.catalog.get_chapters(self.manga)
            self.chapters.reverse()
            self.chapters.sort(key=lambda ch: ch.language.value if ch.language.value else False)
            self.db.add_chapters(self.chapters, self.manga)

        def update_chapters():
            self.ui.items_tree.clear()
            self.ui.items_frame.setVisible(bool(self.chapters))
            self.sort_chapters()
            for lang in self.sorted_chapters:
                lang_item = QTreeWidgetItem([translate("NlLanguage", lang.to_full_str())])
                lang_item.setIcon(0, QIcon(get_language_icon(lang)))
                self.ui.items_tree.addTopLevelItem(lang_item)
                for chapter in self.sorted_chapters[lang]:
                    ch_item = QTreeWidgetItem([chapter.get_name()])
                    if self.db.check_complete_chapter(chapter):
                        if self.db.get_complete_status(chapter):
                            ch_item.setBackground(0, ItemsColors.READ)
                        else:
                            ch_item.setBackground(0, ItemsColors.UNREAD)
                    lang_item.addChild(ch_item)
                if len(self.sorted_chapters) == 1:
                    lang_item.setExpanded(True)

        Worker(target=get_chapters, callback=update_chapters).start(pool=self.thread_pool)

    def get_relations(self):
        def get_relations():
            self.related_mangas = self.catalog.get_relations(self.manga)

        def update_relations():
            self.ui.related_list.clear()
            self.ui.related_frame.setVisible(bool(self.related_mangas))
            for manga in self.related_mangas:
                item = QListWidgetItem(manga.get_name())
                self.ui.related_list.addItem(item)

        Worker(target=get_relations, callback=update_relations).start(pool=self.thread_pool)

    def get_characters(self):
        def get_characters():
            self.related_characters = self.catalog.get_characters(self.manga)

        def update_characters():
            self.ui.characters_list.clear()
            self.ui.characters_frame.setVisible(bool(self.related_characters))
            for character in self.related_characters:
                item = QListWidgetItem(character.get_name())
                self.ui.characters_list.addItem(item)

        Worker(target=get_characters, callback=update_characters).start(pool=self.thread_pool)

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
                self.reader_window = ReaderWindow()
                self.reader_window.setup(self.manga, self.chapters, self.chapters.index(selected_chapter) + 1)

    @Slot()
    def open_related_manga(self):
        self.opened_related_manga.emit(self.get_current_manga())
