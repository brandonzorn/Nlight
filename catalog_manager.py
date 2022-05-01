from parser.Desu import Desu
from parser.MangaDex import MangaDex
from parser.Shikimori import Shikimori

CATALOGS = {0: Desu, 1: Shikimori, 2: MangaDex}


def get_catalog(catalog_id=0):
    return CATALOGS.get(catalog_id)
