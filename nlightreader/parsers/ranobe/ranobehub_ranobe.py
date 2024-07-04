import base64

import bs4.element
from bs4 import BeautifulSoup

from nlightreader.consts.urls import URL_RANOBEHUB_API, URL_RANOBEHUB
from nlightreader.consts.enums import Nl
from nlightreader.consts.items import RanobehubItems
from nlightreader.items import RequestForm, Manga, Chapter, Image
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.utils.utils import get_html, get_data


class Ranobehub(AbstractRanobeCatalog):
    CATALOG_ID = 4
    CATALOG_NAME = "Ranobehub"

    def __init__(self):
        super().__init__()
        self.url = URL_RANOBEHUB
        self.url_api = URL_RANOBEHUB_API
        self.items = RanobehubItems

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self.url_api}/ranobe/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            data = response.get("data")
            manga.kind = Nl.MangaKind.ranobe
            manga.score = data.get("rating")

            manga.add_description(
                Nl.Language.undefined,
                data.get("description"),
            )
        return manga

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}/search"
        params = {
            "title-contains": form.search,
            "page": form.page,
            "sort": form.get_order_id(),
            "tags:positive[]": [int(i) for i in form.get_genre_ids()],
        }
        response = get_html(
            url,
            headers=self.headers,
            params=params,
            content_type="json",
        )
        mangas = []
        if response:
            for i in get_data(response, ["resource"], default_val=[]):
                manga_id = str(i.get("id"))
                name = i.get("names").get("eng")
                russian = i.get("names").get("rus")
                manga = Manga(manga_id, self.CATALOG_ID, name, russian)
                manga.preview_url = i.get("poster").get("medium")
                mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f"{self.url_api}/ranobe/{manga.content_id}/contents"
        response = get_html(url, headers=self.headers, content_type="json")
        chapters = []
        if response:
            for i in get_data(response, ["volumes"], default_val=[]):
                volume_num = i.get("num")
                for chapter_data in get_data(i, ["chapters"], []):
                    chapter = Chapter(
                        str(chapter_data.get("id")),
                        self.CATALOG_ID,
                        volume_num,
                        chapter_data.get("num"),
                        chapter_data.get("name"),
                        Nl.Language.ru,
                    )
                    chapters.append(chapter)
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self.url}/ranobe/"
            f"{manga.content_id}/{chapter.vol}/{chapter.ch}"
        )
        return [Image("", 1, url)]

    def get_image(self, image: Image):
        # Function to get content images from chapter
        def get_chapter_content_image(media_id: str):
            url = f"{self.url_api}/media/{media_id}"
            chapter_image = get_html(url, headers=self.headers).content
            str_equivalent_image = base64.b64encode(chapter_image).decode()
            return f"data:image/png;base64,{str_equivalent_image}"

        def find_text_container(
                containers: bs4.element.ResultSet,
        ) -> bs4.element.Tag:
            for container in containers:
                if container.has_attr("data-container"):
                    return container

        # Parse HTML content and extract text container
        response = get_html(image.img, content_type="text")
        if response:
            soup = BeautifulSoup(response, "html.parser")
            text_container = find_text_container(
                soup.findAll("div", {"class": "ui text container"}),
            )
            if not text_container:
                return

            # Construct content with images
            content = ""

            header = soup.find("div", class_="title-wrapper")
            if header is not None:
                header_text = header.find("h1", class_="ui header")
                if header_text is not None:
                    content += f"<h1>{header_text.text}</h1>"

            for p in text_container.findAll("p"):
                if p.find("img"):
                    media: str = p.find("img")["data-media-id"]
                    content += (
                        f"<p>"
                        f'<img src="{get_chapter_content_image(media)}">'
                        f"</p>"
                    )
                else:
                    content += str(p)
            return content

    def get_preview(self, manga: Manga):
        if manga.preview_url:
            return get_html(
                manga.preview_url,
                headers=self.headers,
                content_type="content",
            )

    def get_manga_url(self, manga: Manga) -> str:
        return f"{URL_RANOBEHUB}/ranobe/{manga.content_id}"
