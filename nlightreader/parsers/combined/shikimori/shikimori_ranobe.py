from nlightreader.items import RequestForm
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.parsers.combined.shikimori.shikimori_base import (
    ShikimoriBase,
)
from nlightreader.utils.utils import get_html


class ShikimoriRanobe(ShikimoriBase, AbstractRanobeCatalog):
    CATALOG_NAME = "Shikimori(Ranobe)"

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}/ranobe"
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
            headers=self.headers,
            params=params,
            content_type="json",
        )

        mangas = []
        if response:
            for i in response:
                mangas.append(self.setup_manga(i))
        return mangas
