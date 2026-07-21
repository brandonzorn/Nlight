from typing import override

from nlightreader.database import Database
from nlightreader.items import RequestForm
from nlightreader.models import Manga


class LocalLibrary:
    CATALOG_NAME = "LocalLib"

    def __init__(self) -> None:
        self._db = Database()

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        return self._db.library.get_by_library_list(form.lib_list)


__all__ = ["LocalLibrary"]
