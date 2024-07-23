from types import NoneType

import validators


class Image:
    def __init__(self, image_id: str, page_number: int, url: str | None):
        self.id = image_id
        self.page_number = page_number
        self.__url = None

        self.url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str | None):
        if not isinstance(url, (str, NoneType)):
            raise TypeError(f"Url must be str or None got {type(url)}")
        if url is not None and not validators.url(url):
            raise ValueError(f"Url {url} is not valid")
        self.__url = url

    @staticmethod
    def get_empty_instance():
        return Image("", 1, None)
