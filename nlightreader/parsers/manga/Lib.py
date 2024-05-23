import json
import re

from bs4 import BeautifulSoup

from nlightreader.consts.items import MangaLibItems
from nlightreader.consts.urls import URL_SLASHLIB, URL_MANGALIB
from nlightreader.consts.enums import Nl
from nlightreader.items import RequestForm, Manga, Chapter, Image
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import get_html, get_data


class LibBase(AbstractMangaCatalog):
    def __init__(self):
        super().__init__()
        self.url = None
        self.items = MangaLibItems

    def get_manga(self, manga: Manga):
        url = f"{self.url}/manga-short-info?slug={manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            manga.name = response.get("name")
            manga.russian = response.get("rus_name")
            manga.score = response.get("rate_avg")

            manga.add_description(Nl.Language.undefined, response.get("summary"))
        return manga

    def search_manga(self, form: RequestForm):
        url = f"{self.url}/manga-list"
        params = {
            "name": form.search,
            "page": form.page,
            "sort": form.get_order_id(),
            "types[]": form.get_kind_ids(),
            "genres[include][]": form.get_genre_ids(),
        }
        response = get_html(
            url,
            headers=self.headers,
            params=params,
            content_type="text",
        )
        mangas = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            cards = soup.find_all("a", class_="media-card")
            for card in cards:
                card_sub_info = card.find("div", class_="media-card__caption")
                kind_el = card_sub_info.find("h5", class_="media-card__subtitle")
                title_el = card_sub_info.find(
                    "h3", class_="media-card__title line-clamp")
                manga = Manga(
                    card.get("data-media-slug"),
                    self.CATALOG_ID,
                    title_el.text,
                    "",
                )
                manga.kind = Nl.MangaKind.from_str(kind_el.text)
                manga.preview_url = card.get("data-src")
                mangas.append(manga)
        return mangas

    def get_chapters(self, manga: Manga):
        url = f"{self.url}/{manga.content_id}?section=chapters&ui=2239878"
        response = get_html(url, headers=self.headers, content_type="text")
        chapters = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            script_tag = soup.find("script", text=re.compile(r"window\.__DATA__"))
            script_content = script_tag.text if script_tag else None
            match = re.search(r"window\.__DATA__\s*=\s*(.*?}});", script_content)
            data = json.loads(match.group(1))
            for i in get_data(data, ["chapters", "list"]):
                vol = i.get("chapter_volume")
                ch = i.get("chapter_number")
                vol = str(vol) if vol is not None else vol
                ch = str(ch) if ch is not None else ch
                chapter = Chapter(
                    i.get("chapter_id"), self.CATALOG_ID, vol, ch, i.get("chapter_name"),
                )
                chapter.language = Nl.Language.ru
                chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url}/{manga.content_id}/v{chapter.vol}/c{chapter.ch}?ui=2239878"
        response = get_html(url, headers=self.headers, content_type="text")
        images = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            pages_data_tag = soup.find(
                "script", id="pg", text=re.compile(r"window\.__pg"),
            )
            pages_data_content = pages_data_tag.text if pages_data_tag else None
            pages_data_match = re.search(
                r"window\.__pg\s*=\s*(.*?}]);", pages_data_content,
            )
            pages_data = json.loads(pages_data_match.group(1))

            metadata_info_tag = soup.find(
                "script", text=re.compile(r"window\.__info"),
            )
            metadata_info_content = metadata_info_tag.text if metadata_info_tag else None
            metadata_info_match = re.search(
                r"window\.__info\s*=\s*(.*?}});", metadata_info_content,
            )
            metadata_info_data = json.loads(metadata_info_match.group(1))

            chapter_link = metadata_info_data["img"]["url"]
            server_link = metadata_info_data["servers"]["main"]
            for i in pages_data:
                page_num = i.get("p")
                file_name = i.get("u")
                img_url = f"{server_link}{chapter_link}{file_name}"
                image = Image("", page_num, img_url)
                images.append(image)
        return images

    def get_image(self, image: Image):
        headers = self.headers | {"Referer": f"{self.url}/"}
        return get_html(image.img, headers=headers, content_type="content")

    def get_preview(self, manga: Manga):
        headers = self.headers | {"Referer": f"{self.url}/"}
        return get_html(manga.preview_url, headers=headers, content_type="content")

    def get_manga_url(self, manga: Manga):
        return f"{self.url}/{manga.content_id}"


class SlashLib(LibBase):
    CATALOG_NAME = "SlashLib(Legacy)"
    CATALOG_ID = 9

    def __init__(self):
        super().__init__()
        self.url = URL_SLASHLIB


class MangaLib(LibBase):
    CATALOG_NAME = "MangaLib(Legacy)"
    CATALOG_ID = 10

    def __init__(self):
        super().__init__()
        self.url = URL_MANGALIB
