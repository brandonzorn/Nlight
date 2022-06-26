from parser.Desu import Desu
from parser.MangaDex import MangaDex
from parser.Rulate import Rulate
from parser.Shikimori import Shikimori

CATALOGS = {0: Desu, 1: Shikimori, 2: MangaDex, 3: Rulate}


def get_catalog(catalog_id=0):
    return CATALOGS.get(catalog_id)