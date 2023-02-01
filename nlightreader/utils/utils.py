import contextlib
from typing import Callable

import requests
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QLocale, Signal, QObject
from PySide6.QtWidgets import QApplication

from nlightreader.consts import DEFAULT_HEADERS, MangaKinds
from nlightreader.consts.files import LangIcons, Translations, Styles


def get_html(url: str, headers: dict = DEFAULT_HEADERS, params=None):
    try:
        assert "test" not in QApplication.arguments(), "Test mode"
        return requests.get(url, headers=headers, params=params)
    except Exception as e:
        print(f"{e=}", f"{url=}", f"{params=}", f"{headers=}", sep="\n")


def get_language_icon(language: str):
    match language:
        case 'ru':
            return LangIcons.Ru
        case 'en':
            return LangIcons.Gb
        case 'jp':
            return LangIcons.Jp
        case 'ua':
            return LangIcons.Ua
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
            return Translations.Ru
        case QLocale.Language.Ukrainian:
            return Translations.Uk
        case _:
            return Translations.En


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
    dark = Styles.Dark
    light = Styles.Light
    themes = {"Dark": dark, "Light": light}
    return themes[style]


class Signals(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()


class Worker(QRunnable):
    def __init__(self, target: Callable, args=(), kwargs=None, *, callback=None):
        super(Worker, self).__init__()
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self.signals = Signals()
        if callback:
            self.signals.finished.connect(callback)

    @Slot()
    def run(self):
        self._target(*self._args, **self._kwargs)
        self.signals.finished.emit()

    def start(self):
        QThreadPool.globalInstance().start(self)


@contextlib.contextmanager
def lock_ui(ui_to_lock: list):
    [i.setEnabled(False) for i in ui_to_lock]
    yield
    [i.setEnabled(True) for i in ui_to_lock]
