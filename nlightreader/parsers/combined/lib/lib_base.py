from nlightreader.consts.enums import Nl
from nlightreader.consts.urls import URL_LIB_API
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Manga
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
        params = {"fields[]": ["summary", "rate_avg"]}
        response = get_html(url, params=params, content_type="json")
        if response:
            data = response["data"]
            manga.preview_url = data["cover"]["md"]
            manga.score = float(data["rating"]["average"])
            if description := data.get("summary"):
                manga.add_description(Nl.Language.ru, description)
        return manga

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self.url_api}/{self.content_name}"
        params = {
            "site_id[]": self.site_id,
            "sort_by": form.get_order_id(),
            "types[]": form.get_kind_ids(),
            "genres[]": form.get_genre_ids(),
            "q": form.search,
        }
        cookies = {"adult_caution": '{"media":true,"content":true}'}
        response = get_html(
            url,
            params=params,
            cookies=cookies,
            content_type="json",
        )

        mangas = []
        if response:
            for i in response.get("data"):
                manga = Manga(
                    i["slug_url"],
                    self.CATALOG_ID,
                    i["name"],
                    i["rus_name"],
                )
                manga.preview_url = i["cover"]["md"]
                manga.score = float(i["rating"]["average"])
                mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        branches_url = (
            f"{self.url_api}/branches/{manga.content_id.split('--')[0]}"
        )

        branches = {}
        if branches_response := get_html(branches_url, content_type="json"):
            for branch in branches_response["data"]:
                branches.update({branch["id"]: branch["teams"][0]["name"]})

        chapters_url = (
            f"{self.url_api}/{self.content_name}/{manga.content_id}/chapters"
        )

        chapters: list[Chapter] = []
        if chapters_response := get_html(chapters_url, content_type="json"):
            for i in chapters_response["data"]:
                chapter = Chapter(
                    str(i["id"]),
                    self.CATALOG_ID,
                    i["volume"],
                    i["number"],
                    i["name"],
                    Nl.Language.ru,
                )
                if branches_data := i.get("branches"):
                    chapter.translator = branches.get(
                        branches_data[0]["branch_id"],
                    )
                chapters.append(chapter)
        chapters.reverse()
        return chapters

    def get_preview(self, manga: Manga):
        return get_html(manga.preview_url, content_type="content")


__all__ = [
    "LibBase",
]
