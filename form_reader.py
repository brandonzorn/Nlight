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
