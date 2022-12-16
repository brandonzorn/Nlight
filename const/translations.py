import os
import sys


def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__name__)))
    return os.path.join(base_path, relative_path)


en_trans_path = ""
ru_trans_path = get_resource_path("data/translations/ru/ru.qm")
uk_trans_path = get_resource_path("data/translations/uk/uk.qm")
