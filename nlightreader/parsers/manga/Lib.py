import json
import re

from bs4 import BeautifulSoup

from nlightreader.consts import URL_SLASHLIB, URL_MANGALIB, Nl
from nlightreader.items import RequestForm, Manga, Chapter
from nlightreader.parsers.Parser import Parser
from nlightreader.utils.utils import get_html, get_data


class LibBase(Parser):
    def __init__(self):
        super().__init__()
        self.url = None

    def search_manga(self, form: RequestForm):
        url = f"{self.url}/manga-list"
        params = {
            "name": form.search,
            "page": form.page,
        }
        response = get_html(url, headers=self.headers, params=params, content_type="text")
        mangas = []
        if response:
            soup = BeautifulSoup(response, "html.parser")
            cards = soup.find_all("a", class_="media-card")
            for card in cards:
                card_sub_info = card.find("div", class_="media-card__caption")
                kind_el = card_sub_info.find("h5", class_="media-card__subtitle")
                title_el = card_sub_info.find("h3", class_="media-card__title line-clamp")
                manga = Manga(card.get("data-media-slug"), self.CATALOG_ID, title_el.text, "")
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
            script_tag = soup.find('script', text=re.compile(r'window\.__DATA__'))
            script_content = script_tag.text if script_tag else None
            match = re.search(r'window\.__DATA__\s*=\s*(.*?}});', script_content)
            data = json.loads(match.group(1))
            for i in get_data(data, ["chapters", "list"]):
                vol = i.get("chapter_volume")
                ch = i.get("chapter_number")
                vol = str(vol) if vol is not None else vol
                ch = str(ch) if ch is not None else ch
                chapter = Chapter(i.get("chapter_id"), self.CATALOG_ID, vol, ch, i.get("chapter_name"))
                chapter.language = Nl.Language.ru
                chapters.append(chapter)
        return chapters

    def get_preview(self, manga: Manga):
        response = get_html(manga.preview_url, content_type="content")
        return response

    def get_manga_url(self, manga: Manga):
        return f"{self.url}/{manga.content_id}"


class SlashLib(LibBase):
    CATALOG_NAME = "SlashLib"
    CATALOG_ID = 9

    def __init__(self):
        super().__init__()
        self.url = URL_SLASHLIB


class MangaLib(LibBase):
    CATALOG_NAME = "MangaLib"
    CATALOG_ID = 10

    def __init__(self):
        super().__init__()
        self.url = URL_MANGALIB