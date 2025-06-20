class NoContentError(Exception):
    pass


class FetchContentError(Exception):
    pass


class RequestsParamsError(Exception):
    pass


__all__ = [
    "FetchContentError",
    "NoContentError",
    "RequestsParamsError",
]
