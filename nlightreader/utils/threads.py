import traceback
from typing import Callable

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThread,
    QThreadPool,
    Signal,
    Slot,
)


class Signals(QObject):
    error = Signal(Exception)
    finished = Signal(object)


class NlThread:
    def __init__(
        self,
        target: Callable,
        args=(),
        kwargs=None,
        *,
        callback=None,
        error_callback=None,
    ):
        super().__init__()
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self.signals = Signals()
        if callback:
            self.signals.finished.connect(callback)
        if error_callback:
            self.signals.error.connect(error_callback)

    @Slot()
    def run(self):
        try:
            result = self._target(*self._args, **self._kwargs)
        except Exception as e:
            traceback.print_exc()
            self.signals.error.emit(e)
        else:
            self.signals.finished.emit(result)


class Worker(NlThread, QRunnable):
    """
    Initializes a new `Runnable` instance.

    :param target:
        A callable object representing
        the target function to run in the thread.
    :param args:
        An optional tuple or list containing
        the arguments to pass to the target function.
        Defaults to an empty tuple.
    :param kwargs:
        An optional dictionary containing
        keyword arguments to pass to the target function.
        Defaults to an empty dictionary.
    :param callback:
        An optional callable object to invoke
        when the thread finishes running. Defaults to None.
    """

    def __init__(
        self,
        target: Callable,
        args=(),
        kwargs=None,
        *,
        callback=None,
        error_callback=None,
    ):
        super().__init__(
            target,
            args,
            kwargs,
            callback=callback,
            error_callback=error_callback,
        )

    def start(self, pool=None):
        if pool is None:
            pool = QThreadPool.globalInstance()
        if pool.activeThreadCount() == pool.maxThreadCount():
            return
        pool.start(self)


class Thread(NlThread, QThread):
    """
    Initializes a new `Thread` instance.

    :param target:
        A callable object representing
        the target function to run in the thread.
    :param args:
        An optional tuple or list containing
        the arguments to pass to the target function.
        Defaults to an empty tuple.
    :param kwargs:
        An optional dictionary containing
        keyword arguments to pass to the target function.
        Defaults to an empty dictionary.
    :param callback:
        An optional callable object to invoke
        when the thread finishes running. Defaults to None.
    """

    def __init__(
        self,
        target: Callable,
        args=(),
        kwargs=None,
        *,
        callback=None,
        error_callback=None,
    ):
        super().__init__(
            target,
            args,
            kwargs,
            callback=callback,
            error_callback=error_callback,
        )


__all__ = [
    "Worker",
    "Thread",
]
