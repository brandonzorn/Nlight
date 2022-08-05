import os
import sys


def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__name__)))
    return os.path.join(base_path, relative_path)


app_icon_path = get_resource_path("images/icon.png")

favorite_icon_path = get_resource_path("images/favorite.png")
favorite1_icon_path = get_resource_path("images/favorite1.png")
favorite2_icon_path = get_resource_path("images/favorite2.png")

gb_icon_path = get_resource_path("images/gb.svg")
ru_icon_path = get_resource_path("images/ru.svg")
jp_icon_path = get_resource_path("images/jp.svg")
