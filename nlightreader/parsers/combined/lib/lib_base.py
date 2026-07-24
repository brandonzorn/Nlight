from typing import ClassVar, override

from nlightreader.core.enums import Language
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Manga
from nlightreader.parsers.catalog import AbstractCatalog
from nlightreader.utils.network import NetworkClient
from nlightreader.utils.utils import dd_get


class LibBase(AbstractCatalog):
    _URL = None
    _URL_API = "https://api.cdnlibs.org/api"

    _COOKIES: ClassVar = {"adult_caution": '{"media":true,"content":true}'}

    _CONTENT_NAME = None
    _SITE_ID = None

    def __init__(self) -> None:
        self._client = NetworkClient(
            headers={
                "Site-Id": str(self._SITE_ID),
                "Referer": f"{self._URL}/",
            },
            cookies=self._COOKIES,
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

        summary = data.get("summary")
        if not summary:
            return manga

        if isinstance(summary, str):
            manga.add_description(Language.RUSSIAN, summary)
        if isinstance(summary, dict):
            text = dd_get(summary, "content.0.content.0.text")
            if isinstance(text, str):
                manga.add_description(Language.RUSSIAN, text)
        return manga

    @override
    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}/{self._CONTENT_NAME}"
        params = {
            "page": form.page,
            "site_id[]": self._SITE_ID,
            "sort_by": form.get_order_id(),
            "types[]": form.get_kind_ids(),
            "genres[]": form.get_genre_ids(),
            "q": form.search,
        }
        response = self._client.get_json(url, params=params)

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

        branches: dict[str, str] = {}
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
            for branch in i.get("branches", []):
                chapter = Chapter(
                    content_id=f"{i['id']}_{branch['branch_id']}",
                    catalog_id=self.CATALOG_ID,
                    volume_number=i["volume"],
                    chapter_number=i["number"],
                    title=i["name"],
                    language=Language.RUSSIAN,
                )
                chapter.translator = branches.get(branch["branch_id"])
                chapters.append(chapter)
        return chapters

    @override
    def get_preview(self, manga: Manga) -> bytes | None:
        url = manga.preview_url
        if url is None:
            return None
        return self._client.get_bytes(url)


__all__ = ["LibBase"]
