import requests
from bs4 import BeautifulSoup

from const import URL_RULATE, DEFAULT_HEADERS
from items import Manga, Chapter, Image, Genre, RequestForm
from parser.Parser import Parser
from static import get_html


class Rulate(Parser):
    catalog_name = 'Rulate'

    def __init__(self):
        self.url_api = URL_RULATE
        self.headers = DEFAULT_HEADERS
        self.catalog_id = 3

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def search_manga(self, params: RequestForm) -> [Manga]:
        params = {'t': params.search}
        html = get_html(f"{self.url_api}/search", headers=self.headers, params=params)
        soup = BeautifulSoup(html.text, "html.parser")
        hranobe = soup.findAll('p', class_='book-tooltip')
        ranobe = []
        for i in hranobe:
            fname = i.text.strip()
            name = fname
            id = i.unwrap()['data-tooltip-content'].split('#book-tooltip-')[-1]
            data = {'id': id, 'name': name, 'catalog_id': self.catalog_id}
            ranobe.append(Manga(data))
        return ranobe

    def get_chapters(self, manga: Manga) -> [Chapter]:
        chapters = []
        a = get_html(f"{self.url_api}/book/{manga.id}", headers=DEFAULT_HEADERS)
        soup = BeautifulSoup(a.text, "html.parser")
        hchapters = soup.findAll('tr', class_='chapter_row')
        for chapter in hchapters:
            name: str = chapter.find('td', class_='t').text
            name = name.strip()
            id = chapter.unwrap()['data-id']
            data = {'id': id, 'title': name}
            chapters.append(Chapter(data))
        chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        a = get_html(f"{self.url_api}/book/{manga.id}/{chapter.id}/download?format=t&enc=UTF-8",
                     headers=DEFAULT_HEADERS)

        return [Image({'text': a.text})]

