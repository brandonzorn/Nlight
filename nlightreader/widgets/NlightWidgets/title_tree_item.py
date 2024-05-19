from PySide6.QtWidgets import QTreeWidgetItem

from nlightreader.items import Chapter


class ChapterTreeItem(QTreeWidgetItem):
    def __init__(self, chapter: Chapter):
        super().__init__([chapter.get_name()])
        self.chapter = chapter
