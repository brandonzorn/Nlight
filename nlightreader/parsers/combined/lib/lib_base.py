from typing import override

from nlightreader.core.enums import Language
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Manga
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.utils import get_html


class LibBase(AbstractCatalog):
    _URL = None
    _URL_API = "https://api.cdnlibs.org/api"

    _CONTENT_NAME = None
    _SITE_ID = None

    @property
    def _headers(self) -> dict[str, str]:
        return {"Referer": f"{self._URL}/"}

    @override
    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}"
        params = {"fields[]": ["summary", "rate_avg"]}
        response = get_html(
            url,
            params=params,
            headers=self._headers,
            content_type="json",
        )

        if not isinstance(response, dict):
            return manga

        data = response.get("data")

        if not isinstance(data, dict):
            return manga

        manga.preview_url = data.get("cover", {}).get("md")
        manga.score = float(data.get("rating", {}).get("average", 0))
        if isinstance(description := data.get("summary"), str):
            manga.add_description(Language.ru, description)
        return manga

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/{self._CONTENT_NAME}"
        params = {
            "site_id[]": self._SITE_ID,
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
            headers=self._headers,
            content_type="json",
        )

        mangas: list[Manga] = []
        if not isinstance(response, dict):
            return mangas
        for i in response.get("data", {}):
            if not isinstance(i, dict):
                continue
            manga = Manga(
                i["slug_url"],
                self.CATALOG_ID,
                i["name"],
                i.get("rus_name", ""),
            )
            manga.preview_url = i.get("cover", {}).get("md")
            manga.score = float(i.get("rating", {}).get("average", 0))
            mangas.append(manga)
        return mangas

    @override
    def get_chapters(self, manga: Manga) -> list[Chapter]:
        if not manga.content_id:
            return []

        branches_url = (
            f"{self._URL_API}/branches/{manga.content_id.split('--')[0]}"
        )

        branches = {}
        branches_response = get_html(branches_url, content_type="json")
        if isinstance(branches_response, dict):
            for branch in branches_response.get("data", {}):
                branches.update({branch["id"]: branch["teams"][0]["name"]})

        chapters_url = (
            f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}/chapters"
        )

        chapters: list[Chapter] = []
        chapters_response = get_html(chapters_url, content_type="json")
        if not isinstance(chapters_response, dict):
            return chapters
        for i in reversed(chapters_response.get("data", {})):
            chapter = Chapter(
                str(i["id"]),
                self.CATALOG_ID,
                i["volume"],
                i["number"],
                i["name"],
                Language.ru,
            )
            if branches_data := i.get("branches"):
                chapter.translator = branches.get(
                    branches_data[0]["branch_id"],
                )
            chapters.append(chapter)
        return chapters

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        return get_html(
            manga.preview_url,
            content_type="content",
            headers=self._headers,
        )


__all__ = ["LibBase"]
