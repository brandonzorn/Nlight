from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QObject
import keyboard


class Communicate(QObject):
    next_page = pyqtSignal()
    prev_page = pyqtSignal()
    next_ch = pyqtSignal()
    prev_ch = pyqtSignal()


class Reader(QWidget):
    def __init__(self):
        super().__init__()
        self.c = Communicate()
        self.cur_chapter: int = 1
        self.max_chapters: int = 1
        self.cur_page: int = 1
        self.max_page: int = 1
        keyboard.add_hotkey('left', lambda: self.press_key('prev_page'))
        keyboard.add_hotkey('right', lambda: self.press_key('next_page'))
        keyboard.add_hotkey('up', lambda: self.press_key('next_ch'))
        keyboard.add_hotkey('down', lambda: self.press_key('prev_ch'))
        keyboard.add_hotkey('esc', self.close_reader)

    def close_reader(self):
        self.hide()

    def press_key(self, e):
        if self.isActiveWindow():
            if e == 'next_page':
                self.c.next_page.emit()
            if e == 'prev_page':
                self.c.prev_page.emit()
            if e == 'next_ch':
                self.c.next_ch.emit()
            if e == 'prev_ch':
                self.c.prev_ch.emit()

    def change_page(self, page):
        if page == '+':
            if self.cur_page == self.max_page and self.cur_chapter == self.max_chapters:
                return
            elif self.cur_page == self.max_page:
                self.press_key('next_ch')
            else:
                self.cur_page += 1
        elif page == '-':
            if self.cur_page > 1:
                self.cur_page -= 1
            elif self.cur_page == 1 and self.cur_chapter == 1:
                return
            else:
                self.press_key('prev_ch')

    def change_chapter(self, page=None):
        if page == '+':
            if self.cur_chapter != self.max_chapters:
                self.cur_chapter += 1
            else:
                return
        elif page == '-':
            if self.cur_chapter > 1:
                self.cur_chapter -= 1
            elif self.cur_chapter == 1:
                return
        self.cur_page = 1
