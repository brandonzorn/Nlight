import os
from enum import Enum
from pathlib import Path

URL_DESU = 'https://desu.me'
URL_DESU_API = 'https://desu.me/manga/api'
URL_SHIKIMORI = 'https://shikimori.one'
URL_SHIKIMORI_API = 'https://shikimori.one/api'
URL_SHIKIMORI_TOKEN = 'https://shikimori.one/oauth/token'
URL_MANGA_DEX = 'https://mangadex.org'
URL_MANGA_DEX_API = 'https://api.mangadex.org'
URL_RULATE = 'https://tl.rulate.ru'


DESU_HEADERS = {'User-Agent': 'Desu'}
SHIKIMORI_HEADERS = {'User-Agent': 'Shikimori'}
MANGA_DEX_HEADERS = {'User-Agent': 'Shikimori'}
DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}

lib_lists_en = ('planned', 'completed', 'watching', 'rewatching', 'on_hold', 'dropped')
lib_lists_ru = ('запланированно', 'прочитано', 'читаю', 'перечитываю', 'отложено', 'брошено')


app_icon_path = os.path.join(Path(__file__).parent, "images/icon.png")

main_icon_path = os.path.join(Path(__file__).parent, "images/main.png")
shikimori_icon_path = os.path.join(Path(__file__).parent, "images/shikimori.png")
library_icon_path = os.path.join(Path(__file__).parent, "images/library.png")
history_icon_path = os.path.join(Path(__file__).parent, "images/history.png")

search_icon_path = os.path.join(Path(__file__).parent, "images/search.png")
delete_icon_path = os.path.join(Path(__file__).parent, "images/delete.png")
back_icon_path = os.path.join(Path(__file__).parent, "images/back.png")
fullscreen_icon_path = os.path.join(Path(__file__).parent, "images/fullscreen.png")

favorite_icon_path = os.path.join(Path(__file__).parent, "images/favorite.png")
favorite1_icon_path = os.path.join(Path(__file__).parent, "images/favorite1.png")
favorite2_icon_path = os.path.join(Path(__file__).parent, "images/favorite2.png")

prev_page_icon_path = os.path.join(Path(__file__).parent, "images/prev.png")
next_page_icon_path = os.path.join(Path(__file__).parent, "images/next.png")
prev_ch_icon_path = os.path.join(Path(__file__).parent, "images/double_prev.png")
next_ch_icon_path = os.path.join(Path(__file__).parent, "images/double_next.png")

gb_icon_path = os.path.join(Path(__file__).parent, "images/gb.svg")
ru_icon_path = os.path.join(Path(__file__).parent, "images/ru.svg")
jp_icon_path = os.path.join(Path(__file__).parent, "images/jp.svg")


manga_desu_genres = ({'en': 'Dementia', 'ru': 'Безумие'}, {'en': 'Martial Arts', 'ru': 'Боевые искусства'},
                     {'en': 'Color', 'ru': 'В цвете'}, {'en': 'Vampire', 'ru': 'Вампиры'}, {'en': 'Web', 'ru': 'Веб'},
                     {'en': 'Harem', 'ru': 'Гарем'}, {'en': 'Heroic Fantasy', 'ru': 'Героическое фэнтези'},
                     {'en': 'Demons', 'ru': 'Демоны'}, {'en': 'Mystery', 'ru': 'Детектив'},
                     {'en': 'Josei', 'ru': 'Дзёсей'}, {'en': 'Drama', 'ru': 'Драма'}, {'en': 'Yonkoma', 'ru': 'Ёнкома'},
                     {'en': 'Game', 'ru': 'Игры'}, {'en': 'Isekai', 'ru': 'Исекай'},
                     {'en': 'Historical', 'ru': 'Исторический'}, {'en': 'Comedy', 'ru': 'Комедия'},
                     {'en': 'Space', 'ru': 'Космос'}, {'en': 'LitRPG', 'ru': 'ЛитRPG'}, {'en': 'Magic', 'ru': 'Магия'},
                     {'en': 'Mecha', 'ru': 'Меха'}, {'en': 'Mystic', 'ru': 'Мистика'}, {'en': 'Music', 'ru': 'Музыка'},
                     {'en': 'Sci-Fi', 'ru': 'Научная фантастика'}, {'en': 'Parody', 'ru': 'Пародия'},
                     {'en': 'Slice of Life', 'ru': 'Повседневность'},
                     {'en': 'Post Apocalyptic', 'ru': 'Постапокалиптика'}, {'en': 'Adventure', 'ru': 'Приключения'},
                     {'en': 'Psychological', 'ru': 'Психологическое'}, {'en': 'Romance', 'ru': 'Романтика'},
                     {'en': 'Samurai', 'ru': 'Самураи'}, {'en': 'Supernatural', 'ru': 'Сверхъестественное'},
                     {'en': 'Shoujo', 'ru': 'Сёдзе'}, {'en': 'Shoujo Ai', 'ru': 'Сёдзе Ай'},
                     {'en': 'Seinen', 'ru': 'Сейнен'}, {'en': 'Shounen', 'ru': 'Сёнен'},
                     {'en': 'Shounen Ai', 'ru': 'Сёнен Ай'}, {'en': 'Gender Bender', 'ru': 'Смена пола'},
                     {'en': 'Sports', 'ru': 'Спорт'}, {'en': 'Super Power', 'ru': 'Супер сила'},
                     {'en': 'Tragedy', 'ru': 'Трагедия'}, {'en': 'Thriller', 'ru': 'Триллер'},
                     {'en': 'Horror', 'ru': 'Ужасы'}, {'en': 'Fiction', 'ru': 'Фантастика'},
                     {'en': 'Fantasy', 'ru': 'Фэнтези'}, {'en': 'Hentai', 'ru': 'Хентай'},
                     {'en': 'School', 'ru': 'Школа'}, {'en': 'Action', 'ru': 'Экшен'}, {'en': 'Ecchi', 'ru': 'Этти'},
                     {'en': 'Yuri', 'ru': 'Юри'}, {'en': 'Yaoi', 'ru': 'Яой'})


manga_desu_orders = ({'en': 'name', 'ru': 'Название'}, {'en': 'popular', 'ru': 'Популярность'})

manga_desu_kinds = ({'en': 'manga', 'ru': 'Манга'}, {'en': 'manhwa', 'ru': 'Манхва'}, {'en': 'manhua', 'ru': 'Маньхуа'},
                    {'en': 'one_shot', 'ru': 'Ваншот'}, {'en': 'comics', 'ru': 'Комикс'})


class LibraryLists(Enum):
    lib_lists_ru = ('запланированно', 'прочитано', 'читаю', 'перечитываю', 'отложено', 'брошено')
    PLANNED = 'planned'
    COMPLETED = 'completed'
    WATCHING = 'watching'
    REWATCHING = 'rewatching'
    ON_HOLD = 'on_hold'
    DROPPED = 'dropped'
