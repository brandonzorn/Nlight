from functools import wraps
from typing import cast


def singleton[T: type](cls: T) -> T:
    instance: list[object | None] = [None]

    @wraps(cls)
    def wrapper(*args: object, **kwargs: object) -> object:
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return cast(T, wrapper)


__all__ = ["singleton"]
