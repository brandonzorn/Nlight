from typing import Callable

from PySide6.QtCore import QThreadPool, QRunnable, QObject, Signal, Slot, QThread


class Signals(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()


class Worker(QRunnable):
    def __init__(self, target: Callable, args=(), kwargs=None, *, callback=None, locker=None):
        """
        Initializes a new `Runnable` instance.

        :param target: A callable object representing the target function to run in the thread.
        :param args: An optional tuple or list containing the arguments to pass to the target function.
            Defaults to an empty tuple.
        :param kwargs: An optional dictionary containing keyword arguments to pass to the target function.
            Defaults to an empty dictionary.
        :param callback: An optional callable object to invoke when the thread finishes running. Defaults to None.
        :param locker: An optional QMutex object to lock the thread during execution. Defaults to None.
        """
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
        """
        Initializes a new `Thread` instance.

        :param target: A callable object representing the target function to run in the thread.
        :param args: An optional tuple or list containing the arguments to pass to the target function.
            Defaults to an empty tuple.
        :param kwargs: An optional dictionary containing keyword arguments to pass to the target function.
            Defaults to an empty dictionary.
        :param callback: An optional callable object to invoke when the thread finishes running. Defaults to None.
        :param locker: An optional QMutex object to lock the thread during execution. Defaults to None.
        """
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
