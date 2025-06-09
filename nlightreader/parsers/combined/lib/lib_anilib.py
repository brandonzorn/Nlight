from nlightreader.consts.enums import Nl
from nlightreader.consts.items import AniLibItems
from nlightreader.consts.urls import URL_ANILIB
from nlightreader.models import Chapter, Manga
from nlightreader.parsers.catalogs_base import AbstractAnimeCatalog
from nlightreader.parsers.combined.lib.lib_base import LibBase
from nlightreader.utils.utils import get_html


class LibAnilib(LibBase, AbstractAnimeCatalog):
    CATALOG_NAME = "AniLib"
    CATALOG_ID = 14

    def __init__(self):
        super().__init__()
        self.url = URL_ANILIB
        self.items = AniLibItems

        self.content_name = "anime"
        self.site_id = 5

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self.url_api}/episodes?anime_id={manga.content_id}"
        episodes: list[Chapter] = []
        episodes_response = get_html(url, content_type="json")
        if episodes_response:
            for i in episodes_response["data"]:
                episode = Chapter(
                    i["id"],
                    self.CATALOG_ID,
                    None,
                    "",
                    f"Episode {i['number']}",
                    Nl.Language.ru,
                )
                episodes.append(episode)
        episodes.reverse()
        return episodes


__all__ = [
    "LibAnilib",
]
