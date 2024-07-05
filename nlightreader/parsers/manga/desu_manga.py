from nlightreader.consts.urls import DESU_HEADERS, URL_DESU, URL_DESU_API
from nlightreader.consts.enums import Nl
from nlightreader.consts.items import DesuItems
from nlightreader.items import Chapter, Genre, Image, Manga, RequestForm
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import get_data, get_html


class Desu(AbstractMangaCatalog):
    CATALOG_ID = 0
    CATALOG_NAME = "Desu"

    def __init__(self):
        super().__init__()
        self.url = URL_DESU
        self.url_api = URL_DESU_API
        self.headers = DESU_HEADERS
        self.items = DesuItems

    def get_manga(self, manga: Manga):
        url = f"{self.url_api}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            data = get_data(response, ["response"], {})
            manga.genres = [
                Genre(
                    str(i.get("id")),
                    self.CATALOG_ID,
                    i.get("text"),
                    i.get("russian"),
                )
                for i in data.get("genres")
            ]
            manga.score = data.get("score")
            manga.kind = Nl.MangaKind.from_str(data.get("kind"))
            manga.volumes = data.get("chapters").get("last").get("vol")
            manga.chapters = data.get("chapters").get("last").get("ch")
            manga.status = data.get("status")

            manga.add_description(
                Nl.Language.undefined,
                data.get("description"),
            )
        return manga

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}"
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
            headers=self.headers,
            params=params,
            content_type="json",
        )
        manga = []
        if response:
            for i in get_data(response, ["response"]):
                manga.append(
                    Manga(
                        str(i.get("id")),
                        self.CATALOG_ID,
                        i.get("name"),
                        i.get("russian"),
                    ),
                )
        return manga

    def get_chapters(self, manga: Manga):
        url = f"{self.url_api}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        chapters = []
        if response:
            for i in get_data(response, ["response", "chapters", "list"]):
                vol = i.get("vol")
                ch = i.get("ch")
                vol = str(vol) if vol is not None else vol
                ch = str(ch) if ch is not None else ch
                chapter = Chapter(
                    str(i.get("id")),
                    self.CATALOG_ID,
                    vol,
                    ch,
                    i.get("title"),
                    Nl.Language.ru,
                )
                chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/{manga.content_id}/chapter/{chapter.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        images = []
        if response:
            for i in get_data(response, ["response", "pages", "list"]):
                image_id = str(i.get("id"))
                page = i.get("page")
                img: str = i.get("img")
                img = img.replace("desu.me", "desu.win")
                images.append(Image(image_id, page, img))
        return images

    def get_image(self, image: Image):
        headers = self.headers | {"Referer": f"{self.url}/"}
        return get_html(image.img, headers=headers, content_type="content")

    def get_preview(self, manga: Manga):
        return get_html(
            f"{self.url}/data/manga/covers/preview/{manga.content_id}.jpg",
            content_type="content",
        )

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/manga/{manga.content_id}"
