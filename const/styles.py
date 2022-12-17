import os
import sys


def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__name__)))
    return os.path.join(base_path, relative_path)


dark_style = get_resource_path("data/styles/dark/widget_dark.qss")
light_style = get_resource_path("data/styles/light/widget_light.qss")
