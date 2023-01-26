from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtWidgets import QWidget
from data.ui.manga_item import Ui_Form
from nlightreader.items import Manga
from nlightreader.utils import Worker, get_catalog, get_manga_preview


class Signals(QObject):
    manga_clicked = Signal(Manga)


class MangaItem(QWidget):
    def __init__(self, manga: Manga):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setStyleSheet(
            "QPushButton{padding: 0px;background-color: rgb(0, 133, 52, 255);"
            "border-radius: 0px;font-weight: bold;color: rgb(255, 255, 255, 255);}")
        self.ui.pushButton.setMaximumSize(128, 228)
        self.manga = manga
        self.manga_pixmap = None
        self.signals = Signals()
        self.ui.pushButton.clicked.connect(lambda: self.signals.manga_clicked.emit(self.manga))
        self.set_image()

    def resizeEvent(self, event):
        self.ui.pushButton.setMaximumSize(self.ui.frame.size())
        self.update_image()

    def update_image(self):
        if self.manga_pixmap:
            pixmap = self.manga_pixmap.scaled(self.ui.pushButton.maximumSize(), Qt.AspectRatioMode.KeepAspectRatio,
                                              Qt.TransformationMode.SmoothTransformation)
            self.ui.pushButton.setIcon(pixmap)
            self.ui.pushButton.setIconSize(pixmap.size())

    def set_image(self):
        self.ui.name_lbl.setText(self.manga.name)
        self.ui.sub_name_lbl.setText(self.manga.get_name())

        def get_image():
            catalog = get_catalog(self.manga.catalog_id)()
            self.manga_pixmap = get_manga_preview(self.manga, catalog)

        Worker(target=get_image, callback=self.update_image).start()
