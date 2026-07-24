class BaseContentError(Exception):
    pass


class NoContentError(BaseContentError):
    pass


class FetchContentError(BaseContentError):
    pass


class RequestsParamsError(BaseContentError):
    pass


__all__ = [
    "BaseContentError",
    "FetchContentError",
    "NoContentError",
    "RequestsParamsError",
]
