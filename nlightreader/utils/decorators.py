from functools import wraps
from typing import Callable


def singleton(cls):
    """
    A decorator that transforms a class into a singleton.

    Parameters:
        cls (type): The class to be transformed.

    Returns:
        callable: Wrapped class as a singleton.
    """
    instance = [None]

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper


def with_lock_thread(locker):
    """
    A decorator that acquires a lock before executing a function in a threaded environment.

    Parameters:
        locker (threading.Lock): The lock object to acquire.

    Returns:
        callable: Decorator that acquires the lock before executing wrapped function.
    """
    def decorator(func: Callable):

        @wraps(func)
        def wrapper(*args, **kwargs):
            with locker:
                return func(*args, **kwargs)
        return wrapper
    return decorator
