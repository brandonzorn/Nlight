from nlightreader.items import RequestForm
from nlightreader.models import Manga
from nlightreader.utils.database import Database


class LocalLibrary:
    CATALOG_NAME = "LocalLib"

    def __init__(self) -> None:
        self.db: Database = Database()

    def search_manga(self, form: RequestForm) -> list[Manga]:
        return self.db.get_manga_library(form.lib_list)


__all__ = ["LocalLibrary"]
