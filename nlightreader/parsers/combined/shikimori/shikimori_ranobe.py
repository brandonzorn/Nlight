from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)


class ShikimoriRanobe(ShikimoriBase, AbstractRanobeCatalog):
    CATALOG_NAME = "Shikimori(Ranobe)"
    _CONTENT_NAME = "ranobe"


__all__ = ["ShikimoriRanobe"]
