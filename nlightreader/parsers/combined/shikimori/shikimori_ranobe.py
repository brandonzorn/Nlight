from parsers.catalogs_base import AbstractRanobeCatalog

from .shikimori_base import ShikimoriBase


class ShikimoriRanobe(ShikimoriBase, AbstractRanobeCatalog):
    CATALOG_NAME = "Shikimori(Ranobe)"
    _CONTENT_NAME = "ranobe"


__all__ = ["ShikimoriRanobe"]
