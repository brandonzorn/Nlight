from typing import Callable

from PySide6.QtCore import QThreadPool, QRunnable, QObject, Signal, Slot, QThread


class Signals(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()


class Worker(QRunnable):
    def __init__(self, target: Callable, args=(), kwargs=None, *, callback=None, locker=None):
        super(Worker, self).__init__()
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._locker = locker
        self.signals = Signals()
        if callback:
            self.signals.finished.connect(callback)

    @Slot()
    def run(self):
        if self._locker:
            while not self._locker.tryLock():
                pass
            self._target(*self._args, **self._kwargs)
            self._locker.unlock()
        else:
            self._target(*self._args, **self._kwargs)
        self.signals.finished.emit()

    def start(self, pool=None):
        if pool is None:
            pool = QThreadPool.globalInstance()
        if pool.activeThreadCount() == pool.maxThreadCount():
            return
        pool.start(self)


class Thread(QThread):
    def __init__(self, target: Callable, args=(), kwargs=None, *, callback=None, locker=None):
        super().__init__()
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._locker = locker
        self.signals = Signals()
        if callback:
            self.signals.finished.connect(callback)

    @Slot()
    def run(self):
        if self._locker:
            while not self._locker.tryLock():
                pass
            self._target(*self._args, **self._kwargs)
            self._locker.unlock()
        else:
            self._target(*self._args, **self._kwargs)
        self.signals.finished.emit()