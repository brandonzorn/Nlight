from typing import override

from database import Database
from items import RequestForm
from models import Manga
from parsers.catalog import AbstractCatalog


class LocalLibrary(AbstractCatalog):
    CATALOG_NAME = "LocalLib"

    def __init__(self) -> None:
        self._db = Database()

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        return self._db.library.get_by_library_list(form.lib_list)


__all__ = ["LocalLibrary"]
