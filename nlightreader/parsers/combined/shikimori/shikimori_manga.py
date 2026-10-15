from consts.items import ShikimoriItems
from models import Kind
from parsers.catalogs_base import AbstractMangaCatalog

from .shikimori_base import ShikimoriBase


class ShikimoriManga(ShikimoriBase, AbstractMangaCatalog):
    CATALOG_NAME = "Shikimori(Manga)"
    _CONTENT_NAME = "mangas"

    def get_kinds(self) -> list[Kind]:
        return [
            Kind(
                content_id=i["value"],
                catalog_id=self.CATALOG_ID,
                name=i["name"],
                russian=i["russian"],
            )
            for i in ShikimoriItems.KINDS
        ]


__all__ = ["ShikimoriManga"]
