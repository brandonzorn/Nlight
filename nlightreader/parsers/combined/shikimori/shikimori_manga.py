from nlightreader.consts.items import ShikimoriItems
from nlightreader.items import RequestForm
from nlightreader.models import Kind, Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)
from nlightreader.utils.utils import get_html


class ShikimoriManga(ShikimoriBase, AbstractMangaCatalog):
    CATALOG_NAME = "Shikimori(Manga)"

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/mangas"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "order": form.get_order_id(),
            "genre": ",".join(form.get_genre_ids()),
            "kind": ",".join(form.get_kind_ids()),
        }
        response = get_html(
            url,
            headers=self._HEADERS,
            params=params,
            content_type="json",
        )

        mangas = []
        if response:
            for i in response:
                mangas.append(self._setup_manga(i))
        return mangas

    def get_kinds(self) -> list[Kind]:
        return [
            Kind(
                i["value"],
                self.CATALOG_ID,
                i["name"],
                i["russian"],
            )
            for i in ShikimoriItems.KINDS
        ]


__all__ = [
    "ShikimoriManga",
]
