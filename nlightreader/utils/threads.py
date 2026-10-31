from collections.abc import Callable
import contextlib
import logging

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThread,
    QThreadPool,
    Signal,
    Slot,
)

logger = logging.getLogger(__name__)


class Signals(QObject):
    on_error = Signal(object)
    on_finished = Signal(object)


class BaseThread:
    def __init__(
        self,
        target: Callable,
        args: tuple = (),
        kwargs: dict | None = None,
        *,
        callback: Callable | None = None,
        error_callback: Callable | None = None,
    ) -> None:
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs or {}

        self.signals = Signals()
        if callback:
            self.signals.on_finished.connect(callback)
        if error_callback:
            self.signals.on_error.connect(error_callback)

    @Slot()
    def run(self) -> None:
        try:
            result = self._target(*self._args, **self._kwargs)
        except Exception as e:
            logger.exception("Thread raised an exception:\n")
            with contextlib.suppress(RuntimeError):
                self.signals.on_error.emit(e)
        else:
            with contextlib.suppress(RuntimeError):
                self.signals.on_finished.emit(result)


class NWorker(BaseThread, QRunnable):
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
        args: tuple = (),
        kwargs: dict | None = None,
        *,
        callback: Callable | None = None,
        error_callback: Callable | None = None,
    ) -> None:
        super().__init__(
            target,
            args,
            kwargs,
            callback=callback,
            error_callback=error_callback,
        )
        self.setAutoDelete(True)

    def start(self, thread_pool: QThreadPool | None) -> None:
        if thread_pool is None:
            thread_pool = QThreadPool.globalInstance()
        thread_pool.start(self)


class NThread(BaseThread, QThread):
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
        args: tuple = (),
        kwargs: dict | None = None,
        *,
        callback: Callable | None = None,
        error_callback: Callable | None = None,
    ) -> None:
        super().__init__(
            target,
            args,
            kwargs,
            callback=callback,
            error_callback=error_callback,
        )


__all__ = ["NThread", "NWorker"]
