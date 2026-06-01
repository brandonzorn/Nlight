from types import NoneType

import validators


class Image:
    def __init__(
        self, image_id: str, page_number: int, url: str | None,
    ) -> None:
        self.id = image_id
        self.page_number = page_number
        self.__url = None

        self.url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str | None) -> None:
        if not isinstance(url, (str, NoneType)):
            msg = f"Url must be str or None got {type(url)}"
            raise TypeError(msg)
        if url is not None and not validators.url(url):
            msg = f"Url {url} is not valid"
            raise ValueError(msg)
        self.__url = url


__all__ = [
    "Image",
]
