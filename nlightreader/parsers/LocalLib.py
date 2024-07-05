from nlightreader.items import Manga, RequestForm
from nlightreader.utils.database import Database


class LocalLib:
    CATALOG_NAME = "LocalLib"

    def __init__(self):
        self.db: Database = Database()

    def search_manga(self, params: RequestForm) -> list[Manga]:
        return self.db.get_manga_library(params.lib_list)
