from desureader.utils.database import Database
from items import RequestForm


class LocalLib:
    catalog_name = 'LocalLib'

    def __init__(self):
        self.db: Database = Database()

    def search_manga(self, params: RequestForm):
        manga = self.db.get_manga_library(params.lib_list)
        return manga
