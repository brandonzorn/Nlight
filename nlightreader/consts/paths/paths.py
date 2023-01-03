import os
import sys

from nlightreader.consts.app import APP_NAME

TOKEN_PATH = f'{APP_NAME}/tokens'


def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__name__)))
    return os.path.join(base_path, relative_path)
