import base64

from bs4 import BeautifulSoup

from nlightreader.consts.items import RulateItems
from nlightreader.core.enums import Language, MangaKind
from nlightreader.items import RequestForm
from nlightreader.models import Chapter, Image, Manga
from nlightreader.parsers.catalogs_base import AbstractRanobeCatalog
from nlightreader.utils.utils import get_html


class Rulate(AbstractRanobeCatalog):
    CATALOG_ID = 3
    CATALOG_NAME = "Rulate"
    _FILTERS = RulateItems
    _URL = "https://tl.rulate.ru"
    _COOKIES = {
        "mature": "c3a2ed4b199a1a15f5a5483504c7a75a7030dc4bi%3A1%3B",
    }

    def get_manga(self, manga: Manga) -> Manga:
        response = get_html(
            f"{self._URL}/book/{manga.content_id}",
            cookies=self._COOKIES,
            content_type="text",
        )
        if not isinstance(response, str):
            return manga
        soup = BeautifulSoup(response, "html.parser")
        hranobe = soup.find("div", style="margin: 20px 0 0 0")
        if not hranobe:
            return manga
        description_text = hranobe.text
        if description_text:
            manga.add_description(
                Language.undefined,
                str(description_text),
            )
        manga.kind = MangaKind.ranobe
        return manga

    def search_manga(self, form: RequestForm) -> list[Manga]:
        params = {
            "t": form.search,
            "cat": 12,
            "Book_page": form.page,
            "sort": form.get_order_id(),
            "adult": 0,
        }
        response = get_html(
            f"{self._URL}/search",
            params=params,
            content_type="text",
        )

        ranobe: list[Manga] = []
        if not isinstance(response, str):
            return ranobe

        soup = BeautifulSoup(response, "html.parser")
        hranobe = soup.find_all("p", class_="book-tooltip")
        for i in hranobe:
            name_text = i.text.strip()
            name_items = name_text.split("/")
            name = name_text
            russian = ""
            if len(name_items) == 2:
                name = name_items[0].strip()
                russian = name_items[1].strip()
            ranobe_id = str(
                i.unwrap()["data-tooltip-content"].split(
                    "#book-tooltip-",
                )[-1],
            )
            ranobe.append(
                Manga(
                    ranobe_id,
                    self.CATALOG_ID,
                    name,
                    russian,
                ),
            )
        return ranobe

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        chapters = []
        response = get_html(
            f"{self._URL}/book/{manga.content_id}",
            cookies=self._COOKIES,
            content_type="text",
        )
        if not isinstance(response, str):
            return chapters
        soup = BeautifulSoup(response, "html.parser")
        ranobe_chapters = soup.find_all("tr", class_="chapter_row")
        for chapter_data in reversed(ranobe_chapters):
            if chapter_data.find(
                "span",
                class_="disabled",
            ) or chapter_data.find("i", class_="ac_read g"):
                continue
            name: str = chapter_data.find("td", class_="t").text
            name = name.strip()
            chapter_id = chapter_data.unwrap()["data-id"]

            chapter = Chapter(
                chapter_id,
                self.CATALOG_ID,
                None,
                "",
                name,
                Language.ru,
            )
            chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = (
            f"{self._URL}/book/"
            f"{manga.content_id}/{chapter.content_id}/ready_new"
        )
        return [Image("", 1, url)]

    def get_image(self, image: Image) -> str | None:
        def get_chapter_content_image(media_id: str) -> str:
            url = f"{self._URL}/{media_id}"
            if media_id.startswith("http"):
                url = media_id
            chapter_image = get_html(
                url,
                headers=self._HEADERS,
                content_type="content",
            )
            if not isinstance(chapter_image, bytes):
                return ""
            str_equivalent_image = base64.b64encode(chapter_image).decode()
            return f"data:image/jpg;base64,{str_equivalent_image}"

        response = get_html(
            image.url,
            cookies=self._COOKIES,
            content_type="text",
        )
        if not isinstance(response, str):
            return None
        soup = BeautifulSoup(response, "html.parser")
        text_container = soup.find("div", class_="content-text")
        if not text_container:
            return None

        content = ""
        for p in text_container:
            if p.find("img") and not isinstance(p.find("img"), int):
                img_src = get_chapter_content_image(p.find("img")["src"])
                content += f'<p><img src="{img_src}"></p>'
            else:
                content += f"<p>{p.text}</p>"
        return content

    def get_preview(self, manga: Manga) -> bytes | None:
        response = get_html(
            f"{self._URL}/book/{manga.content_id}",
            cookies=self._COOKIES,
            content_type="text",
        )
        if not isinstance(response, str):
            return None
        soup = BeautifulSoup(response, "html.parser")
        himage = soup.find("meta", property="og:image")
        if not himage:
            return None
        image_response = get_html(
            str(himage["content"]),
            content_type="content",
        )
        if not isinstance(image_response, bytes):
            return None
        return image_response

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self._URL}/book/{manga.content_id}"


class Erolate(Rulate):
    CATALOG_ID = 5
    CATALOG_NAME = "Erolate"
    _URL = "https://erolate.com"
    _COOKIES = {
        "mature": "7da3ee594b38fc5355692d978fe8f5adbeb3d17di%3A1%3B",
    }

    def search_manga(self, form: RequestForm) -> list[Manga]:
        ranobe: list[Manga] = []
        params = {
            "t": form.search,
            "cat": 2,
            "Book_page": form.page,
            "sort": form.get_order_id(),
            "adult": 0,
        }
        response = get_html(
            f"{self._URL}/search",
            params=params,
            content_type="text",
        )
        if not isinstance(response, str):
            return ranobe
        soup = BeautifulSoup(response, "html.parser")
        hranobe = soup.find_all("p", class_="book-tooltip")
        for i in hranobe:
            name_text = i.text.strip()
            name_items = name_text.split("/")
            name = name_text
            russian = ""
            if len(name_items) == 2:
                name = name_items[0].strip()
                russian = name_items[1].strip()
            ranobe_id = i.unwrap()["data-tooltip-content"].split(
                "#book-tooltip-",
            )[-1]
            ranobe.append(
                Manga(
                    ranobe_id,
                    self.CATALOG_ID,
                    name,
                    russian,
                ),
            )
        return ranobe


__all__ = ["Rulate", "Erolate"]
