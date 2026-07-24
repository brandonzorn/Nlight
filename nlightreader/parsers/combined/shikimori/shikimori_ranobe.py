from nlightreader.items import RequestForm
from nlightreader.models import Manga
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)


class ShikimoriRanobe(ShikimoriBase, AbstractRanobeCatalog):
    CATALOG_NAME = "Shikimori(Ranobe)"

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/ranobe"
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
        mangas.extend(self._setup_manga(data) for data in response)
        return mangas


__all__ = ["ShikimoriRanobe"]
