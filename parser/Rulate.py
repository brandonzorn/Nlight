from bs4 import BeautifulSoup

from const import URL_RULATE, DEFAULT_HEADERS
from items import Manga, Chapter, Image, RequestForm
from parser.Parser import Parser
from utils import get_html


class Rulate(Parser):
    catalog_name = 'Rulate'

    def __init__(self):
        self.url_api = URL_RULATE
        self.headers = DEFAULT_HEADERS
        self.catalog_id = 3

    def get_manga(self, manga: Manga) -> Manga:
        html = get_html(f"{self.url_api}/book/{manga.id}")
        soup = BeautifulSoup(html.text, "html.parser")
        hranobe = soup.find('div', style="margin: 20px 0 0 0")
        description = hranobe.findAll('p')[0].text
        manga.description = description
        return manga

    def search_manga(self, params: RequestForm):
        params = {'t': params.search, 'cat': 12, 'Book_page': params.page, 'sort': 5}
        html = get_html(f"{self.url_api}/search", params=params)
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

    def get_chapters(self, manga: Manga):
        chapters = []
        a = get_html(f"{self.url_api}/book/{manga.id}")
        soup = BeautifulSoup(a.text, "html.parser")
        hchapters = soup.findAll('tr', class_='chapter_row')
        for chapter in hchapters:
            name: str = chapter.find('td', class_='t').text
            name = name.strip()
            id = chapter.unwrap()['data-id']
            data = {'id': id, 'title': name, 'language': 'ru'}
            chapters.append(Chapter(data))
        chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/book/{manga.id}/{chapter.id}/download?format=t&enc=UTF-8"
        return [Image({'is_text': True, 'page': 1, 'img': url})]

    def get_image(self, image: Image):
        a = get_html(image.img)
        return a

    def get_preview(self, manga: Manga):
        a = get_html(f"{self.url_api}/book/{manga.id}")
        soup = BeautifulSoup(a.text, "html.parser")
        himage = soup.find('meta', property="og:image")
        return get_html(himage['content'])
