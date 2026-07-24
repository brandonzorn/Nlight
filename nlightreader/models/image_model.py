from types import NoneType

import validators


class Image:
    def __init__(
        self,
        *,
        content_id: str,
        page_number: int,
        url: str | None,
    ) -> None:
        self._content_id = content_id
        self._page_number = page_number
        self._url = None

        self.url = url

    @property
    def page_number(self) -> int:
        return self._page_number

    @property
    def url(self) -> str | None:
        return self._url

    @url.setter
    def url(self, url: str | None) -> None:
        if not isinstance(url, (str, NoneType)):
            msg = f"Url must be str or None got {type(url)}"
            raise TypeError(msg)
        if url is not None and not validators.url(url):
            msg = f"Url {url} is not valid"
            raise ValueError(msg)
        self._url = url


class ImageStub(Image):
    def __init__(self) -> None:
        super().__init__(content_id="", page_number=1, url=None)


__all__ = ["Image", "ImageStub"]
