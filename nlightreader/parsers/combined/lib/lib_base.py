from nlightreader.consts.enums import Nl
from nlightreader.consts.urls import URL_LIB_API
from nlightreader.items import Manga, RequestForm, Chapter
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.utils import get_html


class LibBase(AbstractCatalog):
    def __init__(self):
        super().__init__()
        self.url_api = URL_LIB_API

        # override in subclass
        self.content_name = None
        self.site_id = None

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self.url_api}/{self.content_name}/{manga.content_id}"
        params = {"fields[]": "summary"}
        response = get_html(url, params=params, content_type="json")
        if response:
            data = response["data"]
            manga.add_description(Nl.Language.ru, data["summary"])
        return manga

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self.url_api}/{self.content_name}"
        mangas = []
        params = {
            "site_id[]": self.site_id,
            "q": form.search,
        }
        cookies = {"adult_caution": '{"media":true,"content":true}'}
        response = get_html(url, params=params, cookies=cookies, content_type="json")
        if response:
            for i in response.get("data"):
                manga = Manga(i["slug_url"], self.CATALOG_ID, i["name"], i["rus_name"])
                manga.preview_url = i["cover"]["md"]
                manga.score = i["rating"]["average"]
                mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self.url_api}/{self.content_name}/{manga.content_id}/chapters"
        chapters: list[Chapter] = []
        response = get_html(url, content_type="json")
        if response:
            for i in response["data"]:
                chapter = Chapter(
                        i["id"], self.CATALOG_ID, i["volume"], i["number"], i["name"],
                )
                chapter.language = Nl.Language.ru
                chapters.append(chapter)
        chapters.reverse()
        return chapters

    def get_preview(self, manga: Manga):
        return get_html(manga.preview_url, content_type="content")
