from nlightreader.consts import URL_DESU_API, DESU_HEADERS, URL_DESU
from nlightreader.consts.items import DesuItems
from nlightreader.items import Manga, Chapter, Image, Genre, RequestForm
from nlightreader.parsers.catalogs_base import MangaCatalog
from nlightreader.utils.utils import get_html, get_data


class Desu(MangaCatalog):
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
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = get_data(html.json(), ["response"], {})
            manga.genres = [Genre(i.get("id"), self.CATALOG_ID, i.get("text"), i.get("russian"))
                            for i in data.get("genres")]
            manga.score = data.get("score")
            manga.kind = data.get("kind")
            manga.description.update({"all": data.get("description")})
            manga.volumes = data.get("chapters").get("last").get("vol")
            manga.chapters = data.get("chapters").get("last").get("ch")
            manga.status = data.get("status")
        return manga

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "genres": ",".join([i.content_id for i in form.genres]),
            "order": form.order.content_id,
            "kinds": ",".join([i.content_id for i in form.kinds]),
        }
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in get_data(html.json(), ["response"]):
                manga.append(Manga(i.get("id"), self.CATALOG_ID, i.get("name"), i.get("russian")))
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
                chapters.append(Chapter(i.get("id"), self.CATALOG_ID, vol, ch, i.get("title"), "ru"))
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/{manga.content_id}/chapter/{chapter.content_id}"
        html = get_html(url, headers=self.headers)
        images = []
        if html and html.status_code == 200 and html.json():
            for i in get_data(html.json(), ["response", "pages", "list"]):
                image_id = i.get("id")
                page = i.get("page")
                img: str = i.get("img")
                img = img.replace("desu.me", "desu.win")
                images.append(Image(image_id, page, img))
        return images

    def get_image(self, image: Image):
        headers = self.headers.copy()
        headers.update({"Referer": f"{self.url}/"})
        response = get_html(image.img, headers=headers, content_type="content")
        return response

    def get_preview(self, manga: Manga):
        response = get_html(f"{self.url}/data/manga/covers/preview/{manga.content_id}.jpg", content_type="content")
        return response

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/manga/{manga.content_id}"
