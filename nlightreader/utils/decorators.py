from functools import wraps


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


__all__ = [
    "singleton",
]
