from PySide6.QtWidgets import QGridLayout, QWidget
from qfluentwidgets import CheckBox, MessageBoxBase, SubtitleLabel

from nlightreader.models import Genre


class GenresDialogUi(MessageBoxBase):
    MAX_GENRES_PER_ROW = 5

    def __init__(
        self,
        genres: dict[Genre, bool],
        parent: QWidget,
    ) -> None:
        super().__init__(parent)
        self._setup_ui()

        self._checkboxes: dict[Genre, CheckBox] = {}
        self._populate_genres(genres)

    def _setup_ui(self) -> None:
        self._title_label = SubtitleLabel(self.tr("Genres"), self)
        self.viewLayout.addWidget(self._title_label)
        self._genres_layout = QGridLayout()
        self.viewLayout.addLayout(self._genres_layout)

    @property
    def selected_genres(self) -> set[Genre]:
        return {
            genre
            for genre, checkbox in self._checkboxes.items()
            if checkbox.isChecked()
        }

    def _populate_genres(self, genres: dict[Genre, bool]) -> None:
        for index, (genre, checked) in enumerate(genres.items()):
            checkbox = CheckBox(genre.get_name(), self)
            checkbox.setChecked(checked)
            self._checkboxes[genre] = checkbox
            row, column = divmod(index, self.MAX_GENRES_PER_ROW)
            self._genres_layout.addWidget(checkbox, row, column)


class GenresDialog:
    def __init__(self, parent: QWidget) -> None:
        self._parent = parent
        self._genres: dict[Genre, bool] = {}

    def exec(self) -> bool:
        w = GenresDialogUi(self._genres, parent=self._parent)
        if not w.exec():
            return False
        for genre in self._genres:
            self._genres[genre] = genre in w.selected_genres
        return True

    @property
    def selected_genres(self) -> set[Genre]:
        return {genre for genre, selected in self._genres.items() if selected}

    def set_genres(self, genres: list[Genre]) -> None:
        self._genres = {genre: False for genre in genres}

    def reset_items(self) -> None:
        self._genres = dict.fromkeys(self._genres, False)

    def clear(self) -> None:
        self._genres.clear()


__all__ = ["GenresDialog"]
