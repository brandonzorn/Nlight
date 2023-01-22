import contextlib
from typing import Callable

import requests
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QLocale, Signal, QObject
from PySide6.QtWidgets import QApplication

from nlightreader.consts import DEFAULT_HEADERS, ru_icon_path, gb_icon_path, jp_icon_path, ua_icon_path, MangaKinds, \
    ru_trans_path, uk_trans_path, en_trans_path, light_style, dark_style


def get_html(url: str, headers: dict = DEFAULT_HEADERS, params=None):
    try:
        assert "test" not in QApplication.arguments(), "Test mode"
        return requests.get(url, headers=headers, params=params)
    except Exception as e:
        print(f"{e=}", f"{url=}", f"{params=}", f"{headers=}", sep="\n")


def get_language_icon(language: str):
    match language:
        case 'ru':
            return ru_icon_path
        case 'en':
            return gb_icon_path
        case 'jp':
            return jp_icon_path
        case 'ua':
            return ua_icon_path
        case _:
            return ''


def get_manga_kind(kind: str) -> None:
    kinds_matches = {'manga': MangaKinds.manga, 'manhwa': MangaKinds.manhwa, 'manhua': MangaKinds.manhua,
                     'one_shot': MangaKinds.one_shot, 'doujin': MangaKinds.doujin, 'ranobe': MangaKinds.ranobe}
    assert kind in kinds_matches, f"Not fond matches for {kind}"
    return kinds_matches[kind]


def get_locale_path(locale: QLocale.Language) -> str:
    match locale:
        case QLocale.Language.Russian:
            return ru_trans_path
        case QLocale.Language.Ukrainian:
            return uk_trans_path
        case _:
            return en_trans_path


def get_data(a: dict, path: list, default_val=None):
    if default_val is None:
        default_val = {}
    data = a
    for p in path:
        try:
            data = data.get(p)
        except Exception as e:
            data = default_val
            print("Get data error\t", e)
    return data


def get_ui_style(style: str):
    dark = open(dark_style).read()
    light = open(light_style).read()
    themes = {"Dark": dark, "Light": light}
    return themes[style]


class Signals(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()


class Worker(QRunnable):
    def __init__(self, func: Callable, callback=None, pre=None, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.pre = pre
        self.args = args
        self.kwargs = kwargs
        self.signals = Signals()
        if callback:
            self.signals.finished.connect(callback)

    @Slot()
    def run(self):
        self.func(*self.args, **self.kwargs)
        self.signals.finished.emit()

    def start(self):
        if self.pre:
            self.pre()
        QThreadPool.globalInstance().start(self)


@contextlib.contextmanager
def lock_ui(ui_to_lock: list):
    [i.setEnabled(False) for i in ui_to_lock]
    yield
    [i.setEnabled(True) for i in ui_to_lock]
