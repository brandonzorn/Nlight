from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from desu_readerUI import Ui_Dialog


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
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.prev_page.clicked.connect(lambda: self.press_key('prev_page'))
        self.ui.next_page.clicked.connect(lambda: self.press_key('next_page'))
        self.ui.prev_chp.clicked.connect(lambda: self.press_key('prev_ch'))
        self.ui.next_chp.clicked.connect(lambda: self.press_key('next_ch'))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Left:
            self.press_key('prev_page')
        if event.key() == Qt.Key_Right:
            self.press_key('next_page')
        if event.key() == Qt.Key_Up:
            self.press_key('next_ch')
        if event.key() == Qt.Key_Down:
            self.press_key('prev_ch')
        event.accept()

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
        self.ui.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')

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
        self.ui.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')