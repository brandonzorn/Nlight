from database import Database
from items import Manga, RequestForm
from parser.Parser import Parser


class LocalLib(Parser):
    catalog_name = 'LocalLib'

    def __init__(self):
        self.catalog_id = -1
        self.db: Database = Database()

    def get_manga(self, manga: Manga):
        return manga

    def search_manga(self, params: RequestForm):
        manga = self.db.get_manga_library(params.mylist)
        return manga
