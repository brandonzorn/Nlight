from consts.items import ShikimoriRanobeItems
from parsers.catalogs_base import AbstractRanobeCatalog

from .shikimori_base import ShikimoriBase


class ShikimoriRanobe(ShikimoriBase, AbstractRanobeCatalog):
    CATALOG_ID = 1002
    CATALOG_NAME = "Shikimori(Ranobe)"

    _FILTERS = ShikimoriRanobeItems

    _CONTENT_NAME = "ranobe"
    _PREVIEW_FOLDER = "mangas"
    _GENRE_ENTRY_TYPE = "Manga"


__all__ = ["ShikimoriRanobe"]
