import os
import sys


def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__name__)))
    return os.path.join(base_path, relative_path)


app_icon_path = get_resource_path("images/icon.png")

main_icon_path = get_resource_path("images/main.png")
shikimori_icon_path = get_resource_path("images/shikimori.png")
library_icon_path = get_resource_path("images/library.png")
history_icon_path = get_resource_path("images/history.png")

search_icon_path = get_resource_path("images/search.png")
delete_icon_path = get_resource_path("images/delete.png")
back_icon_path = get_resource_path("images/back.png")
fullscreen_icon_path = get_resource_path("images/fullscreen.png")
settings_icon_path = get_resource_path("images/settings.png")

favorite_icon_path = get_resource_path("images/favorite.png")
favorite1_icon_path = get_resource_path("images/favorite1.png")
favorite2_icon_path = get_resource_path("images/favorite2.png")

prev_page_icon_path = get_resource_path("images/prev.png")
next_page_icon_path = get_resource_path("images/next.png")
prev_ch_icon_path = get_resource_path("images/double_prev.png")
next_ch_icon_path = get_resource_path("images/double_next.png")

gb_icon_path = get_resource_path("images/gb.svg")
ru_icon_path = get_resource_path("images/ru.svg")
jp_icon_path = get_resource_path("images/jp.svg")
