from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from const import app_icon_path
from desu_genresUI import Ui_Dialog


class FormGenres(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_ge = Ui_Dialog()
        self.ui_ge.setupUi(self)
        self.setFixedSize(self.minimumSize())
        self.setWindowTitle('Genres')
        self.setWindowIcon(QIcon(app_icon_path))
        self.ui_ge.buttonBox.accepted.connect(self.accept_genres)
        self.ui_ge.buttonBox.rejected.connect(self.reject_genres)
        self.selected_genres = {'genres': ''}
        self.genres = {self.ui_ge.g_dementia: 'Dementia', self.ui_ge.g_martialarts: 'Martial Arts',
                       self.ui_ge.g_color: 'Color', self.ui_ge.g_vampire: 'Vampire', self.ui_ge.g_web: 'Web',
                       self.ui_ge.g_harem: 'Harem', self.ui_ge.g_heroicfantasy: 'Heroic Fantasy',
                       self.ui_ge.g_demons: 'Demons', self.ui_ge.g_mystery: 'Mystery', self.ui_ge.g_josei: 'Josei',
                       self.ui_ge.g_drama: 'Drama', self.ui_ge.g_yonkoma: 'Yonkoma', self.ui_ge.g_game: 'Game',
                       self.ui_ge.g_isekai: 'Isekai', self.ui_ge.g_historical: 'Historical',
                       self.ui_ge.g_comedy: 'Comedy', self.ui_ge.g_space: 'Space', self.ui_ge.g_litrpg: 'LitRPG',
                       self.ui_ge.g_magic: 'Magic', self.ui_ge.g_mecha: 'Mecha', self.ui_ge.g_mystic: 'Mystic',
                       self.ui_ge.g_music: 'Music', self.ui_ge.g_scifi: 'Sci-Fi', self.ui_ge.g_parody: 'Parody',
                       self.ui_ge.g_sliceoflife: 'Slice of Life', self.ui_ge.g_postapocalyptic: 'Post Apocalyptic',
                       self.ui_ge.g_adventure: 'Adventure', self.ui_ge.g_psychological: 'Psychological',
                       self.ui_ge.g_romance: 'Romance', self.ui_ge.g_samurai: 'Samurai',
                       self.ui_ge.g_supernatural: 'Supernatural', self.ui_ge.g_shoujo: 'Shoujo',
                       self.ui_ge.g_shoujoai: 'Shoujo Ai', self.ui_ge.g_seinen: 'Seinen',
                       self.ui_ge.g_shounen: 'Shounen', self.ui_ge.g_shounenai: 'Shounen Ai',
                       self.ui_ge.g_genderbender: 'Gender Bender', self.ui_ge.g_sports: 'Sports',
                       self.ui_ge.g_superpower: 'Super Power', self.ui_ge.g_tragedy: 'Tragedy',
                       self.ui_ge.g_thriller: 'Thriller', self.ui_ge.g_horror: 'Horror',
                       self.ui_ge.g_fiction: 'Fiction', self.ui_ge.g_fantasy: 'Fantasy', self.ui_ge.g_hentai: 'Hentai',
                       self.ui_ge.g_school: 'School', self.ui_ge.g_action: 'Action', self.ui_ge.g_ecchi: 'Ecchi',
                       self.ui_ge.g_yuri: 'Yuri', self.ui_ge.g_yaoi: 'Yaoi'}

    def accept_genres(self):
        genres = [self.genres.get(i) for i in self.genres if i.isChecked()]
        self.selected_genres = {'genres': ','.join(genres)}

    def reject_genres(self):
        for i in self.genres:
            if self.genres.get(i) not in self.selected_genres.get('genres'):
                i.setChecked(False)
            else:
                i.setChecked(True)

    def clear_genres(self):
        [i.setChecked(False) for i in self.genres]
        self.accept_genres()
