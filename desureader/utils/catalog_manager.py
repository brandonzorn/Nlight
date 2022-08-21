from desureader.parsers.Desu import Desu
from desureader.parsers.MangaDex import MangaDex, MangaDexLib
from desureader.parsers.Ranobehub import Ranobehub
from desureader.parsers.Rulate import Rulate
from desureader.parsers.Shikimori import ShikimoriBase, ShikimoriLib, ShikimoriRanobe, ShikimoriManga

CATALOGS = {0: Desu, 1: ShikimoriBase, 2: MangaDex, 3: Rulate, 4: Ranobehub}
USER_CATALOGS = [Desu, ShikimoriManga, ShikimoriRanobe, MangaDex, Rulate, Ranobehub]
LIB_CATALOGS = {ShikimoriBase: ShikimoriLib, MangaDex: MangaDexLib}


def get_catalog(catalog_id=0):
    return CATALOGS.get(catalog_id)


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)
