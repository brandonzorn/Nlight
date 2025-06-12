from PySide6.QtWidgets import QGridLayout
from qfluentwidgets import CheckBox, MessageBoxBase, SubtitleLabel

from nlightreader.models import Genre


class GenresDialogUi(MessageBoxBase):
    def __init__(self, genres: dict[Genre, bool], parent=None):
        super().__init__(parent)
        self.genres_items = {}
        self.max_genres_per_row = 5

        self.title_label = SubtitleLabel(self.tr("Genres"), parent=self)
        self.genres_layout = QGridLayout()
        self._populate_genres(genres)

        self.viewLayout.addWidget(self.title_label)
        self.viewLayout.addLayout(self.genres_layout)

    def get_selected_genres(self):
        return [
            genre
            for checkbox, genre in self.genres_items.items()
            if checkbox.isChecked()
        ]

    def _populate_genres(self, genres: dict[Genre, bool]):
        for index, (genre, selected) in enumerate(genres.items()):
            checkbox = CheckBox(genre.get_name())
            checkbox.setChecked(selected)
            self.genres_items[checkbox] = genre
            row, col = divmod(index, self.max_genres_per_row)
            self.genres_layout.addWidget(checkbox, row, col)


class GenresDialog:
    def __init__(self, parent):
        self.parent = parent
        self.genres: dict[Genre, bool] = {}

    def set_genres(self, genres: list[Genre]):
        self.genres = {genre: False for genre in genres}

    @property
    def selected_genres(self):
        return [genre for genre, selected in self.genres.items() if selected]

    def show(self):
        w = GenresDialogUi(self.genres, parent=self.parent)
        if w.exec():
            for genre in w.get_selected_genres():
                self.genres[genre] = True

    def reset_items(self):
        for genre in self.genres:
            self.genres[genre] = False

    def clear(self):
        self.genres.clear()


__all__ = [
    "GenresDialog",
]
