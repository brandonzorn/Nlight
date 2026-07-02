from nlightreader.consts.items import ShikimoriItems
from nlightreader.items import RequestForm
from nlightreader.models import Kind, Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)


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
        response = self._client.get_json(url, params=params)

        mangas: list[Manga] = []
        if not isinstance(response, list):
            return mangas
        for data in response:
            mangas.append(self._setup_manga(data))
        return mangas

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
