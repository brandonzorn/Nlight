from typing import override

from nlightreader.core.enums import Language
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Manga
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.network import NetworkClient
from nlightreader.utils.utils import dd_get


class LibBase(AbstractCatalog):
    _URL = None
    _URL_API = "https://api.cdnlibs.org/api"

    _CONTENT_NAME = None
    _SITE_ID = None

    def __init__(self) -> None:
        self._client = NetworkClient(
            headers={
                "Site-Id": str(self._SITE_ID),
                "Referer": f"{self._URL}/",
            },
        )

    @override
    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}"
        params = {"fields[]": ["summary", "rate_avg"]}
        response = self._client.get_json(
            url,
            params=params,
        )

        if not isinstance(response, dict):
            return manga

        data = response.get("data")

        if not isinstance(data, dict):
            return manga

        manga.preview_url = data.get("cover", {}).get("md")
        manga.score = float(data.get("rating", {}).get("average", 0))

        summary = data.get("summary", {})

        if isinstance(summary, str) and summary:
            manga.add_description(Language.ru, summary)
        elif isinstance(summary, dict):
            text = dd_get(summary, "content.0.content.0.text")
            if text:
                manga.add_description(Language.ru, text)
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
        response = self._client.get_json(
            url,
            params=params,
            extra_cookies=cookies,
        )

        mangas: list[Manga] = []
        if not isinstance(response, dict):
            return mangas
        for i in response.get("data", {}):
            if not isinstance(i, dict):
                continue
            manga = Manga(
                content_id=i["slug_url"],
                catalog_id=self.CATALOG_ID,
                name=i["name"],
                russian=i.get("rus_name", ""),
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
        branches_response = self._client.get_json(branches_url)
        if isinstance(branches_response, dict):
            for branch in branches_response.get("data", {}):
                branches.update({branch["id"]: branch["teams"][0]["name"]})

        chapters_url = (
            f"{self._URL_API}/{self._CONTENT_NAME}/{manga.content_id}/chapters"
        )

        chapters: list[Chapter] = []
        chapters_response = self._client.get_json(chapters_url)
        if not isinstance(chapters_response, dict):
            return chapters
        for i in reversed(chapters_response.get("data", [])):
            chapter = Chapter(
                content_id=str(i["id"]),
                catalog_id=self.CATALOG_ID,
                volume_number=i["volume"],
                chapter_number=i["number"],
                title=i["name"],
                language=Language.ru,
            )
            if branches_data := i.get("branches"):
                chapter.translator = branches.get(
                    branches_data[0]["branch_id"],
                )
            chapters.append(chapter)
        return chapters

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(url)


__all__ = ["LibBase"]
