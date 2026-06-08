from nlightreader.items import RequestForm
from nlightreader.models import Manga
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)
from nlightreader.utils.utils import get_html


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
        response = get_html(
            url,
            headers=self._HEADERS,
            params=params,
            content_type="json",
        )

        mangas: list[Manga] = []
        if not isinstance(response, dict):
            return mangas
        for data in response:
            mangas.append(self._setup_manga(data))
        return mangas


__all__ = [
    "ShikimoriRanobe",
]
