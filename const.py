import os
from pathlib import Path

URL = 'https://desu.me'
URL_API = 'https://desu.me/manga/api'
HEADERS = {'User-Agent': 'Desu'}


lib_lists_en = ['planned', 'completed', 'watching', 'rewatching', 'on_hold',  'dropped']
lib_lists_ru = ['запланированно', 'прочитано', 'читаю', 'перечитываю', 'отложено', 'брошено']


app_icon_path = os.path.join(Path(__file__).parent, "images/icon.png")
library_icon_path = os.path.join(Path(__file__).parent, "images/library.png")
main_icon_path = os.path.join(Path(__file__).parent, "images/main.png")
back_icon_path = os.path.join(Path(__file__).parent, "images/back.png")
favorite_icon_path = os.path.join(Path(__file__).parent, "images/favorite.png")
favorite1_icon_path = os.path.join(Path(__file__).parent, "images/favorite1.png")
favorite2_icon_path = os.path.join(Path(__file__).parent, "images/favorite2.png")
