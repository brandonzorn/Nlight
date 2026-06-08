from nlightreader.consts.items import DesuItems
from nlightreader.core.enums import Language, MangaKind, MangaStatus
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import get_data, get_html


class Desu(AbstractMangaCatalog):
    CATALOG_ID = 0
    CATALOG_NAME = "Desu"
    _FILTERS = DesuItems
    _URL = "https://desu.uno"
    _URL_API = f"{_URL}/manga/api"
    _HEADERS = {"User-Agent": "Nlight"}

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self._URL_API}/{manga.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        if not isinstance(response, dict):
            return manga
        data = response.get("response", {})
        manga.score = data.get("score", 0)
        manga.kind = MangaKind.from_str(data.get("kind"))
        manga.volumes = int(data["chapters"].get("last").get("vol"))
        manga.chapters = int(data["chapters"]["count"])
        manga.status = MangaStatus.from_str(data.get("status"))

        manga.add_description(
            Language.undefined,
            data.get("description"),
        )
        return manga

    def search_manga(self, form: RequestForm) -> list[Manga]:
        url = f"{self._URL_API}"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "genres": ",".join(form.get_genre_ids()),
            "order": form.get_order_id(),
            "kinds": ",".join(form.get_kind_ids()),
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

        for data in response.get("response", {}):
            mangas.append(
                Manga(
                    str(data.get("id")),
                    self.CATALOG_ID,
                    data.get("name"),
                    data.get("russian"),
                ),
            )
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self._URL_API}/{manga.content_id}"
        response = get_html(url, headers=self._HEADERS, content_type="json")
        chapters: list[Chapter] = []
        if not isinstance(response, dict):
            return chapters
        for data in get_data(response, ["response", "chapters", "list"]):
            vol = data.get("vol")
            ch = data.get("ch")
            vol = str(vol) if vol is not None else vol
            ch = str(ch) if ch is not None else ch
            chapter = Chapter(
                str(data.get("id")),
                self.CATALOG_ID,
                vol,
                ch,
                data.get("title"),
                Language.ru,
            )
            chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL_API}/{manga.content_id}/chapter/{chapter.content_id}"
        )
        response = get_html(url, headers=self._HEADERS, content_type="json")
        images: list[Image] = []
        if not isinstance(response, dict):
            return images
        for data in get_data(response, ["response", "pages", "list"]):
            image_id = str(data.get("id"))
            page = data.get("page")
            img: str = data.get("img")
            if "?" in img:
                img = img.split("?")[0]
            images.append(Image(image_id, page, img))
        return images

    def get_image(self, image: Image) -> bytes | None:
        headers = self._HEADERS | {"Referer": f"{self._URL}/"}
        return get_html(image.url, headers=headers, content_type="content")

    def get_preview(self, manga: Manga) -> bytes | None:
        return get_html(
            f"{self._URL}/data/manga/covers/preview/{manga.content_id}.jpg",
            content_type="content",
        )

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/manga/{manga.content_id}"


__all__ = ["Desu"]
